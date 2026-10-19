---
title: "Holocore: transporte de rede e fluxo de pacotes"
---

# Holocore: transporte de rede e fluxo de pacotes

Este guia acompanha a implementação local na revisão [ff53903bbb8b0ff2edcd2493d66f940767036aaa](https://github.com/ProjectSWGCore/Holocore/tree/ff53903bbb8b0ff2edcd2493d66f940767036aaa). Holocore implementa a conexão e o despacho para serviços. Os codecs SWG importados pertencem ao submódulo pswgcommon, que está desinicializado neste checkout; portanto, os detalhes de NetBuffer, CRC e classes de pacote são identificados como dependência externa.

## Caminho de entrada

NetworkClientService cria um servidor TCP e um serviço UDP na porta configurada bindPort (padrão 44463). A camada TCP usa NIO/selector. O fluxo normal do cliente segue uma negociação WebSocket sobre TCP: NetworkClient valida os parâmetros username, password e protocolVersion da URL, decodifica cada valor com o decoder Base64 padrão do Java, compara a versão do protocolo e notifica a conexão. Depois emite HoloConnectionStarted e um RequestLoginIntent.

Após a negociação, os dados binários recebidos são mensagens binárias WebSocket. O cliente exige pelo menos seis bytes, lê o CRC de 32 bits no deslocamento 2 via NetBuffer e escolhe o caminho:

    frame binário WebSocket
      -> mensagem SWG
      -> CRC no deslocamento 2
      -> ObjectController.decodeController(...) se for o CRC de controller
         ou PacketType.getForCrc(crc).decode(...) para pacote comum
      -> InboundPacketIntent
      -> serviço inscrito no tipo de pacote

Esse diagrama descreve o despacho de código observado. O framing interno, endian e mapeamento completo de CRCs residem nos codecs externos. A conexão também trata endpoints HTTP /health-check e /stats. O UDP é separado: datagrama iniciado pelo byte 1 recebe o byte 1 seguido do estado textual da galáxia.

## Entrada no login e sessões

O upgrade WebSocket fornece credenciais e versão. O código compara NetworkProtocol.VERSION; no caminho observado, o intent de login usa a string de versão de cliente fixa 20051010-17:00. O LoginService aceita HoloLoginRequestPacket e o caminho legado LoginClientId, verifica credenciais/estado, envia respostas de login e pode listar galáxias/personagens. A negociação de transporte e a autenticação são fases distintas no código.

Ao abrir a conexão, ConnectionOpenedIntent permite que o serviço de sessão associe a conexão a um jogador; fechar a conexão segue intents de fechamento. Pacotes recebidos viram intents para que serviços de domínio tratem o conteúdo.

## Caminhos de pacote vistos em Holocore

| Fluxo | Implementação no servidor |
| --- | --- |
| Atualização de objeto visível | CreatureObjectAwareness envia SceneCreateObjectByCrc, baselines e, se houver pai, UpdateContainmentMessage |
| Mensagem privada | ChatInstantMessageService recebe ChatInstantMessageToCharacter, verifica destinatário/estado/ignore e envia resposta e ChatInstantMessageToClient |
| Movimento recebido | ClientAwarenessService valida objeto, identidade, pai, postura e estado de teleporte antes de produzir MoveObjectIntent |

## Confronto com o Binary Ninja

O banco SWGEmu.exe.bndb foi aberto apenas para leitura no Binary Ninja. Nas funções nativas, os construtores e readers registram estes campos:

| Mensagem | CRC | Registro observado no cliente nativo |
| --- | --- | --- |
| SceneCreateObjectByCrc | FE89DDEA | NetworkId, Transform, uint32, bool |
| UpdateContainmentMessage | 56CBDE9E | NetworkId, NetworkId, int |
| ChatInstantMessageToClient | 3C565CED | ChatAvatarId, string UTF-16, string UTF-16 |

Os endereços e pseudocódigos dos readers e construtores estão preservados em [binary-ninja-client-messages.json](../../data/holocore-evidence/binary-ninja-client-messages.json) e [binary-ninja-client-readers.json](../../data/holocore-evidence/binary-ninja-client-readers.json). Para os dois primeiros layouts, a serialização de referência tem 47 e 26 bytes. A mensagem de chat ilustra que o cliente registra quatro operandos incluindo opcode, enquanto o serializer PSWGCommon analisado registra contador diferente. O guia [PSWGCommon: mensagens confrontadas com o cliente](pswgcommon-client-messages.md) detalha essas diferenças e os limites da evidência.

O confronto mostra que o código de Holocore usa classes cujos campos coincidem com as mensagens nativas selecionadas. Não demonstra que todos os pacotes de Holocore sejam compatíveis nem que o servidor foi aceito pelo cliente em execução.

## Fontes consultadas

- [NetworkClient.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/global/network/NetworkClient.kt#L67)
- [NetworkClientService.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/network/NetworkClientService.kt#L48)
- [LoginService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/zone/LoginService.java)
- [ChatInstantMessageService.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/services/support/global/chat/ChatInstantMessageService.java#L50)
- [CreatureObjectAwareness.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/objects/swg/creature/CreatureObjectAwareness.kt#L158)

\n