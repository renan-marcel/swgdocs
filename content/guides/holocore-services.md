---
title: "Holocore: serviços, intents e gameplay"
---

# Holocore: serviços, intents e gameplay

A revisão [ff53903bbb8b0ff2edcd2493d66f940767036aaa](https://github.com/ProjectSWGCore/Holocore/tree/ff53903bbb8b0ff2edcd2493d66f940767036aaa) organiza o servidor em managers e serviços que recebem Intent tipados. As classes de domínio carregam dados; handlers de serviços conectam entrada de rede, validação, estado do mundo e respostas de protocolo.

## Managers

ProjectSWG.run cria dois managers raiz em ordem explícita: GameplayManager e depois SupportManager. O código comenta que essa ordem garante que Gameplay veja intents de Support. Os filhos declarados nos managers oferecem o mapa funcional:

| Manager | Áreas declaradas |
| --- | --- |
| GameplayManager | Bazaar, combate, conversas, crafting, entretenimento, facção, Jedi, missões, jogador, estruturas, comércio e mundo |
| SupportManager | Dados de suporte, objetos, serviços globais e NPCs |
| GlobalManager | Administração, chat, comandos, health, rede e zonas |
| ObjectManager | Awareness, objetos, buildouts estáticos, itens, radiais e armazenamento |

As relações de filhos são declarações de composição. A criação de cada manager não significa que toda funcionalidade esteja completa ou ativa em todas as configurações.

## Intents como ligação entre subsistemas

Um intent representa um evento ou pedido tipado. Por exemplo, os intents de objetos incluem criar, destruir, mover, teleportar e transferir entre containers. Um serviço publica intents e outro método anotado com @IntentHandler os recebe. Esse padrão desacopla o socket do processamento de gameplay.

Exemplo resumido da entrada de movimento:

    pacote inbound
      -> serviço de awareness valida jogador/objeto e condições
      -> MoveObjectIntent
      -> serviços que observam movimento atualizam domínio e notificações

O contrato de despacho é fornecido por jlcommon, uma biblioteca externa. As fontes de Holocore demonstram anotações e broadcasts, mas não estabelecem aqui garantias de transação, ordenação global ou entrega exatamente uma vez.

## Objetos, zona e persistência

ObjectStorageService coordena objetos persistentes, estado em memória e objetos estáticos de buildout. No início, carrega buildouts de dados preparados e objetos salvos, reconstrói relações de parent/container e publica intents de criação. Um pool de uma thread salva objetos periodicamente (intervalo observado: cinco minutos) e durante encerramento; destruição remove as referências persistidas correspondentes.

Isso separa duas origens:

- Buildouts e dados de mundo vêm de serverdata, gerado a partir de dados do cliente.
- Estado mutável persistente é reconstruído/gravado na base configurada, normalmente MongoDB.

O código de persistência contém caminhos de recursão e TODOs, então essa descrição é do comportamento visível, não uma garantia de durabilidade para cada tipo de objeto.

## Exemplos de gameplay

O serviço de mensagem privada localiza o destinatário pelo primeiro nome, rejeita destinatários ausentes ou fora do estado ZONED_IN, verifica a lista de ignorados, responde ao remetente e encaminha a mensagem ao destinatário. A mensagem de resposta do servidor é ChatInstantMessageToClient, cujo layout no cliente foi confrontado com Binary Ninja.

No fluxo de entrada de personagem no mundo, CreatureObjectAwareness emite a criação de cena, baselines e atualização de contenção quando o objeto tem pai. Esse encadeamento conecta objetos do servidor às estruturas de rede que o cliente consome. Não se deve interpretar a criação do objeto como confirmação de que seus handlers ou todas as regras posteriores foram analisados.

## Persistência e configuração

PswgDatabase fornece coleções para configuração, usuários, objetos, recursos, bazaar e chat. A configuração é consultada por serviço/pacote; algumas tabelas podem usar outro backend quando há configuração de roteamento. Os argumentos de inicialização incluem URI do banco e nome lógico. No ambiente de desenvolvimento, docker-compose.yml define MongoDB e mongo-express.

Não foram iniciados containers nem conectada uma base durante esta análise. O teste de ambiente da aplicação, migrações de dados e garantias de recuperação continuam fora do escopo verificado.

## Fontes consultadas

- [ProjectSWG.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/ProjectSWG.kt#L66)
- [GameplayManager.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/gameplay/GameplayManager.kt)
- [SupportManager.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/SupportManager.kt)
- [ObjectStorageService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/objects/ObjectStorageService.java#L59)
- [LoginService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/zone/LoginService.java)

\n