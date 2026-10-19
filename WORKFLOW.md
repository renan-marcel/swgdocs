# SWG Docs — Workflow de Engenharia Reversa e Atualização Automatizada do Histórico

Este documento estabelece o procedimento operacional padrão (SOP) para engenharia reversa de pacotes de rede do Star Wars Galaxies (SWG) e a **tarefa automatizada de atualização contínua** da página de Histórico (`history/index.html`).

## Referência de implementação PSWGCommon

A análise da biblioteca possui um [índice próprio](content/guides/pswgcommon-overview.md), com Markdown em `content/guides/pswgcommon-*.md`, HTML em `guides/pswgcommon-*.html`, inventário em `data/pswgcommon-inventory.json` e evidências em `data/pswgcommon-evidence/`.

Os scripts desta extensão ficam dentro de `swgdocs/scripts/`: `inventory_pswgcommon.py` lê o clone irmão; `build_pswgcommon_docs.py` renderiza os guias e integra busca/navegação; `validate_pswgcommon_docs.py` verifica os artefatos e links. O renderer requer `scripts/requirements-pswgcommon.txt`; as páginas prontas continuam estáticas. Após executar um gerador legado que sobrescreva índice ou busca, execute novamente `build_pswgcommon_docs.py` e o validador. As fontes Markdown PSWGCommon e seu catálogo são a entrada dessa etapa.

Correspondência nominal de mensagens, existência de um encoder ou coincidência da tabela CRC não autorizam promover um pacote a `100% Verified`. Mantenha o histórico de pacotes para desserializações efetivamente demonstradas no alvo pertinente. Limitações de provedor e afirmações por leitura de fontes devem permanecer separadas de evidência binária e de tráfego observado. A fase inicial da análise da biblioteca não gerou entradas artificiais no histórico. A continuação pelo Binary Ninja registrou três layouts demonstrados no lote 3, com o limite semântico de SceneCreateObjectByCrc preservado. O backlog de protocolos continua sem mudanças de completude nesta etapa.

## Referência de implementação Holocore

Os guias `content/guides/holocore-*.md` registram a leitura estática da revisão `ff53903bbb8b0ff2edcd2493d66f940767036aaa`, o inventário `data/holocore-inventory.json` e as pseudodescompilações Binary Ninja em `data/holocore-evidence/`. Para regenerar a documentação, use `scripts/inventory_holocore.py`, `scripts/build_holocore_docs.py` e `scripts/validate_holocore_docs.py`. O submódulo `Holocore/pswgcommon` estava desinicializado; não atribua os codecs comuns ao checkout de Holocore. REA MCP não estava registrado nesta sessão, e nenhuma configuração foi alterada.

---

## 📌 1. Visão Geral da Arquitetura

O portal de documentação mantém um registro centralizado e versionado de todas as estruturas recuperadas a partir do cliente `SWGEmu.exe`:

- **Banco de Dados Histórico:** [`data/reversal_history.json`](data/reversal_history.json)
- **Interface Web do Histórico:** [`history/index.html`](history/index.html)
- **Gerador Automatizado:** [`scripts/update_history.py`](../scripts/update_history.py)
- **Inspetor de Pacotes:** [`tools/inspector.html`](tools/inspector.html) & [`assets/js/protocol-data.js`](assets/js/protocol-data.js)
- **Tabelas Globais:** [`data/all_packets.csv`](data/all_packets.csv) e [`data/packets_summary.json`](data/packets_summary.json)

---

## ⚙️ 2. Tarefa Automatizada: Atualização do Histórico

Sempre que um novo pacote ou lote de pacotes for decodificado/revertido, a página de histórico **DEVE** ser atualizada. Para garantir isso, o processo foi automatizado em duas modalidades:

### Opção A: Execução Direta via Script Python
Após adicionar o pacote em `data/reversal_history.json`:
```bash
python scripts/update_history.py
```
O script lê `data/reversal_history.json`, recalcula a ordenação global (`#1` a `#N`), compila os metadados e regera `swgdocs/history/index.html` com layout responsivo, busca instantânea e badges de status.

### Opção B: Inclusão Programática nos Pipelines de Reversão
Nos scripts de reversão (como `scripts/apply_new_protocol_deserializations.py` ou novos geradores), a função de atualização já está acoplada:
```python
from update_history import record_packet, generate_history

# Para registrar um novo pacote programaticamente:
packet_data = {
    "name": "NomeDoPacoteMessage",
    "opcode": "1234ABCD",
    "section": "protocols",
    "section_name": "Protocols",
    "direction": "S→C",
    "category": "Space & Ship Packets",
    "url": "protocols/NomeDoPacoteMessage.html",
    "fields_count": 5,
    "unpack_address": "0x00123456",
    "vtables": ["0x015eaed0"],
    "reversal_details": "Registra membros AutoVariable...",
    "status": "100% Verified"
}

# Registra e regera a página de histórico imediatamente:
record_packet(batch_id=3, packet_info=packet_data)
```

---

## 🔬 3. Passo a Passo para Decodificar Novos Pacotes

Ao analisar novos pacotes utilizando Rea + Binary Ninja no `SWGEmu.exe`:

1. **Localização de RTTI e VTable:**
   - Buscar string da classe C++ `.??_R0?AV<NomeDoPacote>@@@8` (RTTI Type Descriptor).
   - Obter referências cruzadas para a Complete Object Locator (`??_R4...`).
   - Mapear a Virtual Table (vtable) associada ao objeto.

2. **Identificação do Construtor ReadIterator:**
   - O construtor de rede aceita tipicamente `(this, Archive::ReadIterator &)`.
   - Localizar chamadas para `Archive::AutoVariable<T>::AutoVariable(..., Archive::AutoByteStream &)` ou `addVariable()`.
   - Mapear a ordem exata dos campos na pilha/heap (`+0x2c`, `+0x3c`, etc.).

3. **Criação da Documentação:**
   - Gerar a página HTML em `swgdocs/<section>/<NomeDoPacote>.html`.
   - Gerar o arquivo Markdown em `swgdocs/content/<section>/<NomeDoPacote>.md`.
   - Criar amostra de hex dump representativa com operand count (`0x0002` para mensagens de topo, `0x0005` com `0x0000000B` para ObjectControllers).

4. **Sincronização dos Bancos de Dados:**
   - Atualizar `swgdocs/search-index.json`.
   - Atualizar `swgdocs/data/packets_summary.json` (mudando status para `100%` e `present`).
   - Atualizar `swgdocs/data/all_packets.csv`.
   - Executar `python scripts/generate_protocol_data.py` para atualizar o Inspetor.

5. **Registro no Histórico:**
   - Adicionar o pacote em `swgdocs/data/reversal_history.json` ou usar `record_packet`.
   - Executar `python scripts/update_history.py`.

6. **Atualização do Backlog de Pendentes (0%):**
   - Executar `python scripts/generate_pending_page.py` para sincronizar `swgdocs/pending/index.html`, `data/pending_items.json` e `data/pending_items.csv` (o pacote recém-decodificado sairá automaticamente da lista de pendências).

---

## 🛡️ 4. Checklist Pré-Commit

Antes de publicar qualquer alteração no branch `main` (GitHub Pages):

- [ ] `python scripts/update_history.py` executado sem erros.
- [ ] `python scripts/generate_pending_page.py` executado sem erros.
- [ ] `history/index.html` e `pending/index.html` refletem a numeração correta.
- [ ] Opcode copiável e link clicável funcionando no histórico e na página de pendentes.
- [ ] Nenhum texto residual de disclaimer legado presente.
- [ ] `git status` validado e arquivos comitados com mensagem descritiva.
