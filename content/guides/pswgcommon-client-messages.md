---
title: "PSWGCommon: três mensagens comparadas com o cliente"
---

# PSWGCommon: três mensagens comparadas com o cliente

Esta etapa confronta `UpdateContainmentMessage`, `SceneCreateObjectByCrc` e `ChatInstantMessageToClient` da revisão `9ab4234e94be480f3b48f539a1f0dd6f5bd408a4` de PSWGCommon com leitores e escritores do cliente `SWGEmu.exe`. O Binary Ninja foi usado diretamente pelo MCP, seguindo o método de coleta e delimitação de evidências da skill REA. O REA CLI não foi usado como motor de decompilação nesta etapa.

O alvo é o PE x86 de SHA-256 `58012e57cebc499454812ba7ed96b1289db01e520963b4fc364edb41c322b2a8`. Todas as observações são estáticas. Não houve execução da biblioteca, execução do cliente ou captura de tráfego. Os layouts são de mensagens SWG a partir do contador inicial; não incluem enquadramento SOE, compressão, criptografia ou o prefixo próprio de `NetworkProtocol`.

## Resultado da comparação

| Mensagem | Resultado estrutural | Diferença ou limite |
| --- | --- | --- |
| [UpdateContainmentMessage](../protocols/UpdateContainmentMessage.md) | Dois NetworkIds de 64 bits e um inteiro de 32 bits; 26 bytes com cabeçalho | `slotIndex` na biblioteca corresponde ao campo chamado Arrangement Id na documentação; significado de cada valor não foi demonstrado pelo codec |
| [SceneCreateObjectByCrc](../protocols/SceneCreateObjectByCrc.md) | NetworkId, transform de 28 bytes, CRC de template e boolean; 47 bytes | O cliente mantém matriz 3×4 em memória e quaternion/posição na rede; semântica completa de ByteFlag permanece parcial |
| [ChatInstantMessageToClient](../protocols/ChatInstantMessageToClient.md) | Avatar de três strings de bytes, mensagem Unicode e outra string Unicode | O `INT 0` final da página histórica era apenas o caso vazio dessa segunda string; biblioteca escreve contador `2`, mas serializador nativo produz `4` |

Os CRCs de nome calculados independentemente por algoritmo bit a bit são `56CBDE9E`, `FE89DDEA` e `3C565CED`, respectivamente. Eles coincidem com os valores documentados. Esse cálculo não é o CRC de transporte SOE e não implica equivalência integral entre clientes NGE e o executável deste workspace.

## Como os alvos foram identificados

O [localizador reproduzível](../../scripts/locate_pswgcommon_messages.py) procura RTTI exato, candidatos a CompleteObjectLocator, vtables e ocorrências de seus endereços nos bytes das seções executáveis. Ocorrências brutas são apenas candidatas. Os construtores selecionados foram então lidos pelo Binary Ninja: eles referenciam o nome da mensagem, instalam as vtables e registram as variáveis antes de chamar o desempacotador. O [resultado do localizador](../../data/pswgcommon-evidence/messages-01/locator.json) preserva também candidatos que não foram seguidos.

| Mensagem | Type descriptor | Vtables principal / base +0x10 | Construtor com valores / leitor |
| --- | --- | --- | --- |
| Contenção | `0x18b0b38` | `0x15eb2d4` / `0x15eb2cc` | `0xadc560` / `0xadc6d0` |
| Criação por CRC | `0x18b0474` | `0x15eafe8` / `0x15eafe0` | `0xad4fb0` / `0xad51b0` |
| Chat para cliente | `0x18b1e20` | `0x15eba3c` / `0x15eba34` | `0xaf2410` / `0xaf2610` |

Os nomes `sub_*` e algumas assinaturas de funções são aproximações do decompilador. A interpretação abaixo foi apoiada por ordem de registro, RTTI dos AutoVariables, rotinas de leitura/escrita e, quando necessário, instruções x86. Offset de membro C++ não equivale a offset no pacote.

## Contador e ordem de variáveis em Archive

O construtor base em `0xacb270` registra o opcode como `AutoVariable<unsigned long>` em `this+0x30`, com valor em `+0x34`. Os construtores concretos acrescentam suas variáveis usando `0x118b5f0`, que as insere em ordem em um vetor. A expressão `arg1[n]` nos exports usa ponteiro de 32 bits; por isso, `arg1[0xe]` significa offset de bytes `+0x38`.

`0x118b6f0` calcula `(fim - início) / 4` para esse vetor, escreve os dois bytes baixos do resultado e chama o método virtual de escrita de cada variável. Logo, o contador é **quantidade de variáveis registradas incluindo o opcode**, não quantidade de todos os campos escalares de uma estrutura composta.

O leitor `0x118b740` lê dois bytes iniciais em uma variável temporária e percorre o vetor chamando os métodos virtuais de leitura. Nessa função, o valor recebido do contador não controla o laço e não é comparado com a quantidade registrada. Isso explica como `4` pode representar opcode + avatar + duas strings, embora o avatar contenha três strings internas. Não demonstra aceitação de um pacote malformado por todas as camadas do cliente.

Evidências: [BASE-CONSTRUCTOR](../../data/pswgcommon-evidence/messages-01/BN-PSWG-BASE-CONSTRUCTOR.json), [ARCHIVE-REGISTER](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ARCHIVE-REGISTER.json), [ARCHIVE-PACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ARCHIVE-PACK.json) e [ARCHIVE-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ARCHIVE-UNPACK.json).

## UpdateContainmentMessage

O leitor registra em ordem AutoVariable de NetworkId em `+0x38`, outro em `+0x48` e int em `+0x58`. Os NetworkIds guardam seus oito bytes em `+0x40` e `+0x50`; o inteiro fica em `+0x5c`. O leitor virtual de NetworkId chega a `0xaa57f0`, que solicita oito bytes; o de int solicita quatro.

| Offset no wire | Bytes | Campo | Confirmação |
| ---: | ---: | --- | --- |
| 0 | 2 | Contador `4` | Opcode base + três membros |
| 2 | 4 | Opcode `56CBDE9E` | CRC do nome e cabeçalho documentado |
| 6 | 8 | Object ID | Primeiro NetworkId |
| 14 | 8 | Parent/container ID | Segundo NetworkId |
| 22 | 4 | Arrangement ID / `slotIndex` | AutoVariable int |

O sample existente tem 26 bytes, opcode correto e último inteiro `-1`. O significado desse valor não foi inferido somente por vê-lo em uma amostra. Fonte PSWGCommon: `network/packets/swg/zone/UpdateContainmentMessage.java:49–63`. Evidências: [CONTAIN-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CONTAIN-READ.json), [CONTAIN-SEND](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CONTAIN-SEND.json) e [NETID-UNPACK64](../../data/pswgcommon-evidence/messages-01/BN-PSWG-NETID-UNPACK64.json).

## SceneCreateObjectByCrc e Transform

O leitor registra `NetworkId` em `+0x38`, `Transform` em `+0x48`, unsigned long em `+0x7c` e bool em `+0x84`. Os valores começam em `+0x40`, `+0x4c`, `+0x80` e `+0x88`. O transform ocupa 48 bytes de matriz em memória; isso não significa 48 bytes na rede.

| Offset no wire | Bytes | Campo |
| ---: | ---: | --- |
| 0 | 2 | Contador `5` |
| 2 | 4 | Opcode `FE89DDEA` |
| 6 | 8 | Object ID |
| 14, 18, 22, 26 | 4 cada | Quaternion `x, y, z, w` |
| 30, 34, 38 | 4 cada | Posição `x, y, z` |
| 42 | 4 | CRC do template |
| 46 | 1 | Boolean / ByteFlag |

`0x5200c0` extrai um quaternion da matriz por `0xaba340`, escreve seus três componentes vetoriais e o componente escalar, depois as três posições da matriz. São sete escritas de quatro bytes. A rotina de conversão inicializa internamente `(w,x,y,z)=(1,0,0,0)`, mas o wire emite `x,y,z,w`. `0x5201a0` lê os mesmos sete floats, reconstrói a rotação e grava posição nos offsets de matriz `+0x0c,+0x1c,+0x2c`.

O leitor testa os quatro componentes do quaternion com uma rotina de classificação de NaN e, se algum for NaN, substitui a orientação pelo quaternion identidade antes de convertê-la para matriz. A biblioteca, em contrapartida, rejeita NaN em orientação ou posição por `verifyInternals`. Não se concluiu que os dois caminhos possuem a mesma política para todos os valores inválidos, infinitos ou quaternions não unitários. Não houve teste dinâmico dessas condições.

A última variável tem RTTI bool e seu leitor consome um byte sem uma normalização visível nesse wrapper. A fonte chama o campo `hyperspace`, mas o codec, sozinho, não demonstra em quais estados ele ativa efeitos no cliente. Mantém-se o status histórico parcial da página, com o layout agora confrontado com o binário.

Fontes: `network/packets/swg/zone/SceneCreateObjectByCrc.java:54–73`, `data/location/Location.java:204–223`, `Quaternion.java:208–229` e `Point3D.java:171–189`. Evidências: [SCENE-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-SCENE-READ.json), [TRANSFORM-PACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-TRANSFORM-PACK.json), [TRANSFORM-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-TRANSFORM-UNPACK.json), [QUATERNION-FROM-TRANSFORM](../../data/pswgcommon-evidence/messages-01/BN-PSWG-QUATERNION-FROM-TRANSFORM.json), [QUATERNION-ROTATION](../../data/pswgcommon-evidence/messages-01/BN-PSWG-QUATERNION-ROTATION.json) e [FLOAT-CLASSIFY](../../data/pswgcommon-evidence/messages-01/BN-PSWG-FLOAT-CLASSIFY.json).

## ChatInstantMessageToClient: o caso vazio escondia uma string

O cliente registra três AutoVariables: `ChatAvatarId` em `+0x38`, string Unicode em `+0x60` e outra string Unicode em `+0x70`. Ambas as strings usam a mesma vtable `0x15ead30`. O avatar tem vtable `0x15eb9d0` e seu leitor `0xb1bf40` chama três vezes o leitor de strings de bytes `0x439f60`. A rotina Unicode `0x11948b0` lê um comprimento de quatro bytes e consome duas vezes esse valor em bytes.

O resultado é:

```text
u16 count=4 | u32 opcode=3C565CED
byte_string game | byte_string galaxy | byte_string character
u32 message_units | message UTF-16LE
u32 second_string_units | second_string UTF-16LE
```

A biblioteca chama a segunda string de `outOfBand`. O binário demonstra seu tipo e sua posição; o tratamento semântico do conteúdo OOB pelo consumidor não foi rastreado nesta etapa. Um `00 00 00 00` final demonstra somente comprimento zero, não que esse campo é uma constante obrigatória nem que o pacote termina sempre imediatamente após esse inteiro.

Para strings de avatar com comprimento menor que `65535`, sejam `G` e `C` os tamanhos em bytes de galaxy e character e `M` e `O` os tamanhos em unidades UTF-16 das duas strings:

| Offset decimal | Bytes | Campo |
| ---: | ---: | --- |
| 0 | 2 | Contador: `4` nativo; `2` em PSWGCommon |
| 2 | 4 | Opcode |
| 6 | 5 | `03 00 53 57 47` (`SWG`) |
| 11 | 2 + G | Galaxy |
| 13 + G | 2 + C | Character |
| 15 + G + C | 4 + 2M | Message |
| 19 + G + C + 2M | 4 + 2O | Segunda string / `outOfBand` |

Total: `23 + G + C + 2M + 2O`. A hipótese game=`SWG` é da biblioteca e do sample; o tipo nativo avatar é mais geral e contém três strings.

### Duas diferenças concretas da biblioteca

`ChatInstantMessageToClient.encode()` escreve `addShort(2)` em vez do `4` obtido da lista de variáveis nativa. A documentação conserva o valor nativo/sample `4` e registra a divergência da implementação. Tanto o `checkDecode` da biblioteca quanto o leitor Archive inspecionado consomem o contador sem validá-lo nessa camada. Isso não autoriza afirmar que todo caminho de recepção aceita qualquer valor.

Há também diferença nos limites de strings de bytes. O leitor nativo trata o tamanho inicial como unsigned short; `0xffff` sinaliza um comprimento adicional de 32 bits. O escritor de avatar `0xb1bf70` usa esse formato estendido quando o tamanho é pelo menos `65535`. A comparação `cmp ax,0xffff` seguida de `jae` foi conferida na desmontagem. `NetBuffer.array`, usado por `ascii`, lê um short Java/Kotlin com sinal e não implementa esse escape. Comprimentos de `32768..65534` e o escape `65535` não têm o mesmo contrato nos dois leitores.

Além disso, o pacote Java reserva espaço para galaxy/character com `String.length`, enquanto `addAscii` escreve bytes UTF-8. Entradas multibyte podem ultrapassar a capacidade calculada. O leitor nativo aqui demonstra strings de bytes, não seu charset para todos os contextos; não se atribuiu UTF-8 ao cliente somente a partir da biblioteca.

Fontes: `network/packets/swg/zone/chat/ChatInstantMessageToClient.java:59–78`, `network/packets/SWGPacket.java:70–77` e `network/NetBuffer.kt:209–213,248–251`. Evidências: [CHAT-READ](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CHAT-READ.json), [CHAT-SEND](../../data/pswgcommon-evidence/messages-01/BN-PSWG-CHAT-SEND.json), [AVATAR-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-AVATAR-UNPACK.json), [AVATAR-PACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-AVATAR-PACK.json), [UNICODE-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-UNICODE-UNPACK.json), [ASCII-UNPACK](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ASCII-UNPACK.json) e [desmontagem parcial do ramo de comprimento](../../data/pswgcommon-evidence/messages-01/BN-PSWG-ASCII-UNPACK-ASM.json).

## Verificação e reprodução

O [relatório de verificação](../../data/pswgcommon-evidence/messages-01/verification.json) conserva os hashes das 46 respostas MCP, o vínculo RTTI de sete vtables de tipos, nove comparações de memória com o PE original — 2093 bytes ao todo — e a leitura independente dos samples documentados. Os trechos incluem os três construtores de leitura completos, o escritor do contador e o leitor completo de transform. São exports estáticos da base existente; não se trata de um replay de execução.

O verificador também constrói uma amostra sintética com segunda string `X`, seguida de uma variante com contador `2`. Elas demonstram offsets e consumo de bytes no decodificador independente; `X` não é apresentado como conteúdo OOB semanticamente válido. Nenhuma dessas amostras é tráfego capturado ou prova de aceitação pelo cliente.

Na raiz de `swgdocs`, com o mesmo executável preservado:

```powershell
python scripts/locate_pswgcommon_messages.py
python scripts/verify_pswgcommon_messages.py
python scripts/apply_pswgcommon_message_crosscheck.py
python scripts/record_pswgcommon_messages.py
python scripts/build_pswgcommon_docs.py
python scripts/validate_pswgcommon_docs.py
```

O primeiro script encontra candidatos; o segundo verifica exports retidos e exemplos; o terceiro sincroniza notas e a correção do campo de chat; `record_pswgcommon_messages.py` registra o lote de histórico sem duplicá-lo. Os dois últimos renderizam e validam os guias. Na raiz do workspace, execute também `python scripts/update_history.py`, `python scripts/generate_protocol_data.py` e `python scripts/generate_pending_page.py` para atualizar histórico, Inspector e backlog. Para repetir a decompilação, abra a mesma base no Binary Ninja e use os endereços e parâmetros registrados nos JSON. Os resultados foram separados do [inventário lexical](pswgcommon-catalog.md), cujo cruzamento nominal continua sem implicar confirmação de payload.

## Questões que permanecem abertas

| Questão | Estado |
| --- | --- |
| Tipos, ordem e larguras dos três layouts | Confrontados estaticamente com readers/writers |
| Contador de Chat e segunda string | Divergência e tipo confirmados por registro e serialização |
| Transform e limites de strings de bytes | Diferenças de representação e limites identificadas |
| Significado de todos os arrangement IDs | Consumidor não rastreado |
| Estados exatos do flag de hyperspace | Nome da fonte; semântica de execução ainda parcial |
| Gramática e aplicação de OOB no chat | Tipo e posição confirmados; consumidor não rastreado |
| Compatibilidade completa NGE / cliente disponível | Não estabelecida |
| Testes dinâmicos e tráfego | Não executados |
