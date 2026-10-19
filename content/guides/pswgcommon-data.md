---
title: "PSWGCommon: dados, serialização e persistência"
section: guides
category: "PSWGCommon"
slug: pswgcommon-data
layout: guide
date_audited: 2026-10-19
---

# PSWGCommon: dados, serialização e persistência

Esta página descreve o código Java/Kotlin presente em `pswgcommon`, por inspeção estática. Os layouts abaixo representam o comportamento da implementação local; não constituem confirmação de compatibilidade com todas as versões do cliente SWG. Não foram executados a biblioteca nem seus testes para esta análise.

Os caminhos de evidência são relativos à raiz `pswgcommon/src/main/java/com/projectswg/common/`. As linhas indicadas correspondem à revisão local analisada em 19/10/2026. Leitores IFF e arquivos do jogo têm escopo separado.

## Dois contratos para o mesmo objeto

`Encodable` representa bytes de protocolo, enquanto `MongoPersistable` representa campos de documento. Um objeto pode implementar ambos, mas os formatos não precisam conter os mesmos dados. `Location`, por exemplo, envia apenas orientação e posição; seu documento também pode conter terreno. `Mail` envia corpo, assunto e anexos OOB; seu documento armazena também remetente, destinatário, identificação, estado e data.

`NetBuffer` fornece as primitivas usadas nos layouts: inteiros e floats comuns são little-endian; os métodos `addNet*` usam big-endian; boolean ocupa um byte; o método chamado ASCII usa UTF-8 com prefixo de tamanho em bytes de 16 bits; Unicode tem contagem de unidades UTF-16 de 32 bits e corpo UTF-16LE; listas comuns começam com contagem de 32 bits. `addEncodable` acrescenta o objeto, sem um envelope universal de tipo ou tamanho. Evidência: `network/NetBuffer.kt:38–39,99–204`.

Vários objetos calculam `length` somando `String.length` aos campos chamados ASCII. Para caracteres multibyte em UTF-8, esse cálculo pode reservar menos bytes que o encoder precisa. Os layouts abaixo usam a nomenclatura do código, mas não implicam suporte irrestrito a nomes não ASCII.

Na tabela, `ascii` e `unicode` incluem seus prefixos, `list<T>` inclui a contagem, `i32/i64` indicam largura de armazenamento e `f32` é float de 32 bits. A assinatura Java/Kotlin pode usar tipos com sinal mesmo quando um campo de protocolo funciona como identificador ou máscara.

| Objeto | Ordem escrita no protocolo | Evidência |
| --- | --- | --- |
| `CRC` | `i32 crc` | `data/CRC.java:104–120` |
| `Point3D` | `f32 x, y, z` (12 bytes) | `data/location/Point3D.java:171–190` |
| `Quaternion` | `f32 x, y, z, w` (16 bytes) | `data/location/Quaternion.java:208–230` |
| `Location` | `Quaternion`, `Point3D` (28 bytes), sem terreno | `data/location/Location.java:204–224` |
| `ChatAvatar` | `ascii "SWG"`, `ascii galaxy`, `ascii name` | `data/encodables/chat/ChatAvatar.kt:44–60` |
| `ChatRoom` | `i32 id`, `i32 type`, boolean moderated, ASCII path, owner, creator, Unicode title, lista de moderators, lista de invited | `data/encodables/chat/ChatRoom.kt:173–204` |
| `StringId` | `ascii file`, `i32 0`, `ascii key` | `data/encodables/oob/StringId.kt:57–73` |
| `ProsePackage` | base `StringId`, actor, target, other, `i32 di`, `f32 df`, boolean grammarFlag | `data/encodables/oob/ProsePackage.kt:192–217` |
| `ProsePackage.Prose` | `i64 objectId`, `StringId`, Unicode text | `data/encodables/oob/ProsePackage.kt:283–299` |
| `WaypointPackage` | `i32 0`, Point3D, `i64 cellId`, `i32 terrain.crc`, Unicode name, `i64 objectId`, byte color, boolean active | `data/encodables/oob/waypoint/WaypointPackage.kt:61–87` |
| `Mail` | Unicode message, Unicode subject, `OutOfBandPackage` | `data/encodables/player/Mail.kt:50–66` |
| `SkillMod` | `i32 base`, `i32 modifier` (total lógico = base + modifier) | `data/encodables/tangible/SkillMod.kt:34–64` |
| `MapLocation` | `i64 id`, Unicode name, `f32 x`, `f32 y`, byte category, byte subcategory, boolean active | `data/encodables/map/MapLocation.kt:124–148` |
| `GcwGroup` / `GcwRegion` | ASCII planetName, lista de zones | `data/encodables/gcw/GcwGroup.kt:32–52`, `GcwRegion.kt:32–52` |
| `GcwGroupZone` | ASCII name, `i32 weight` | `data/encodables/gcw/GcwGroupZone.kt:32–48` |
| `GcwRegionZone` | ASCII name, `f32 x, z, radius` | `data/encodables/gcw/GcwRegionZone.kt:32–52` |

## CRC e resolução de nomes

`CRC.getCrc(String)` converte diretamente para UTF-8: não transforma caixa, barras ou nomes de arquivo. O algoritmo começa em `0xFFFFFFFF`, percorre os bytes pela tabela cujo polinômio é `0x04C11DB7`, desloca à esquerda e complementa o resultado. Isso é a rotina de identificação de nomes desta classe; não se deve substituir automaticamente pelo CRC de transporte SOE. Evidência: `data/CRC.java:39–72,152–161`.

O objeto pode nascer de texto ou do inteiro CRC. A recuperação de texto consulta um singleton carregado do recurso `data/crc_database.csv`; um CRC ausente retorna `null`. O banco é um dicionário conhecido, não uma inversão matemática do hash. `addCrc` substitui qualquer entrada com o mesmo valor; igualdade e hash de `CRC` usam exclusivamente o inteiro. O documento persiste somente `crc`, e a leitura tenta resolver o nome novamente. Evidência: `data/CrcDatabase.java:44–86` e `data/CRC.java:77–100,123–149`.

`Terrain` é uma enumeração de caminhos `terrain/*.trn`, mas calcula o CRC do nome sem prefixo e extensão. Uma consulta desconhecida por CRC retorna `null`, apesar de um comentário mencionar Tatooine como padrão. Evidência: `data/location/Terrain.java:106–121,154–170`.

## Posição, orientação e terreno

Os objetos geométricos mantêm coordenadas em `double`, mas enviam `float`, reduzindo a precisão no wire. `Point3D` oferece distâncias completas e planas; o plano horizontal usa X/Z. `Location` reúne ponto, quaternion e terreno e oferece um builder para posição, heading e transformações relativas. Seu documento guarda ponto e orientação como subdocumentos com doubles. Evidência: `data/location/Point3D.java:94–168,171–205`, `Location.java:98–152,227–239,375–478`.

Os contratos de proximidade não são intercambiáveis: `isWithinDistance(Location, radius)` verifica terreno, enquanto `isWithinFlatDistance(Location, radius)` encaminha somente o ponto. `getHeadingTo(Location)` e `getHeadingTo(Point3D)` também usam fórmulas com sentidos diferentes. `LocationBuilder.build()` passa suas referências de ponto e orientação ao novo objeto; continuar alterando o mesmo builder pode alterar uma Location já construída. Evidência: `Location.java:111–152,69–73,476–478`. Ao integrar movimento, escolha explicitamente o método e evite reutilizar o builder como se produzisse cópias independentes.

## Aparência e CustomizationString

`CustomizationString` mantém nomes de variáveis em um `LinkedHashMap` sincronizado, preservando ordem de inserção. Os IDs vêm do recurso `data/customization/customization_variables.sdb`. No Mongo, os nomes e valores são salvos no campo `variables`, por `putMap`; esse formato não é a string compactada de rede. Evidência: `data/customization/CustomizationString.kt:45–65,263–284`.

Na rede, `encode()` escreve um array com comprimento de 16 bits. Seu conteúdo é versão `2`, quantidade de variáveis, pares ID/valor e terminador lógico `FF 03`. Cada byte lógico é transformado em um caractere UTF-8 de um ou dois bytes; antes disso, `00` vira `FF 01` e `FF` vira `FF 02`. Portanto, o terminador físico UTF-8 é `C3 BF 03`. Valores entre 0 e 255 usam um byte lógico. Demais valores marcam o bit `0x80` do ID e enviam os dois bytes inferiores em ordem little-endian. Uma personalização vazia retorna apenas dois bytes zero. Evidência: `CustomizationString.kt:94–154,179–254`.

O chamador precisa retirar o prefixo de array antes de chamar `decode`: esse método lê `data.array` desde o início como conteúdo da personalização, não consome um comprimento externo. O teste `src/test/java/com/projectswg/common/data/customization/TestCustomizationString.kt` documenta esse padrão e casos de round-trip; sua existência não comprova execução nesta análise.

Há limites concretos a considerar ao reutilizar o parser:

- `decode()` não limpa as variáveis já presentes e não valida versão ou terminador. Um objeto reutilizado pode conservar campos antigos.
- O leitor assume UTF-8 com no máximo dois bytes e não faz verificações explícitas de truncamento.
- O ramo de dois bytes força `0xFFFF0000` no valor reconstruído. Assim, a implementação também codifica valores positivos maiores que 255, mas os decodifica como negativos; não há round-trip geral para esse intervalo.
- Nomes inválidos são protegidos por `assert` em `put`, enquanto `encode()` usa `!!` na resolução do ID. Não se deve depender de assertions desativáveis para validar dados externos.
- `length` calcula uma estrutura completa mesmo para uma instância vazia, enquanto `encode()` retorna apenas dois bytes. Chamadores que reservam espaço com base em `length` precisam conhecer essa diferença.

Essas observações derivam de `CustomizationString.kt:62–65,94–154,157–196,231–254`; não são falhas reproduzidas em execução.

## Texto localizado, prose e anexos OOB

`StringId` modela uma referência `@arquivo:chave`; não carrega nem traduz o STF. O construtor de argumento único exige `:` e remove `@` inicial quando presente. `ProsePackage` combina uma referência base com três substituições (`TU`, `TT`, `TO`), inteiro decimal (`DI`), float decimal (`DF`) e flag gramatical. Cada substituição pode transportar identificação de objeto, outro StringId e texto Unicode. Evidência: `data/encodables/oob/StringId.kt:32–55` e `ProsePackage.kt:36–190,261–311`.

`OutOfBandPackage` envolve esses objetos em um campo tratado como string Unicode pelo cliente: começa com `(comprimento total - 4) / 2` em 32 bits. Cada registro contém `short paddingSize`, byte de tipo, inteiro de posição, bytes do objeto e padding zero para alinhamento par. Os tipos implementados no despacho são `PROSE_PACKAGE=1`, `WAYPOINT=4` e `STRING_ID=5`, embora a enumeração declare mais valores. A posição emitida é `-1` para StringId/prose e `-3` para waypoint. O modo conversation acrescenta um short zero antes dos registros. Evidência: `OutOfBandPackage.kt:46–87,100–174` e propriedades `oobPosition` das classes concretas.

Persistência OOB usa uma lista de documentos `packages`; a fábrica inclui `oobType` como nome textual da enumeração e escolhe a classe na leitura. `isConversation` não é persistido. Tipos não reconhecidos causam exceção na fábrica Mongo; no parser de rede são registrados em log e não existe um comprimento completo de registro que permita ignorar com segurança um payload arbitrário. `decode()` também não limpa a lista existente. Evidência: `OutOfBandPackage.kt:64–75,91–123` e `OutOfBandFactory.kt:33–55`.

Uma assimetria merece investigação antes de usar prose como formato de ida e volta: `encode` escreve `df` por `addFloat`, mas `decode` lê `data.int.toFloat()`, convertendo o inteiro numericamente em vez de reinterpretar seus bits IEEE-754. Evidência: `ProsePackage.kt:200,211`.

## Chat, correio e SUI

`ChatAvatar` emite a galáxia global definida por `setGalaxy`. Ao decodificar, descarta jogo e galáxia recebidos e converte o nome para minúsculas; igualdade considera apenas nome. Isso pressupõe um contexto de galáxia externo ao objeto. `ChatRoom` mantém membros, convidados, moderadores e banidos em conjuntos concorrentes e guarda uma codificação em cache. O wire da sala contém convidados e moderadores, mas não membros e banidos. Evidência: `data/encodables/chat/ChatAvatar.kt:34–88`, `ChatRoom.kt:36–42,173–204`.

As verificações de sala são auxiliares: `canJoinRoom` examina banimento, associação prévia, acesso público e convite; `canSendMessage` examina banimento e moderação, mas não exige presença em members. O servidor consumidor deve aplicar as demais regras. A moderação de envio consulta o conjunto moderators diretamente, enquanto `isModerator` também reconhece owner. Alterar internamente um `ChatAvatar` já inserido num conjunto ou referenciado por uma sala pode afetar hash e cache sem passar pelos setters da sala. Evidência: `ChatRoom.kt:99–125` e setters/métodos de mutação no mesmo arquivo.

`Mail.encode()` é o conteúdo de uma mensagem; não equivale ao documento completo de correio nem ao pacote de entrega. Há uma codificação separada de cabeçalho. Evidência: `data/encodables/player/Mail.kt:50–89,112`.

`SuiBaseWindow` acumula comandos para manipular widgets e registrar assinaturas de eventos. Cada `SuiComponent` emite byte de tipo, lista de parâmetros Unicode e lista de parâmetros ASCII; o alvo é o primeiro parâmetro ASCII. Callback é um nome enviado ao cliente e uma referência `ISuiCallback` guardada localmente no mapa da janela. O callback Java/Kotlin não é serializado. Evidência: `data/sui/SuiComponent.kt:34–46,116–164` e `SuiBaseWindow.kt:154–209`.

A janela escreve ID, script ASCII, lista de componentes, objeto de alcance, distância máxima, long zero e int zero. O decoder para após distância máxima e deixa os 12 bytes finais sem consumir; o significado desses campos não está estabelecido. Embora o encoder tolere script nulo, `length` usa `suiScript!!`, exigindo inicialização prévia. Evidência: `SuiBaseWindow.kt:211–243`.

## Persistência MongoData

`MongoData` envolve `org.bson.Document`, sem abrir conexão com MongoDB. `MongoPersistable` exige somente leitura e escrita de campos. `_ver` é opcional no construtor; não há migração automática. `toDocument` faz uma cópia superficial. `getDocument(key)` cria e insere um documento vazio se a chave estiver ausente; a leitura pode, portanto, modificar o documento. Evidência: `data/encodables/mongo/MongoData.kt:38–72,172–180`.

Maps são gravados como arrays de documentos `{key: ..., val: ...}`, permitindo chaves que não sejam strings. Objetos persistíveis são convertidos recursivamente em documentos. Na leitura por classe, a implementação procura construtor público `MongoData` ou construtor vazio e chama `readMongo`; também aceita fábricas explícitas. Evidência: `MongoData.kt:228–290,410–500`.

Cuidados de integração extraídos do código:

- Os getters tipados dependem do tipo BSON esperado; defaults resolvem ausência, não todos os conflitos de tipo.
- `putFloat` armazena Double, mas a conversão genérica de coleções trata Float separadamente. Evite presumir representação idêntica entre caminhos de inserção.
- `putArray(LongArray)` usa `listOf(array)`, produzindo uma lista com o array como elemento, diferente de `IntArray`, que é expandido em números individuais.
- Muitos métodos `put*` usam assertions para impedir duplicação de chave; `put` e `putAll` genéricos são explicitamente proibidos.

Evidência: `MongoData.kt:75–116,293–358,482–500,525–537`.

## Configuração e utilitários de suporte

`Config` exige arquivo já existente, carrega-o e o salva imediatamente. Consultar chave ausente com default chama `setProperty`, que salva o arquivo. O parser aceita `chave=valor`, corta conteúdo a partir de `#`, separa no primeiro `=` e não remove espaços. O save reescreve tudo em UTF-8, ordena chaves e substitui comentários por um cabeçalho de data. `load()` sobrepõe valores no mapa existente sem removê-los: apagar uma chave do arquivo não a elimina automaticamente da instância carregada. Evidência: `data/info/Config.java:51–78,126–179`, `ConfigData.java:80–153`.

Os pacotes `data/combat`, `data/objects`, `data/radial` e `data/encodables/tangible` também centralizam códigos, flags e enums compartilhados. `data/schematic/DraftSchematic.java` é um modelo mutável de crafting, com ingredientes e atributos, sem implementar diretamente os contratos wire/Mongo. Os tipos em `data/math/extents` são modelos geométricos; interpretar sua finalidade requer os leitores IFF que os constroem.

Outros pontos de entrada úteis são `utilities/ByteUtilities.java` (hex e conversões), `TimeUtilities.java` (datas), `LocalUtilities.java` (diretórios por aplicação), `ThreadUtilities.java` (fábrica de threads) e `process/JarProcessBuilder.java` (montagem de comando Java, memória e redirecionamento). `network/SecureSocketFactory.java` carrega JKS e inicializa TLSv1.2; seus métodos de socket dependem de `load()` anterior. Isso é independente do transporte UDP SOE.

## HCAP: captura persistida de pacotes

`network/hcap/HcapOutputStream.java` escreve versão `3`, um byte de contagem de propriedades do sistema, pares `key=value` via `DataOutputStream.writeUTF`, e registros com boolean de direção, timestamp epoch-millis de 64 bits, tamanho de 16 bits e dados. Os inteiros de `DataOutputStream` são big-endian, ao contrário das primitivas comuns de `NetBuffer`. `HcapInputStream.java` lê tamanho unsigned de 16 bits nas versões anteriores a 4 e int de 32 bits nas seguintes. Esse suporte de leitura não significa que o writer local produza v4.

O writer não verifica se um pacote cabe no campo de 16 bits, e o reader usa `available()` para decidir se existe cabeçalho suficiente. Isso funciona como uma convenção de arquivo/captura local, mas não estabelece um parser robusto para qualquer stream incremental. A interpretação dos bytes capturados depende da camada que entregou `PacketRecord`, e não apenas da extensão HCAP. Evidência: `network/hcap/HcapOutputStream.java:49–50,66–91`; `HcapInputStream.java:76–104`.

## Limite da evidência

As assimetrias listadas são observáveis no fonte, mas sua ocorrência em produção depende de dados e consumidores. Nenhuma delas foi tratada aqui como comportamento comprovado do executável original ou como resultado obtido pelo Binary Ninja. Para confirmar compatibilidade, o próximo passo é comparar amostras de rede e round-trips dos objetos com a versão exata do cliente, incluindo entradas vazias, truncadas e valores extremos.
