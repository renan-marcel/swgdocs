---
title: "Holocore: fluxos de execução"
---

# Holocore: fluxos de execução

Esta página percorre a revisão [ff53903bbb8b0ff2edcd2493d66f940767036aaa](https://github.com/ProjectSWGCore/Holocore/tree/ff53903bbb8b0ff2edcd2493d66f940767036aaa) de ponta a ponta. Os diagramas resumem caminhos implementados em código. Chamadas de intent e ações de serviços representam eventos relacionados; o agendamento interno é fornecido por jlcommon, por isso o diagrama não presume execução síncrona ou transações.

## 1. Inicialização e encerramento

A entrada é ProjectSWG.main. Depois da leitura dos argumentos e da configuração de logs, o servidor verifica marker.txt, abre a base de dados, aponta o parser de IFF para serverdata, configura a galáxia e cria os gerenciadores globais de intents e coroutines. Inicia GameplayManager antes de SupportManager; o próprio código diz que a ordem permite a Gameplay receber intents de Support.

    ProjectSWG.run
      -> argumentos e logging
      -> valida marker.txt
      -> inicializa MongoDB
      -> SWGParser usa serverdata
      -> prepara galáxia
      -> cria IntentManager e HolocoreCoroutine
      -> GameplayManager.start()
      -> SupportManager.start()
      -> publica estado OPEN
      -> Manager.run(..., 50)
      -> estado TERMINATING
      -> Manager.stop(...)
      -> fecha IntentManager/coroutines
      -> fecha MongoDB e ScheduledUtilities

Ao inicializar seus serviços, ObjectStorageService carrega buildouts estáticos e documentos salvos. Os objetos carregados geram ObjectCreatedIntent para que os serviços interessados reconstruam índices e awareness. Na partida, os buildouts também são publicados como objetos criados.

## 2. Conexão, autenticação e sessão

Há estados diferentes para o socket e para a conta do jogador. O status interno da sessão WebSocket não é o mesmo que PlayerState.

    TCP aceita canal
      -> NetworkClient recebe conexão
      -> ConnectionOpenedIntent
      -> PlayerSessionService registra Player
      -> PlayerState = CONNECTED
      -> handshake WebSocket lê username/password/protocolVersion
      -> compara NetworkProtocol.VERSION
      -> envia HoloConnectionStarted
      -> RequestLoginIntent
      -> LoginService valida versão/conta/senha/banimento
      -> sucesso: PlayerState = LOGGED_IN
                  PlayerServer = LOGIN
                  retorna os dados de login pelo protocolo recebido
      -> falha: estado DISCONNECTED e resposta de erro

Os valores de username, password e protocolVersion vêm de parâmetros da URL e são decodificados com Base64 padrão do Java. A autenticação acontece depois da negociação WebSocket. O fluxo inclui tanto HoloLoginRequestPacket quanto o caminho legado LoginClientId. Uma versão inválida, conta ausente, banimento ou senha incorreta segue caminhos de erro específicos.

Há dois formatos de resposta no código: RequestLoginIntent, gerado no upgrade WebSocket, segue o caminho legado e envia token, cluster, flags e enumeração de personagens. Um HoloLoginRequestPacket recebido como pacote responde com HoloLoginResponsePacket contendo o resultado, galáxias e personagens.

| PlayerState | Significado no fluxo |
| --- | --- |
| DISCONNECTED | Sem sessão de jogador ativa ou login encerrado por falha |
| CONNECTED | A conexão foi associada a um Player |
| LOGGING_IN | Login em validação |
| LOGGED_IN | Autenticado; ainda na etapa de seleção/entrada na zona |
| ZONING_IN | Servidor enviou a cena e espera o cliente ficar pronto |
| ZONED_IN | Cliente respondeu CmdSceneReady e está na zona |

PlayerServer identifica qual etapa/protocolo de servidor está ativa (por exemplo, LOGIN ou ZONE); não é o estado de autenticação.

## 3. Seleção de personagem e entrada na zona

Após o login, ZoneService recebe ClientIdMsg e marca PlayerServer.ZONE. Quando chega SelectCharacter, busca o objeto pelo ID e passa a seleção para ZoneRequester. O requester rejeita personagem inexistente, objeto que não seja CreatureObject, personagem sem PlayerObject ou personagem já associado a outra sessão ativa. Se a validação passa, atribui o Player como dono e publica RequestZoneInIntent.

    SelectCharacter(characterId)
      -> ZoneService procura objeto
      -> ZoneRequester valida tipo, ghost e sessão existente
      -> atribui owner ao CreatureObject
      -> RequestZoneInIntent
      -> AwarenessService.handleZoneIn(...)
      -> move/reinicializa objeto e awareness
      -> PlayerState = ZONING_IN
      -> primeiro zone-in: heartbeat, status de chat e parâmetros
      -> CmdStartScene
      -> cliente carrega a cena
      -> CmdSceneReady
      -> PlayerState = ZONED_IN
      -> PlayerEvent.PE_ZONE_IN_SERVER

O zone-in inicial envia também eventos de primeiro acesso e pode produzir a mensagem configurada de boas-vindas. Teleporte ou viagem reutiliza o tratamento de zone-in quando muda o terreno. Estados inesperados durante essa transição podem fazer o servidor encerrar a conexão como suspeita.

## 4. Replicação de objetos para o cliente

Awareness mantém o conjunto de objetos visíveis a cada criatura. Quando esse conjunto muda, CreatureObjectAwareness calcula criações e destruições e atualiza observers. Para cada objeto novo, o servidor envia primeiro SceneCreateObjectByCrc e baselines 3 e 6; para o objeto do próprio jogador também envia baselines adicionais. Em seguida podem vir permissões de célula, postura, PvP e contenção. SceneEndBaselines fecha os grupos de criação; objetos que saem do conjunto recebem SceneDestroyObject.

    ObjectCreatedIntent / mudança de posição ou container
      -> AwarenessService atualiza conjunto visível
      -> CreatureObjectAwareness.flush(player)
      -> create: SceneCreateObjectByCrc
                baselines e dados auxiliares
                UpdateContainmentMessage se há parent
      -> destroy: SceneDestroyObject
      -> Player.sendPacket(...)
      -> NetworkClient codifica pacote
      -> frame binário WebSocket

Os leitores nativos de SceneCreateObjectByCrc e UpdateContainmentMessage foram confrontados com Binary Ninja na [análise de mensagens](holocore-network.md). O confronto cobre os layouts dessas mensagens selecionadas, não a totalidade da replicação.

## 5. Ação recebida e mudança no mundo

Como exemplo de pacote de movimento, ClientAwarenessService recebe DataTransform através do IntentMultiplexer. Antes de alterar o mundo, confirma que há personagem conectado, que o ID é o do personagem do jogador, que a postura permite movimento e que não há teleporte em andamento. A variante com parent também resolve o objeto pai e rejeita parent desconhecido. Montarias têm tratamento próprio.

    frame binário
      -> NetworkClient resolve CRC e decodifica pacote
      -> InboundPacketIntent(player, DataTransform)
      -> ClientAwarenessService valida identidade/estado/parent
      -> MoveObjectIntent
      -> AwarenessService aplica systemMove
      -> recalcula awareness e relações de parent
      -> transmite transforms e criação/destruição a observers
      -> Player.sendPacket -> WebSocket binário

Assim, o socket não aplica diretamente as regras do mundo. Ele converte bytes em pacote e intent; serviços de suporte validam e alteram estado, e a camada de awareness propaga as mudanças aos jogadores que observam os objetos.

## 6. Objetos e persistência

Dados estáticos e dados persistentes entram por caminhos separados. BuildoutLoader reconstrói objetos do mundo a partir de serverdata. ObjectStorageService também busca documentos salvos na base, recria objetos, restaura pais/células e waypoints, atualiza o próximo ID e publica ObjectCreatedIntent.

    boot: serverdata -> BuildoutLoader -> objectMap/buildouts
          MongoDB -> factories -> grafo pai/filho -> objectMap
          ObjectCreatedIntent -> índices, awareness e demais observers

    runtime: objeto persistente criado -> ObjectCreatedIntent -> gravação inicial
             conjunto persistido -> salvamento periódico (5 min)
             shutdown -> salvamento final -> fecha database

No código, o armazenamento periódico usa uma thread e intervalo de cinco minutos. A descrição não estabelece garantias ACID, recuperação contra falhas no meio da gravação ou cobertura de todos os tipos de objeto.

## 7. Como seguir outro fluxo

Para seguir uma funcionalidade específica, comece no pacote correspondente em intents, encontre os métodos @IntentHandler ou a entrada @Multiplexer, e acompanhe o pacote até os métodos sendPacket, ObjectCreatedIntent, MoveObjectIntent ou outro evento de saída. O contrato de despacho e escalonamento de jlcommon é externo. Os codecs de rede compartilhados são do submódulo pswgcommon; esse submódulo estava desinicializado no checkout examinado.

### Fontes principais

- [ProjectSWG.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/ProjectSWG.kt#L66)
- [NetworkClient.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/global/network/NetworkClient.kt#L98)
- [PlayerSessionService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/zone/PlayerSessionService.java)
- [LoginService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/zone/LoginService.java)
- [ZoneService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/zone/ZoneService.java)
- [ZoneRequester.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/global/zone/ZoneRequester.kt)
- [AwarenessService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/objects/awareness/AwarenessService.java)
- [ClientAwarenessService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/objects/awareness/ClientAwarenessService.java)
- [CreatureObjectAwareness.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/objects/swg/creature/CreatureObjectAwareness.kt)
- [ObjectStorageService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/objects/ObjectStorageService.java)
