---
title: "Holocore: conversão de dados do cliente"
---

# Holocore: conversão de dados do cliente

Holocore separa arquivos brutos do cliente e dados prontos para o servidor. O conjunto de utilitários em src/utility lê clientdata/ e grava representações em serverdata/; loaders em runtime leem esses arquivos para instanciar objetos e tabelas. O fluxo não converte genericamente todos os assets: cada conversor implementa um escopo próprio.

## Fluxo de geração e leitura

    clientdata (IFF, datatables, STF, templates)
      -> ClientFactory / SWGParser e conversores especializados
      -> SDB e IFF preparados em serverdata
      -> loaders de dados durante a inicialização e serviços de mundo

A tarefa Gradle runClientdataConversion executa ClientdataConvertAll. Ela chama conversores em sequência; ClientdataConvertSpecific é um ponto de entrada reduzido para células de edifícios. A biblioteca pswgcommon fornece parsers e modelos compartilhados, mas seu submódulo local não foi inicializado neste checkout.

## Formato SDB observado

SdbGenerator escreve um cabeçalho de colunas separado por tabulações, uma linha vazia para indicar ausência de tipos e linhas de dados tabulares. Coleções são achatadas usando ;, mapas viram pares chave=valor separados por vírgulas, e null é gravado como string vazia. A saída é ASCII. A conversão de strings escapa tabulações e quebras de linha para sequências textuais.

Esse formato exige cuidado com valores que contenham separadores. O teste TestSdbGenerator cobre escalares, nulos, coleções e mapas, mas isso não valida todos os conversores e loaders.

## Famílias de conversão

| Família | Entrada e saída principal | Consumidor ou observação |
| --- | --- | --- |
| Datatables | IFF de tabelas para SDBs de comandos, buffs, skills, crafting, facções, criação e outros catálogos | Converters lista os destinos |
| Dados de objetos | clientdata/object/**/*.iff para objects/object_data.sdb | ObjectDataLoader converte colunas para tipos do servidor |
| Células | Layouts IFF e portais para building_cells.sdb, incluindo vizinhos JSON | BuildingCellLoader interpreta relações de célula |
| Buildouts | Tabelas de áreas/cenas para areas.sdb e objects.sdb | BuildoutLoader filtra eventos e recria objetos |
| Terreno | Lista fixa de 21 terrenos; reescreve IFF, relê para validação e copia bitmaps referenciados | Não é varredura genérica de terreno |
| Strings | Arquivos clientdata/string/en/**/*.stf para strings.sdb | Ordena arquivos e chaves; escapa newline/tab |
| Quests | Listas e tarefas IFF para SDBs agregados ou por quest | QuestLoader lê manifesto e tarefas sob demanda |

## Lacunas e inconsistências verificadas

- ConvertAppearances lista arquivos e prepara cabeçalho, mas a escrita dos registros está comentada; não faz parte da sequência principal.
- ConvertBuildingList declara três colunas e escreve oito valores por linha; também não integra a sequência principal.
- ConvertQuestLists grava quest.sdb, enquanto QuestLoader consulta questlist.msdb; o manifesto versionado conecta o fluxo atual.
- ConvertTerrain processa nomes fixos e copia apenas bitmaps referenciados.

Esses pontos delimitam o que o pipeline implementa hoje na revisão analisada. A conversão não foi executada, então não foram comparados arquivos gerados com saídas reais neste trabalho.

## Caminhos de código

O inventário de fontes mantém hashes e classificações de src/main, src/test e src/utility. As implementações chave estão em src/utility/java/com/projectswg/utility/clientdata/, src/main/java/com/projectswg/holocore/resources/support/data/server_info/loader/ e src/main/java/com/projectswg/holocore/utilities/SdbGenerator.java, na revisão pinada no [guia principal](holocore-overview.md).

## Fontes consultadas

- [ClientdataConvertAll.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/utility/java/com/projectswg/utility/ClientdataConvertAll.java)
- [Converters.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/utility/java/com/projectswg/utility/clientdata/Converters.java)
- [SdbGenerator.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/utilities/SdbGenerator.java)
- [ConvertBuildouts.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/utility/java/com/projectswg/utility/clientdata/ConvertBuildouts.java)
- [QuestLoader.kt](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/main/java/com/projectswg/holocore/resources/support/data/server_info/loader/QuestLoader.kt)
- [TestSdbGenerator.java](https://github.com/ProjectSWGCore/Holocore/blob/ff53903bbb8b0ff2edcd2493d66f940767036aaa/src/test/java/com/projectswg/holocore/utilities/TestSdbGenerator.java)

\n