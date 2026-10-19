---
title: "PSWGCommon: arquitetura e guia de leitura"
---

# PSWGCommon: arquitetura e guia de leitura

Análise de 19/10/2026 da revisão `9ab4234e94be480f3b48f539a1f0dd6f5bd408a4` de [ProjectSWGCore/pswgcommon](https://github.com/ProjectSWGCore/pswgcommon/tree/9ab4234e94be480f3b48f539a1f0dd6f5bd408a4). A biblioteca reúne contratos de dados, codecs de mensagens, leitores de assets e utilitários compartilhados por aplicações ProjectSWG. O módulo JPMS chama-se `com.projectswg.common`; o artefato Gradle declara grupo `com.projectswg`, versão `1.0.0` e plugin `java-library`.

O código se identifica como parte do emulador NGE baseado no publish final anterior aos eventos de encerramento. Isso importa ao comparar layouts com a documentação histórica e com o cliente `SWGEmu.exe` disponível neste workspace: a identidade de uma classe ou opcode não demonstra identidade de versão nem de todos os campos. Nenhuma página de pacote recebeu status de confirmação binária apenas por existir na biblioteca.

## Como navegar pela análise

| Guia | Pergunta respondida |
| --- | --- |
| [Rede, codecs e replicação](pswgcommon-network.md) | Como bytes viram mensagens; endian, strings, framing, factories, OCM, baseline, delta e HCAP |
| [Dados e persistência](pswgcommon-data.md) | Como objetos compartilhados são representados em rede, Mongo, customização, OOB e SUI |
| [Assets e terreno](pswgcommon-assets.md) | Como os dois sistemas IFF carregam dados, resolvem formatos, mantêm caches e calculam terreno |
| [Comparação com o binário](pswgcommon-binary.md) | O que REA e Binary Ninja conseguiram verificar e o que continua desconhecido |
| [Mensagens comparadas com o cliente](pswgcommon-client-messages.md) | Tipos e layouts de contenção, criação na cena e chat; divergências de contador e strings |
| [Catálogo de fontes e mensagens](pswgcommon-catalog.md) | Onde estão os arquivos, pacotes e correspondências nominais com o portal |

O [inventário JSON](../../data/pswgcommon-inventory.json) preserva caminhos, hashes e classificação dos arquivos. É um inventário lexical: não substitui leitura das implementações, resolução de herança nem call graph. O catálogo liga mensagens às páginas existentes por nome; isso é uma pista de navegação, não uma validação de esquema.

## Fluxos principais

```text
Consumidor (por exemplo, servidor)
  -> modelos Encodable -> NetBuffer -> SWGPacket.encode()
  -> NetworkProtocol.encode() -> envelope de comprimento -> consumidor de I/O

Entrada do consumidor -> NetworkProtocol.decode()
  -> opcode -> PacketType -> pacote concreto -> NetBuffer -> valores do modelo
  -> caso ObjectController: segundo despacho pelo controller ID

Arquivo local do cliente
  -> ClientFactory / SWGFile / visitantes (API swgfile)
  OU SWGParser / IffForm / SWGParserFactory / cache (API swgiff)
  -> dados de objetos, aparência, portais, slots ou terreno

Modelo MongoPersistable -> MongoData -> documento BSON
```

Esses fluxos têm contratos diferentes. O envelope de comprimento de `NetworkProtocol` não demonstra implementação completa de transporte SOE. Um `Encodable` não possui necessariamente envelope próprio. Dados Mongo não são cópia automática dos bytes de rede. As duas APIs IFF têm registros de formatos e estado de leitura distintos.

## Mapa de responsabilidades

| Área de fontes | Papel e pontos de entrada |
| --- | --- |
| `encoding` | `Encodable`, `Encoder`, `CachedEncode`: contrato binário, conversões e cache de bytes |
| `network` | `NetBuffer`, `NetBufferStream`, `NetworkProtocol`, TLS; delegação de I/O ao consumidor |
| `network.packets` | Bases SWG/SOE, registro `PacketType`, mensagens de aplicação e controllers |
| `network.hcap` | Entrada/saída de registros de captura e reconstrução de mensagens |
| `data.encodables` | Chat, correio, GCW, mapa, flags de tangible e pacotes de texto OOB |
| `data.location`, `data.math` | Posição, orientação, terreno, geometria e volumes usados pelos modelos e parsers |
| `data.customization` | Variáveis de aparência e formato compacto de customização |
| `data.sui`, `data.radial` | Construção de interface SUI e representações de menus |
| `data.swgfile` | Leitor IFF e visitantes para dados extraídos do cliente |
| `data.swgiff` | Outra árvore IFF, parsers especializados, cache e motor de terreno |
| `data.info`, `utilities`, `process` | Configuração, caminhos locais, conversões, threads, relógio e lançamento de JAR |

As enumerações e estruturas restantes, como combate, objetos e schematic, são indexadas no catálogo. Não se deve inferir implementação de regras de jogo pela presença desses tipos. A aplicação que usa a biblioteca decide autorização, ciclo de vida de objetos e tratamento dos valores recebidos.

## Build e dependências

`build.gradle.kts` configura Java/Kotlin mistos em `src/main/java`, JUnit Jupiter e compilação modular. Exporta como dependências de API annotations `20.1.0`, `jlcommon 1.10.1` e Bouncy Castle `1.71`; usa Kotlin stdlib e MongoDB sync driver `3.12.2` na implementação. O descritor JPMS declara os módulos requeridos e os packages exportados. Fonte: [build.gradle.kts](https://github.com/ProjectSWGCore/pswgcommon/blob/9ab4234e94be480f3b48f539a1f0dd6f5bd408a4/build.gradle.kts) e [module-info.java](https://github.com/ProjectSWGCore/pswgcommon/blob/9ab4234e94be480f3b48f539a1f0dd6f5bd408a4/src/main/java/module-info.java).

A árvore isolada não contém wrapper nem `settings.gradle.kts`. A versão do plugin Kotlin e as propriedades extras `javaVersion` e `kotlinTargetJdk` são fornecidas externamente. No checkout local de `Holocore`, `settings.gradle.kts` inclui `pswgcommon`, `.gitmodules` aponta para este repositório e o build pai fornece essas propriedades. Porém, o subdiretório `Holocore/pswgcommon` estava vazio durante a inspeção; o clone analisado é o diretório irmão. Logo, executar o wrapper do pai sem preparar seu submódulo não testa automaticamente as fontes aqui analisadas. Não foi escolhido um JDK arbitrário nem declarada compilação bem-sucedida.

O `module-info.java` expõe `jlcommon` e `java.management` transitivamente, declara `java.sql` e `java.desktop` como `requires static`, além de BSON, annotations, Bouncy Castle e Kotlin. A biblioteca não oferece um `main` de servidor: `JarProcessBuilder` apenas monta um comando Java com opções de memória/VM e chama `ProcessBuilder.start()` quando solicitado. Fonte: `process/JarProcessBuilder.java:161–198`.

## Recursos e estado compartilhado

O recurso `data/crc_database.csv` permite mapear CRCs conhecidos para nomes; não inverte matematicamente o hash. `customization_variables.sdb` fornece IDs de variáveis de aparência. Os leitores de assets procuram por padrão uma árvore local `clientdata`; não há extração TRE implícita nesse caminho. A disponibilidade desses dados afeta o resultado e os testes de terreno.

Caches não são intercambiáveis: `CachedEncode` conserva bytes até invalidação explícita, enquanto os leitores de assets possuem caches de objetos e cursores de leitura próprios. Antes de compartilhar instâncias entre threads ou reserializar um objeto decodificado, confira o contrato do tipo. O guia de rede e o de assets descrevem os casos concretos em que leitura seguida de escrita não preserva os dados.

## Resultado e limites da investigação

| Questão | Estado | Evidência e limite |
| --- | --- | --- |
| Módulo, build e dependências | Respondida por fontes | Build e descritor JPMS; compilação não executada |
| Codecs e despacho de mensagens | Respondida na arquitetura | Implementações e exemplos derivados; não houve revisão campo a campo de todas as mensagens |
| Baseline, delta e OCM | Parcial | Envelopes e factories documentados; sem reconstrução de todas as views de objetos no consumidor |
| Modelos, customização e persistência | Respondida nos contratos centrais | Fontes e testes existentes lidos; testes da JVM não executados |
| Assets e terreno | Respondida na arquitetura, parcial nos formatos | Registros e parsers lidos; faltam corpus de assets/versionamento e testes dinâmicos |
| Correspondência com o cliente | Parcial | Tabela CRC e três layouts de mensagens confrontados com o Binary Ninja; consumidores semânticos ainda parciais |
| REA nativo | Limitado pelo provedor | Ghidra/REA no Windows recusou PE x86; resposta preservada |
| Inventário da árvore | Respondida como inventário lexical | JSON com arquivos e hashes; não é cobertura semântica integral |

Próximas verificações úteis são testes de ida e volta de baseline/OOB/customização, limites de framing, fixtures UTF-8 e leitura de floats após operações big-endian; depois, comparação de mensagens selecionadas contra o cliente da versão correta. Os achados descritos são problemas ou lacunas observados por inspeção; esta atualização altera documentação, não a biblioteca.
