---
title: "Holocore: arquitetura e mapa funcional"
---

# Holocore: arquitetura e mapa funcional

Leitura estática da revisão [ff53903bbb8b0ff2edcd2493d66f940767036aaa](https://github.com/ProjectSWGCore/Holocore/tree/ff53903bbb8b0ff2edcd2493d66f940767036aaa) de Holocore. O README descreve o projeto como emulador de servidor de Star Wars Galaxies voltado à era Combat Upgrade (CU), em desenvolvimento inicial. O código mistura Java e Kotlin e divide execução, regras de jogo, infraestrutura e ferramentas de conversão de dados.

O guia organiza os principais subsistemas e oferece caminhos de leitura. Ele não declara o comportamento do servidor completo ou compatibilidade integral com o jogo: os fluxos descritos são os que aparecem nas fontes inspecionadas. A análise não iniciou o servidor, não conectou à MongoDB e não executou cenários de cliente.

## Mapa dos guias

| Guia | Conteúdo |
| --- | --- |
| [Fluxos de execução](holocore-flows.md) | Inicialização, login, entrada na zona, awareness, ações de jogo e persistência |
| [Rede e protocolos](holocore-network.md) | TCP/WebSocket, handshake, despacho de CRC e mensagens confirmadas no cliente |
| [Serviços e gameplay](holocore-services.md) | Inicialização, managers, intents, objetos, login, chat e persistência |
| [Dados do cliente](holocore-clientdata.md) | Conversores, arquivos SDB/IFF, loaders e lacunas conhecidas |

O [inventário JSON](../../data/holocore-inventory.json) cataloga arquivos-fonte das pastas src/main, src/test e src/utility nessa revisão. É um índice por caminho e hash, não uma prova de que cada classe foi compreendida.

## Organização do projeto

- src/main/java/com/projectswg/holocore/services/gameplay reúne regras de gameplay: combate, crafting, entretenimento, facções, Jedi, jogador, estruturas, comércio e mundo.
- services/support abriga serviços de suporte, como dados do servidor, objetos, rede, chat, comandos, zonas e NPCs.
- intents define eventos tipados compartilhados entre serviços; resources contém dados e componentes de estado usados por esses fluxos.
- src/utility contém conversores de dados do cliente e utilitários de captura/análise de pacotes. src/test inclui testes unitários, testes de arquitetura e cenários headless.
- serverdata contém dados preparados para leitura pelo servidor. pswgcommon é um submódulo Git declarado em .gitmodules, mas estava desinicializado neste checkout. O código de codecs compartilhados precisa ser consultado no repositório separado [ProjectSWGCore/pswgcommon](https://github.com/ProjectSWGCore/pswgcommon/tree/9ab4234e94be480f3b48f539a1f0dd6f5bd408a4), e não atribuído às fontes locais de Holocore.

## Inicialização em alto nível

ProjectSWG.main transfere o controle para run. A sequência visível em ProjectSWG.kt é: interpretar argumentos, configurar logs, exigir o recurso marker.txt, abrir a base de dados, inicializar o parser de IFF com serverdata, preencher os metadados da galáxia, criar o IntentManager e o gerenciador de coroutines, iniciar GameplayManager e SupportManager, marcar o servidor aberto, executar os managers e, no encerramento, parar serviços e fechar recursos.

O código declara que Gameplay deve iniciar antes de Support para receber intents de Support. Esse comentário registra uma dependência de ordem entre os dois managers raiz. Detalhes do escalonamento interno pertencem a jlcommon, uma dependência externa, e não são inferidos aqui.

## Dependências e configuração

O build inclui o subprojeto :pswgcommon, Kotlin, coroutines, MongoDB, logging e bibliotecas de rede/utilidade. O servidor inicializa MongoDB com URI padrão mongodb://localhost e base padrão cu; várias configurações são lidas da coleção de configuração por serviço. O arquivo _config.yml no topo do repositório é configuração do GitHub Pages, não configuração do servidor.

O build define a ferramenta de conversão runClientdataConversion e testes JUnit. Nenhum build ou teste foi executado durante esta documentação. A versão de Java/Kotlin é definida pelo build e pode requerer toolchain compatível com o host.

## Evidência e limites

As descrições de arquitetura, serviços e dados abaixo vêm das fontes Java/Kotlin na revisão indicada. A comparação binária usa o SWGEmu.exe local, identificado por SHA-256 58012e57cebc499454812ba7ed96b1289db01e520963b4fc364edb41c322b2a8, analisado em Binary Ninja x86. Ela confirma estruturas selecionadas de mensagens no cliente; não confirma handlers, regras de gameplay, transporte em execução ou compatibilidade de todos os pacotes.

REA MCP não estava disponível nesta sessão. O diagnóstico local de REA indicou registro Codex ausente/desalinhado e identidade de skill antiga; nenhum arquivo de configuração foi alterado. Binary Ninja foi consultado diretamente e suas pseudodescompilações foram preservadas em [evidências do cliente](../../data/holocore-evidence/).

## Fontes consultadas

- [README.md](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/README.md)
- [ProjectSWG.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/ProjectSWG.kt#L66)
- [build.gradle.kts](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/build.gradle.kts)
- [.gitmodules](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/.gitmodules)

\n
