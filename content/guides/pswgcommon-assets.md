---
title: "PSWGCommon: arquivos do cliente e terreno"
section: guides
category: "PSWGCommon"
slug: pswgcommon-assets
layout: guide
date_audited: 2026-10-19
---

# PSWGCommon: arquivos do cliente e terreno

Este guia descreve a implementação encontrada nas fontes de `pswgcommon`, revisão `9ab4234e94be480f3b48f539a1f0dd6f5bd408a4`. As observações abaixo resultam de leitura estática; não representam testes executados, comparação com o cliente original ou confirmação por desmontagem. A existência de um parser registrado não garante suporte integral ao formato nem preservação dos dados ao gravá-los novamente.

Nas referências, os caminhos `data/...` partem de `pswgcommon/src/main/java/com/projectswg/common/`. O número após `:` identifica a linha nessa revisão. O repositório de origem é [ProjectSWGCore/pswgcommon](https://github.com/ProjectSWGCore/pswgcommon/tree/9ab4234e94be480f3b48f539a1f0dd6f5bd408a4).

## Duas famílias de leitores

Há duas APIs paralelas para IFF. Elas possuem modelos de nós e registros de formatos diferentes; escolher uma não equivale a acessar automaticamente todos os formatos da outra.

| API | Entrada e fluxo | Resultado |
| --- | --- | --- |
| `data.swgfile` | `ClientFactory.getInfoFromFile` → `SWGFile.read` → árvore `swgfile.IffNode` → seleção pelo tag raiz → `ClientData.readIff` | Um visitante especializado, como `ObjectData`, `DatatableData` ou `WorldSnapshotData` |
| `data.swgiff` | `SWGParser.parse` → `SWGParserCache` → `IffForm.read` → seleção pelo tag → `SWGParser.read` | Um parser especializado, como `TerrainTemplate`, `PortalLayoutTemplate` ou um parser de extent |

O primeiro fluxo está em `data/swgfile/ClientFactory.java:71` e `:114`; o segundo, em `data/swgiff/parsers/SWGParser.java:24`, `SWGParserCache.java:42` e `SWGParserFactory.java:105`. `ClientData` fornece métodos vazios por padrão (`data/swgfile/ClientData.java:32`), enquanto `SWGParser` exige `read` e `write` na interface (`data/swgiff/parsers/SWGParser.java:11`). Isso não impede que uma implementação de `write` retorne `null`.

Ambas as entradas por caminho textual procuram arquivos locais em `clientdata` por padrão. A API `SWGParser` permite mudar essa base com `setBasePath`; `ClientFactory.getFolder` devolve `clientdata/`. Entradas por `File` usam o arquivo informado diretamente. Os fluxos examinados abrem arquivos com `FileChannel`; não fazem extração de arquivos `.tre` nessa etapa. Fontes: `data/swgfile/ClientFactory.java:71`, `:136`, `:213`; `data/swgiff/parsers/SWGParserFactory.java:36`, `:82`, `:96`; `data/swgiff/IffForm.java:227`.

## Estrutura IFF e ordem dos bytes

A estrutura interpretada é uma árvore de forms e chunks:

```text
FORM | tamanho BE de 32 bits | tag de quatro bytes | filhos...
chunk: tag de quatro bytes | tamanho BE de 32 bits | payload...
```

O tamanho do `FORM` inclui o tag de tipo e seus filhos, excluindo os oito bytes iniciais. A validação externa compara o tamanho do arquivo com `formSize + 8`. O payload dos chunks é normalmente lido em **little-endian**, enquanto comprimentos da estrutura usam **big-endian**. Fontes: `data/swgiff/IffForm.java:237`, `:278`, `:316`; `data/swgiff/IffChunk.java:25`; `data/swgfile/IffNode.java:272`, `:290`, `:306`.

Na API `swgiff`, um primeiro filho cujo tag é reconhecido como versão é incorporado ao form pai: a versão passa para `getVersion()` e seus filhos são promovidos. Na escrita, uma versão explícita é reconstruída como `FORM` com tag decimal de quatro posições. A API `swgfile` conserva os forms de versão como nós navegáveis. Fontes: `data/swgiff/IffForm.java:250`, `:283`; `data/swgfile/IffNode.java:184`, `:290`.

Alguns detalhes relevantes ao comparar bytes ou portar um parser:

- `IffChunk.readString()` lê até NUL e converte cada byte diretamente para `char`; `writeString()` codifica UTF-8. Texto fora de ASCII não tem uma conversão inversa garantida (`data/swgiff/IffChunk.java:101`, `:195`).
- Strings Unicode têm comprimento de 32 bits e dados UTF-16LE (`data/swgiff/IffChunk.java:93`, `:188`).
- Quaternions são lidos e escritos na ordem `w, x, y, z`, convertendo para o construtor `Quaternion(x,y,z,w)` (`data/swgiff/IffChunk.java:117`, `:209`).
- Transforms são matrizes de floats `3 × 4`; a quarta coluna fornece a posição (`data/swgiff/IffChunk.java:133`).
- Os métodos antigos `readUInt`, `readUShort` e `readULong` selecionam big-endian e devolvem tipos Java assinados. O prefixo `U` não os transforma em valores inteiros sem sinal (`data/swgfile/IffNode.java:121`).
- A API antiga considera booleano verdadeiro apenas o byte `1`; a nova considera qualquer byte diferente de zero (`data/swgfile/IffNode.java:136`; `data/swgiff/IffChunk.java:65`).

`close()` em `IffForm`/`IffChunk` marca o nó como lido. Métodos `readForm` e `readChunk` procuram nós ainda não marcados; portanto, os blocos `use` de Kotlin e `try` com recursos de Java têm também efeito no avanço lógico do parser. Não se trata de uma árvore imutável que possa ser relida indiscriminadamente. Fontes: `data/swgiff/IffForm.java:34`, `:89`, `:146`; `data/swgiff/IffChunk.java:33`.

## Formatos registrados

O registro antigo está em `data/swgfile/ClientFactory.java:160`. O registro novo está em `data/swgiff/parsers/SWGParserFactory.java:38`. A tabela resume **encaminhamento disponível**, sem afirmar cobertura completa de todas as versões.

| Família | Tags em `swgfile` | Tags em `swgiff` |
| --- | --- | --- |
| Dados gerais | `CSTB`, `DTII`, `PRFI`, `ARGD`, `0006`, `SLTD`, `WSNP`, `CIDM`, `FOOT` | `CSTB`, `PFDT`, `PRFI`, `ARGD`, `SLTD`, `FOOT`, `IDTL` |
| Aparência e renderização | `APPR`, `APT `, `CSHD`, `DTLA`, `SKTM`, `MESH`, `MLOD`, `SLOD`, `SMAT`, `SKMG`, `SSHT` | `APPR`, `APT `, `DTLA`, `MESH` |
| Portais | `PRTO` | `PRTO`, `CELL`, `PRTL` |
| Volumes/extent | Integrados aos visitantes correspondentes | `CMPT`, `CMSH`, `CPST`, `DTAL`, `EXBX`, `EXSP`, `NULL`, `XCYL`, `XOCL` |
| Terreno | Sem registro `PTAT` | `PTAT`, `LAYR`, `AHCN`, `AHFR`, `AHTR`, `AROA`, `BREC`, `BCIR`, `BPLN`, `BPOL`, `FBIT`, `FDIR`, `FFRA`, `FHGT`, `FSLP`, `FSHD` |
| Templates de objeto | Diversos tags, como `SHOT`, `STOT`, `SCOT`, `SBOT`, `SSHP`, `SWOT`, dirigidos a `ObjectData` | Sem registro equivalente no factory |

O espaço final em `APT ` faz parte do identificador de quatro bytes. Um tag desconhecido retorna `null` no factory correspondente (`data/swgfile/ClientFactory.java:152`; `data/swgiff/parsers/SWGParserFactory.java:105`). Classes auxiliares também podem ser invocadas diretamente por outros parsers sem estarem no registro geral.

### Dados tabulares, templates e snapshots

`DatatableData` interpreta `COLS`, `TYPE` e `ROWS`. As linhas são decodificadas conforme o tipo da coluna: booleano, float, inteiro/CRC/enum, string ou ausência de tipo. `DATATABLE_ENUM` é tratado como inteiro e ainda possui comentário de implementação pendente. Fontes: `data/swgfile/visitors/DatatableData.java:54`, `:145`, `:168`.

`ObjectData` interpreta forms `DERV` para carregar atributos de outro template por `ClientFactory`, mescla o mapa herdado e preserva seu tipo de baseline anteriormente determinado. Campos específicos são lidos de chunks `XXXX`. Sua lista `parsedFiles` evita reaplicar determinadas referências no mesmo objeto; isso não comprova proteção geral contra ciclos entre arquivos durante a carga recursiva. Fonte: `data/swgfile/visitors/ObjectData.java:189`, `:202`, `:209`.

`WorldSnapshotData` despacha o formato de snapshot versão 1. Cada nó versão 0 contém IDs de objeto e container, índice de template, índice de célula, quaternion, posição, raio e CRC do portal layout. Fonte: `data/swgfile/visitors/WorldSnapshotData.java:45`, `:101`, `:117`.

O leitor `.stf` é separado do IFF: verifica magic `0xABCD` e um byte de versão; na versão 1 lê valores Unicode por ID e depois associa chaves ASCII a `StringId`. A versão 0 contém apenas `assert(false)`, e versões desconhecidas lançam erro. Fontes: `data/swgfile/ClientStringParser.kt:38`, `:42`, `:62`; ordem little-endian dos inteiros em `network/NetBuffer.kt:227`.

## Cache, identidade e erros

`ClientFactory` mantém um `ConcurrentHashMap<String, ClientData>` estático. A sobrecarga textual usa a string internada como chave, guarda resultados não nulos e oferece `freeMemory()`. A sobrecarga `File` ignora esse cache. Como o carregamento ocorre antes de `putIfAbsent`, chamadas simultâneas podem analisar o mesmo arquivo mais de uma vez e devolver instâncias distintas durante a primeira carga. Fonte: `data/swgfile/ClientFactory.java:46`, `:98`, `:114`, `:136`.

`SWGParserCache` usa `ConcurrentHashMap<File, SWGParser>.computeIfAbsent`. O código não normaliza caminhos nem consulta data de modificação, não define limite de tamanho e não expõe método de limpeza. Um `File` equivalente por caminho absoluto e relativo pode gerar entradas distintas. `parse(IffForm)` passa diretamente pelo factory e não usa o cache de arquivos. Fontes: `data/swgiff/parsers/SWGParserCache.java:37`; `data/swgiff/parsers/SWGParserFactory.java:100`.

Os objetos devolvidos são compartilhados com futuros consumidores do cache, e várias classes expõem estado mutável. Alterar um parser carregado pode afetar chamadas posteriores. Trocar o diretório base não reprocessa automaticamente entradas já armazenadas sob a mesma chave `File`. Isso deriva da combinação do setter de base e do cache, sem invalidação associada (`data/swgiff/parsers/SWGParserFactory.java:82`; `data/swgiff/parsers/SWGParserCache.java:39`).

Não há um resultado de erro unificado: `ClientFactory` retorna `null` para arquivo inexistente ou `IOException`; `SWGParserCache` imprime `IOException` e retorna `null`. Erros de estrutura, buffers insuficientes e outras exceções de execução não são capturados por esses blocos. Várias validações de tags/versões usam `assert`, cujo efeito depende da configuração da JVM. Fontes: `data/swgfile/ClientFactory.java:75`; `data/swgiff/parsers/SWGParserCache.java:46`; `data/swgiff/IffForm.java:231`, `:241`.

## Motor de terreno

`TerrainTemplate` representa um terreno `PTAT`. Seu `DATA` inclui nome, largura do mapa e dos chunks, tiles por chunk, água global, ciclo de ambiente e parâmetros de distribuição de elementos colidíveis e radiais. Há tratamento específico para campos adicionais da versão 13 e para `legacyMap` nas versões a partir de 15. O comentário de suporte a todas as versões deve ser entendido como intenção do leitor; o código não valida todas as variantes possíveis. Fonte: `data/swgiff/parsers/terrain/TerrainTemplate.kt:78`.

Dentro de `TGEN`, o leitor consome sucessivamente dois forms `MGRP`, primeiro para fractais e depois para bitmaps, e carrega `LYRS/LAYR`. Cada layer contém cabeçalho de habilitação/nome, limites geométricos, filtros, modificadores de altura e sublayers. Layers desabilitados são descartados; sublayers sem modificadores de altura ou água também são descartados. Fontes: `data/swgiff/parsers/terrain/TerrainTemplate.kt:131`; `TerrainLayer.kt:16`; `TerrainListLayer.kt:43`, `:110`.

O cálculo de altitude segue estas etapas (`data/swgiff/parsers/terrain/TerrainTemplate.kt:228`, `:289`, `:325`):

1. Localiza o tile, com tamanho `chunkWidth / (2 * numberOfTilesPerChunk)`.
2. Seleciona um dos triângulos do tile pela paridade das coordenadas e pela posição local.
3. Calcula a altura de cada um dos três vértices percorrendo a árvore de layers.
4. Combina limites por máximo, filtros por mínimo e aplica inversões e feathering. O peso de uma sublayer é multiplicado pelo peso herdado.
5. Aplica modificadores de altura sequencialmente, mantendo a altura produzida pelo anterior.
6. Obtém o plano do triângulo por produto vetorial e interpola a altura no ponto consultado.

O retorno `TerrainInformation` contém altura e componentes da normal calculada por produto vetorial. O código não normaliza esse vetor. O comentário `can be cached` não implementa um cache de alturas (`TerrainTemplate.kt:228`, `:274`, `:321`).

`getTerrainHeight(x,z)` retorna o solo. `getWaterHeight(x,z)` toma o maior nível entre a água global habilitada e água local em limites poligonais/retangulares que contenham o ponto; sem água, retorna `NaN`. `getHeight(x,z)` substitui o solo por água quando ela está acima, retornando normal `(0,1,0)`. `isWater` inclui igualdade entre solo e água. A busca de água percorre os limites diretamente, sem repetir a avaliação de filtros e pesos usada no relevo. Fonte: `TerrainTemplate.kt:203`, `:212`, `:220`, `:306`.

Bitmaps são carregados relativamente à base de `SWGParser`. `BitmapFamily` converte uma falha de I/O em `bitmap = null`; `FilterBitmap` registra a falta e retorna peso `1`, comportamento que pode alterar o terreno sem interromper a carga. O filtro usa interpolação de quatro amostras e bytes convertidos para `0..255`. Fontes: `data/swgiff/parsers/terrain/bitmap/BitmapFamily.kt:13`; `filters/FilterBitmap.kt:19`.

## Limitações concretas e cuidados ao escrever

| Implementação | Comportamento observado nas fontes | Consequência |
| --- | --- | --- |
| `filters/FilterDirection.kt:14` | `process` chama `TODO("unimplemented")` | Consultar relevo que avalie esse filtro pode lançar `NotImplementedError` |
| `filters/FilterShader.kt:13`, `:27` | `process` retorna sempre `0`; `write` produz tag `FSLP` | O filtro não avalia shader; a escrita muda o identificador do formato |
| `appearance/AppearanceTemplate.java:71`, `appearance/MeshAppearanceTemplate.java:40`, `appearance/DetailAppearanceTemplate.java:92` | `write` retorna `null` | A interface comum não garante exportação desses modelos |
| `appearance/PortalLayoutTemplate.java:100`, `:131`, `:141` | `write` retorna `null`; path graph tem TODOs | Layout de portais não implica reconstrução completa de navegação |
| `footprint/FootprintDataParser.java:94` | `write` retorna `null` | A leitura de footprint não oferece gravação correspondente |
| `bitmap/TargaBitmap.kt:50` | Aceita por assert tipo TGA 2 ou 10, mas o laço lê pixels diretamente | Não há decodificação de pacotes RLE visível para tipo 10; não presumir suporte integral a TGA comprimido |
| `bitmap/TargaBitmap.kt:42`, `:55`, `:65`, `:72` | Dimensiona pelo maior lado ao quadrado; leitura e acesso variam com profundidade de cor | Variantes retangulares e coloridas precisam de validação com fixtures antes de serem consideradas compatíveis |

Os caminhos da tabela partem de `data/swgiff/parsers/terrain/` para filtros/bitmap e de `data/swgiff/parsers/` para appearance/footprint.

Há também assimetrias que merecem testes de ida e volta: `IffChunk.readVectorArgb` lê componentes na ordem `b,a,r,g`, enquanto `writeVectorArgb` grava `a,r,g,b` (`data/swgiff/IffChunk.java:125`, `:217`). `IffForm.write` usa a **posição atual** do buffer como tamanho do chunk, não seu limite: gravar uma árvore recém-lida, cujos buffers ainda estão na posição zero, pode emitir chunks vazios (`data/swgiff/IffForm.java:289`, `:303`).

O terreno é regravado como versão 14 ou 15, e layers como versão 3. Como layers desabilitados e forms desconhecidos são descartados na leitura, uma exportação não preserva necessariamente o arquivo original nem seu conteúdo de editor. Fontes: `data/swgiff/parsers/terrain/TerrainTemplate.kt:181`; `TerrainListLayer.kt:64`, `:89`, `:110`.

## O que os testes existentes cobrem

`pswgcommon/src/test/java/com/projectswg/common/data/swgiff/parsers/terrain/TestTerrainEngine.kt` contém coordenadas de referência para altura em Endor, detecção de água em Corellia, interpolação em Tatooine e casos parametrizados de vários planetas. As tolerâncias incluem `0.01`, `0.02` e `0.2` conforme o caso (`:30`, `:55`, `:128`, `:228`).

Esses testes procuram `terrain/<nome>` via `SWGParser.parse`; várias verificações encerram a função com `?: return` quando o terreno não é carregado (`:17`, `:32`, `:85`, `:229`). Assim, uma suíte aprovada sem os arquivos de cliente pode não ter exercitado essas asserções. Este guia apenas identificou essa cobertura nas fontes; não executou os testes.

Para evoluir a documentação e os parsers, as verificações mais úteis são fixtures mínimas para endian e versões, ida e volta de chunks ainda não consumidos, filtros de direção/shader, TGA RLE e coordenadas com água local. Essas são propostas de validação, não resultados já demonstrados.
