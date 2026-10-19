---
title: "PSWGCommon: evidências REA e Binary Ninja"
---

# PSWGCommon: evidências REA e Binary Ninja

A biblioteca analisada tem fontes Java/Kotlin, sem JAR compilado incluído. O alvo nativo disponível é outro artefato: `SWGEmu.exe`, aberto pela base `SWGEmu.exe.bndb`. A comparação abaixo é restrita ao cálculo de CRC de nomes e à normalização observada nesse cliente; não é uma decompilação da biblioteca JVM nem prova de equivalência entre versões do jogo.

A continuação pelo MCP do Binary Ninja está em [três mensagens comparadas com o cliente](pswgcommon-client-messages.md). Ela confronta contenção, criação de objetos e chat e registra uma diferença de contador, o tipo da segunda string de chat e o formato estendido de strings de bytes. A limitação REA descrita abaixo pertence à tentativa anterior de usar seu provedor Ghidra.

## Identidade e ferramentas

| Item | Identidade / resultado |
| --- | --- |
| Fontes | `pswgcommon` revisão `9ab4234e94be480f3b48f539a1f0dd6f5bd408a4` |
| Executável | PE x86 (`0x14c`), image base `0x400000` |
| SHA-256 do PE | `58012e57cebc499454812ba7ed96b1289db01e520963b4fc364edb41c322b2a8` |
| Binary Ninja | Base existente aberta via MCP; pseudocódigo e 1024 bytes da tabela exportados |
| REA CLI | Investigação nativa recusada pelo provedor Ghidra com `architecture_unsupported` |
| Execução | Nenhuma execução do cliente ou da biblioteca; análise estática |

O diagnóstico REA também apontou `config_drift` no registro Codex. Não se alterou configuração: a CLI instalada foi chamada diretamente. O erro de análise foi mais específico: o perfil Ghidra/REA desse host Windows aceita PE x64, e o alvo é x86. Hopper é indisponível nesse host; IDA não estava configurado. Essas respostas não significam ausência das funções no executável. Estão preservadas em [rea-doctor.json](../../data/pswgcommon-evidence/rea-doctor.json) e [rea-function.json](../../data/pswgcommon-evidence/rea-function.json).

## Caminho CRC observado

O pseudocódigo do cliente mostra:

```text
0xaa3c50 -> 0xaa3c10 (copiar ou normalizar string)
         -> 0xaa2df0 (obter string e calcular hash)
                        -> 0xaa4790 (laço CRC)

0xaa3c10, quando o flag é verdadeiro -> 0xaa2d10 (normalização)
0xaa2d10 -> 0x131d6e8 (conversão de caracteres)
```

| Evidência | Observação |
| --- | --- |
| [BN-PSWG-CRC-SET](../../data/pswgcommon-evidence/BN-PSWG-CRC-SET.json) | Encadeia cópia/normalização e cálculo |
| [BN-PSWG-CRC-COPY](../../data/pswgcommon-evidence/BN-PSWG-CRC-COPY.json) | O flag decide entre cópia literal e chamada de normalização |
| [BN-PSWG-CRC-HASH](../../data/pswgcommon-evidence/BN-PSWG-CRC-HASH.json) | Grava o resultado do hash no objeto |
| [BN-PSWG-CRC-NORMALIZE](../../data/pswgcommon-evidence/BN-PSWG-CRC-NORMALIZE.json) | Converte separadores, suprime barras repetidas/iniciais e ignora pontos enquanto está entre segmentos |
| [BN-PSWG-CRC-CHAR](../../data/pswgcommon-evidence/BN-PSWG-CRC-CHAR.json) | Um ramo converte ASCII `A..Z` para `a..z`; o outro depende de estado de locale e não foi inteiramente seguido |
| [BN-PSWG-CRC-COMPUTE](../../data/pswgcommon-evidence/BN-PSWG-CRC-COMPUTE.json) | Estado inicial `0xffffffff`, deslocamento à esquerda de oito bits, lookup em tabela e complemento final |
| [BN-PSWG-CRC-TABLE](../../data/pswgcommon-evidence/BN-PSWG-CRC-TABLE.json) | Exporta a tabela de 256 palavras em `0x15ea5d0` |

As assinaturas, nomes `sub_*` e expressões são resultados de análise do decompilador. Não devem ser lidos como código-fonte original recuperado ou como tipagem perfeita; os bytes preservados são a evidência mais direta da tabela.

## Comparação com CRC.java

O verificador lê a tabela do MCP, a tabela declarada em `data/CRC.java` e o trecho correspondente do PE original. Os **256 valores / 1024 bytes coincidem integralmente**. O SHA-256 do trecho é `0053f121cdcaf9f510a940ba891fb2bccd41487953c5a4c0048c4a3ccdec782e`. O endereço virtual é `0x15ea5d0`, RVA `0x11ea5d0` e offset no arquivo `0x11ea5d0` para este PE. Resultado reproduzível: [crc-verification.json](../../data/pswgcommon-evidence/crc-verification.json).

Essa comparação, somada ao laço de `0xaa4790`, sustenta que as duas rotinas compartilham tabela e estrutura de atualização do CRC. A conclusão não se estende automaticamente aos bytes de entrada:

- `CRC.getCrc(String)` aplica UTF-8 diretamente, sem normalizar caixa, barras ou pontos (`CRC.java:152–161`).
- O caminho nativo tem opção de normalização antes do hash. A normalização de caminhos não é uma regra universal para todos os opcodes.
- O laço C observado encerra em NUL; a implementação Java itera todos os bytes do array. Uma string contendo NUL embutido não tem contrato idêntico.
- Charset/locale e caracteres fora de ASCII exigem investigação adicional; não foram testados.

Na prática, não acrescente `lowercase()` a todo cálculo de opcode da biblioteca com base apenas nessa rotina de caminhos. Verifique o chamador e o nome literal usado por cada mensagem. O [guia de dados](pswgcommon-data.md) explica o contrato da biblioteca; o [guia histórico de CRC](swg-packet-crc.html) trata outro contexto que também deve ser distinguido do CRC de nomes.

## Reproduzir a comparação estática

Na raiz de `swgdocs`, com o clone irmão e o mesmo executável preservados:

```powershell
python scripts/verify_pswgcommon_evidence.py --source ../pswgcommon --binary ../recovered/installation/SWGEmu.exe
```

O script usa a biblioteca padrão Python, verifica as três sequências e regenera o relatório. Os arquivos de evidência estão incluídos no portal; não é necessário distribuir o executável. Nenhuma conclusão de tráfego, regra de jogo ou compatibilidade de pacote foi extraída desta verificação de CRC. Ela não gerou uma entrada no histórico; o lote 3 veio da etapa posterior de [comparação de mensagens](pswgcommon-client-messages.md).
