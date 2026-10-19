---
title: "PSWGCommon: codecs, pacotes e replicação"
description: "Mapa dos formatos e do despacho de mensagens implementados na biblioteca."
---

# PSWGCommon: codecs, pacotes e replicação

A [comparação de três mensagens com o cliente](pswgcommon-client-messages.md) complementa esta leitura das fontes: confirma layouts de contenção, criação e chat e mostra diferenças no contador e nos limites de strings de bytes.

Esta página descreve a implementação encontrada em `pswgcommon`, por leitura estática das fontes. Os exemplos de bytes são derivados das instruções de escrita; não são capturas de tráfego nem resultados de execução. A implementação é evidência do comportamento da biblioteca, mas não comprova por si só a compatibilidade com todas as versões do cliente SWG.

Todos os caminhos abaixo partem da raiz do workspace, que contém `pswgcommon` e `swgdocs`. Para abreviar referências, `J` significa `pswgcommon/src/main/java/com/projectswg/common/`. As linhas indicadas correspondem às fontes analisadas, e podem mudar com futuras revisões.

## Camadas e responsabilidades

| Camada | Responsabilidade observada | Fonte |
| --- | --- | --- |
| `Encodable` | Contrato de objeto binário: `decode(NetBuffer): Boolean`, `encode(): ByteArray`, `length` | `J/encoding/Encodable.kt:30` |
| `Encoder` | Conversão de valores e strings para arrays binários | `J/encoding/Encoder.kt:36` |
| `NetBuffer` | Cursor, primitivas, strings, arrays e listas sobre `ByteBuffer` | `J/network/NetBuffer.kt:37` |
| `SWGPacket` | Classe abstrata de mensagem de aplicação; valida o opcode esperado | `J/network/packets/SWGPacket.java:37` |
| `PacketType` | Registro opcode → classe e criação por reflexão | `J/network/packets/PacketType.java:354` |
| `NetworkProtocol` | Envelope com comprimento de 32 bits e despacho de mensagens SWG | `J/network/NetworkProtocol.java:36` |
| `ObjectController` | Segundo nível de despacho pelo identificador do controller | `J/network/packets/swg/zone/object_controller/ObjectController.java:45` |
| `SOEPacket` | Base independente que lê/escreve opcode SOE de 16 bits em ordem de rede | `J/network/packets/SOEPacket.java:38` |
| HCAP | Serialização de registros de captura e metadados de ambiente | `J/network/hcap/HcapOutputStream.java:42` |

`NetworkProtocol` não chama `SOEPacket`: seu prefixo de comprimento é um envelope próprio desta API. Não se deve acrescentá-lo automaticamente a um datagrama SOE ou interpretar essa classe como implementação completa de transporte confiável, fragmentação, compressão, criptografia e CRC de sessão. A constante `NetworkProtocol.VERSION` vale `20220620-15:00` (`NetworkProtocol.java:38`); ela não determina, isoladamente, a versão de um cliente.

## Primitivas e strings

`NetBuffer` é um buffer de capacidade fixa. `allocate` e `allocateDirect` criam os respectivos `ByteBuffer`; `wrap(ByteBuffer)` conserva a instância e seu cursor, enquanto `wrap(ByteArray)` cria um `ByteBuffer` sobre o array com posição inicial zero (`NetBuffer.kt:415`). Os métodos de adição avançam o cursor. `flip()` prepara o trecho escrito para leitura; `size()` representa a capacidade capturada na construção, e não o número de bytes escritos (`NetBuffer.kt:75`, `:403`).

| Operação | Codificação |
| --- | --- |
| `addShort`, `addInt`, `addLong` | 2, 4 ou 8 bytes, little-endian |
| `addFloat`, `addDouble` | IEEE 754 de 4 ou 8 bytes, little-endian |
| `addNetShort`, `addNetInt`, `addNetLong` | 2, 4 ou 8 bytes, big-endian |
| `addBoolean` | Um byte: `01` ou `00` |
| `addAscii` | Comprimento em bytes, short little-endian, seguido de UTF-8 |
| `addUnicode` | Comprimento em unidades UTF-16, int little-endian, seguido de UTF-16LE |
| `addArray` | Comprimento short little-endian + bytes |
| `addArrayLarge` | Comprimento int little-endian + bytes |
| `addRawArray` | Somente os bytes, sem comprimento |
| `addList` | Quantidade int little-endian + elementos serializados |
| `addByteSizedList` | Quantidade em um byte + elementos serializados |

Fontes: `NetBuffer.kt:99–202`. Apesar do nome `ASCII`, o charset é explicitamente UTF-8 (`:38`). Por exemplo, `addAscii("é")` escreve `02 00 C3 A9`; `addUnicode("A")` escreve `01 00 00 00 41 00`. O comprimento Unicode é `String.length`, isto é, unidades UTF-16, não necessariamente a quantidade de pontos de código visíveis.

Os getters `short`, `int`, `long` e os equivalentes `net*` alteram explicitamente a ordem do `ByteBuffer`. Já `float` e `double` apenas chamam `getFloat/getDouble`, herdando a ordem vigente (`NetBuffer.kt:224–246`). Em `allocate`, `allocateDirect` ou `wrap(ByteArray)`, sem nenhuma escrita/leitura anterior que mude a ordem, a ordem inicial de `ByteBuffer` é big-endian. `wrap(ByteBuffer)` conserva a ordem configurada na instância recebida. Após `getInt()`, a próxima leitura de float seguirá little-endian; após `getNetInt()`, seguirá big-endian. `rewind()` e `flip()` não redefinem essa ordem. Isso não significa que todos os pacotes leiam floats incorretamente: seus cabeçalhos normalmente já leem inteiros little-endian. O risco concreto está em um primeiro float ou na mistura com campos `net*`.

Há outras diferenças importantes entre os dois caminhos de codificação:

- `Encoder.encode(Double)` converte o valor para float de 32 bits; `NetBuffer.addDouble` mantém 64 bits (`Encoder.kt:45`, `:59`; `NetBuffer.kt:124`).
- `Encoder.encodeAscii` aloca `2 + string.length` e escreve UTF-8. Caracteres multibyte podem exceder essa capacidade; o prefixo também usa caracteres, diferentemente de `NetBuffer.addAscii`, que usa a quantidade de bytes (`Encoder.kt:91`; `NetBuffer.kt:103`, `:148`).
- `NetBuffer.array` lê um short **com sinal** como tamanho. Valores de 32768 a 65535 escritos no prefixo tornam-se negativos na leitura (`NetBuffer.kt:248`). Não existe validação geral de tamanho máximo nas rotinas de array.
- O getter boolean aceita somente `01` como verdadeiro (`NetBuffer.kt:206`). Outros valores diferentes de zero não são tratados como verdadeiro.
- `array()` expõe o array de apoio, inclusive bytes não escritos. Em buffers diretos a operação subjacente `ByteBuffer.array()` não é suportada; usar `allocateDirect()` não torna todos os métodos compatíveis com armazenamento direto (`NetBuffer.kt:399`, `:423`).

Para objetos compostos, `getEncodable` e `getList(Class)` exigem construtor público sem argumentos e chamam `decode`. Falhas de reflexão são registradas; `decode == false` interrompe a leitura. `getList` pode devolver uma lista parcial após uma exceção de reflexão (`NetBuffer.kt:309–343`, `:380`). Não há rollback automático do cursor.

`CachedEncode` guarda e devolve o mesmo array até `clearCached()` (`J/encoding/CachedEncode.java:31–52`). A invalidação é responsabilidade do chamador; mutar o objeto ou o array devolvido não dispara nova serialização. A classe não fornece sincronização.

## Envelope e criação de pacotes

O caminho de saída de `NetworkProtocol.encode` é:

1. Chamar `SWGPacket.encode()`.
2. Aplicar `flip()` no buffer retornado.
3. Emitir comprimento little-endian de 4 bytes, sem incluir o próprio prefixo.
4. Copiar os bytes restantes e aplicar `flip()` no envelope.

Isso pressupõe que `encode()` devolva um buffer com o cursor **ao final da escrita**. Um pacote que já aplique `flip()` viola essa convenção e pode ser encapsulado como conteúdo vazio. Se a quantidade escrita divergir da capacidade, a classe registra aviso e usa a quantidade efetivamente escrita (`NetworkProtocol.java:40–51`).

Na entrada, `decode` lê o comprimento, extrai exatamente esse número de bytes e chama `decodePacket`. São exigidos pelo menos 6 bytes para ler um cabeçalho SWG: um short inicial e o opcode int little-endian. O opcode está no deslocamento 2 (`NetworkProtocol.java:78–109`). O short inicial é consumido por `SWGPacket.checkDecode`, mas seu valor não é validado (`SWGPacket.java:70`). Não é um comprimento universal: por exemplo, `HeartBeat.encode()` escreve `1`, enquanto Baseline, Delta e ObjectController escrevem `5`.

`PacketType` agrupa mensagens de login, criação de personagem, inserção na cena, chat, combate, comércio, leilão, interface SUI, espaço e outros subsistemas. A existência de uma classe concreta não basta para garantir despacho genérico: ela precisa de entrada no registro e construtor apropriado. `getForCrc` usa `getConstructor().newInstance()`, retorna `null` para opcode desconhecido e também após falha de instanciação (`PacketType.java:352–389`). O despachante chama `decode` no objeto criado. Controllers são tratados antes desse registro.

**Limitação estática de enquadramento:** `canDecode` restaura o cursor após ler o comprimento e compara `length <= remaining()`. Nesse ponto, `remaining()` ainda inclui os 4 bytes do prefixo (`NetworkProtocol.java:54–76`). Um envelope que anuncia 10 bytes mas contém somente 6 bytes de conteúdo já pode passar na verificação; a extração posterior ainda tentará ler 10. Para consumir um fluxo incremental com segurança, o chamador deve assegurar que há `4 + length` bytes disponíveis. Esta página registra o problema observado; não altera a implementação.

Comprimentos negativos geram `IOException("Stream corrupted")`. Payload menor que 6 bytes e opcode desconhecido podem resultar em `null`; pacotes concretos podem propagar exceções de leitura. `null` não distingue todos esses casos, e não há encapsulamento geral de exceções de desserialização.

### Exemplo de composição

Para `new HeartBeat(new byte[]{0x11, 0x22})`, a mensagem SWG tem 8 bytes:

```text
01 00 | <CRC("HeartBeat") em 4 bytes LE> | 11 22
```

`NetworkProtocol.encode` acrescenta:

```text
08 00 00 00 | 01 00 | <CRC em 4 bytes LE> | 11 22
```

O CRC simbólico evita inventar um valor calculado que não foi executado nesta análise. Fonte do corpo: `J/network/packets/swg/zone/HeartBeat.java:33–63`.

## Baselines e deltas: envelope de replicação

Estas classes transportam dados de replicação. Elas não implementam o estado completo de cada objeto nem definem o significado de todos os índices de variável. Nesta árvore, `Baseline.encodeBaseline()` retorna um buffer vazio por padrão; a obtenção do conteúdo de cada classe/view precisa ser investigada no consumidor da biblioteca.

### Baseline

Fonte: `J/network/packets/swg/zone/baselines/Baseline.java:34–97`.

| Offset no pacote SWG | Tamanho | Campo escrito |
| --- | --- | --- |
| 0 | 2 | Valor `5`, LE |
| 2 | 4 | CRC de `BaselinesMessage`, LE |
| 6 | 8 | ID do objeto, LE |
| 14 | 4 | Tipo textual invertido: `CREO` → bytes `OERC` |
| 18 | 1 | Número da baseline/view |
| 19 | 4 | Comprimento do bloco seguinte: `baseData.length + 2`, LE |
| 23 | 2 | `opCount`, ou `5` quando seu valor é zero, LE |
| 25 | variável | `baseData` |

A enumeração inclui `CREO`, `PLAY`, `TANO`, `SHIP`, `WAYP`, `WEAO` e outras classes de objeto. A enumeração documenta relações de herança nos comentários, mas não aplica essa herança à serialização.

**Assimetria:** ao decodificar, `baseData = getArrayLarge()` inclui o short `opCount`; o código lê esse short de um wrapper separado, sem removê-lo de `baseData`. Ao serializar novamente, acrescenta um novo short antes de todo esse array (`Baseline.java:62–86`). Portanto, o percurso decode → encode não é uma cópia byte a byte: o contador pode aparecer duplicado e o comprimento aumenta em 2. O construtor que recebe outra `Baseline`, por outro lado, obtém somente `encodeBaseline().array()`. Esses dois modos não têm o mesmo contrato interno para `baseData`.

Exemplo simbólico dessa assimetria, considerando apenas o bloco com comprimento: uma entrada `04 00 00 00 | 05 00 AA BB` deixa `baseData={05,00,AA,BB}` e `opCount=5`. O `encode()` seguinte escreve `06 00 00 00 | 05 00 05 00 AA BB`. Isso é uma derivação das atribuições e escritas da fonte, sem execução de round-trip. Se o contador recebido for zero, o novo contador externo ainda é substituído por `5`, pela expressão condicional do encoder.

### Delta

Fonte: `J/network/packets/swg/zone/deltas/DeltasMessage.java:41–105`.

O prefixo até o offset 18 segue a mesma disposição da Baseline, com CRC de `DeltasMessage`. A partir do offset 19:

| Offset | Tamanho | Campo escrito |
| --- | --- | --- |
| 19 | 4 | `deltaData.length + 4`, LE |
| 23 | 2 | Quantidade de atualizações: constante `1`, LE |
| 25 | 2 | Índice `update`, LE |
| 27 | variável | Dados da atualização |

`decode` ignora a quantidade de atualizações e lê somente um índice; o restante do bloco vira `deltaData`. Logo, esta classe modela diretamente uma atualização por mensagem. Uma mensagem com vários pares índice/payload não é convertida em lista de atualizações. O índice é lido como short com sinal; a API o expõe como int.

Por exemplo, para `type=CREO`, `num=3`, `update=7`, `deltaData={01,02}`, a parte após o ID do objeto será:

```text
4F 45 52 43 | 03 | 06 00 00 00 | 01 00 | 07 00 | 01 02
    OERC      view   tamanho     count   índice    dados
```

O exemplo descreve o envelope; não atribui significado de gameplay ao índice 7.

## Object Controller Messages (OCM)

`ObjectController` usa opcode SWG externo `0x80CE5E46`, seguido de um identificador interno que o código chama `controllerCrc`. Muitos valores internos são pequenos códigos numéricos, não um CRC calculado do nome da classe. O cabeçalho completo ocupa 26 bytes (`ObjectController.java:47–85`):

| Offset | Tamanho | Campo |
| --- | --- | --- |
| 0 | 2 | `5`, LE |
| 2 | 4 | `0x80CE5E46`, LE: `46 5E CE 80` |
| 6 | 4 | `update`, LE; construtor padrão usa `0x1B` |
| 10 | 4 | Identificador interno/controller, LE |
| 14 | 8 | ID do objeto, LE |
| 22 | 4 | Campo escrito como zero; ignorado ao ler |
| 26 | variável | Corpo específico |

`decodeController` lê o identificador no deslocamento 10 e escolhe a classe concreta. Exemplos registrados: movimento `0x0071`, movimento com parent `0x00F1`, fila de comandos enqueue `0x0116`, dequeue `0x0117`, postura `0x0131`, menu de objeto `0x0146/0x0147`, comandos de missão, conversa com NPC, buffs, quests e chat espacial (`ObjectController.java:106–158`). A checagem preliminar só exige array de 14 bytes; os 26 bytes do cabeçalho e o corpo continuam sujeitos a falhas posteriores de leitura.

Para ID desconhecido, o retorno é `GenericObjectController`. Ele preserva os campos do cabeçalho lidos, mas não armazena o corpo desconhecido. Seu `encode()` gera somente os 26 bytes do cabeçalho (`ObjectController.java:161–180`). Ferramentas de captura/replay devem guardar os bytes originais, em vez de reserializar esse fallback.

`decodeHeader` registra divergência do controller interno e continua; o método retorna `void`. Falha no opcode externo faz apenas o próprio helper retornar; um `decode` de subclasse pode continuar lendo campos em seguida. Isso não equivale a rejeição transacional da mensagem.

### Exemplo: enqueue de comando

`CommandQueueEnqueue` acrescenta ao cabeçalho OCM, na ordem:

```text
counter:int32 LE
commandCrc:int32 LE
targetId:int64 LE
arguments: string Unicode (int32 de unidades UTF-16 + UTF-16LE)
```

O controller interno é `0x0116`. O pacote ocupa `46 + 2 × arguments.length` bytes; com argumento `"A"`, são 48 bytes antes do prefixo opcional de `NetworkProtocol`. O opcode externo identifica OCM, o código interno identifica enqueue, e `commandCrc` identifica o comando solicitado: são três níveis diferentes. Fonte: `J/network/packets/swg/zone/object_controller/CommandQueueEnqueue.java:32–69`.

## Fluxos de captura HCAP

HCAP é um formato de armazenamento independente dos cabeçalhos SWG. `HcapOutputStream` escreve versão `3`, quantidade de metadados em um byte e pares `chave=valor` usando `DataOutputStream.writeUTF` (UTF modificado de Java, com prefixo próprio). Os metadados incluem SO, arquitetura, Java, timezone e instante da criação (`HcapOutputStream.java:46–92`).

Cada registro de versão 3 contém:

```text
server:boolean (1 byte)
epochMillis:int64 big-endian
dataLength:uint16 big-endian
data: bytes originais
```

Os inteiros aqui seguem `DataOutputStream`, não o little-endian de `NetBuffer`. `HcapInputStream` lê tamanho unsigned short em versões menores que 4 e int em versões 4 ou maiores; o writer desta árvore permanece na versão 3 (`HcapInputStream.java:76–92`). Não atribua automaticamente significado cliente → servidor ao boolean sem verificar quem constrói `PacketRecord` no consumidor.

Limitações observáveis: o writer usa `writeShort(data.length)` sem limitar o array a 65535 bytes; o reader usa `available() >= 11` para decidir se há registro e não implementa um leitor bloqueante geral de rede; a versão 4 precisaria de 13 bytes de cabeçalho. A API retorna `null` quando não consegue completar um payload. Versões futuras não são explicitamente rejeitadas.

## Buffer incremental e sockets TLS

`NetBufferStream` expande a capacidade multiplicando-a por 4 e fornece leitura via cursor, `mark/rewind` e `compact`. `reset()` volta a 1024 bytes mesmo quando o construtor recebeu outra capacidade (`J/network/NetBufferStream.java:94–104`, `:453`). Há duas formas de escrita com comportamentos distintos: `write(byte[])` copia no índice `size` sem avançar o cursor de `NetBuffer`, enquanto `addInt/addAscii/...` escrevem na posição do cursor e incrementam `size` (`:106–135`, `:300–442`). Misturá-las exige cuidado: os pontos de escrita podem divergir. `addAscii` também contabiliza e reserva por caracteres, embora `NetBuffer` escreva UTF-8 em bytes (`:321`).

`SecureSocketFactory.load` carrega um keystore JKS, configura key/trust managers `SunX509` com o mesmo keystore e cria um `SSLContext("TLSv1.2")`. Só então marca `isLoaded=true`. `createSocket()` sem argumentos verifica esse estado, mas os demais overloads delegam diretamente para a fábrica ainda potencialmente nula. `createSocketImpl()` retorna `null`; implementar a interface não o torna um provedor completo de `SocketImpl` (`J/network/SecureSocketFactory.java:53–166`). Estas observações descrevem a API existente e não validam configuração TLS em produção.

## Cobertura e próximos pontos de verificação

A busca em `pswgcommon/src/test` não encontrou testes com caminho de `network` ou `encoding` nesta revisão. Isso não exclui testes indiretos, validação em outros repositórios ou capturas externas. Nenhum round-trip, conexão real ou teste de cliente foi executado para produzir esta página.

Para ampliar a garantia de comportamento, os casos mais informativos são: envelopes incompletos com 1–4 bytes faltantes; UTF-8 multibyte nos três caminhos `Encoder`/`NetBuffer`/`NetBufferStream`; floats logo após campos big-endian; comprimentos de array nas fronteiras 32767/32768; Baseline decode → encode; delta com múltiplas atualizações; OCM desconhecido com payload; HCAP com registro grande e leitura parcial. Esses casos decorrem das assimetrias concretas acima, e não de uma suposição de que todo pacote tenha codec simétrico.

