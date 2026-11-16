# Wiki Operations Log

## [2026-11-16] ingest | SRC-001 — 4Gamers trash-can article

- **Operation**: Human-reviewed ingest and Wiki integration.
- **Raw source**: `raw/articles/SRC-001-trash-can.md`（使用者已提供 Markdown 文章內容；本 ZIP 不覆蓋使用者本地的 raw 檔案）。
- **Review decision**: 使用者明確核准 `C001, C002, C003, C004, C005, C006` 全部納入。
- **Source type**: `secondary`（4Gamers 媒體報導）。
- **Files created**:
  - `wiki/sources/SRC-001.md`
  - `wiki/cases/trash-can.md`
  - `wiki/concepts/meme-culture.md`
  - `wiki/concepts/rickroll.md`
  - `wiki/index.md`
  - `wiki/log.md`
- **Policy decisions**: 遊戲文本細節 C001/C002/C005 先保持 `unverified`（缺少第一手文本）；社群觀察 C003 屬 `not_applicable`，媒體詮釋 C004/C006 屬 `interpretation`。
- **Unresolved**: 遊戲原始互動截圖、智庫原文與社群原帖尚未逐項獨立交叉驗證。
- **Validation**: 本地檢查 Markdown 內部相對連結、Metadata ID 及核准 Claim IDs；結果見交付說明，不代表語意事實已全數核實。
- **Next**: Ingest SRC-002，並在累積五份不同來源後執行完整 Wiki lint。


## [2026-11-16] pre-ingest | Raw Source Cleaning（先前已完成）

- **Operation**：對 8 份上傳的 Markdown 執行前處理，原始檔保留；另外建立 `staging/cleaned/` 供分析。
- **Observed issues**：SRC-002 的作者／來源類型誤植；SRC-003 與 SRC-006-1 的 Base64 圖片；SRC-004 網站 SVG／介面雜訊；SRC-004-1 與 SRC-006-2 缺完整原始 URL。
- **Policy change/proposal**：Ingest 前加上 Metadata Check 與 Accessibility/Provenance Check；不能將 URL 存在等同外部連結驗證通過。
- **Details**：`staging/review/CLEANING_LOG.json`、`staging/review/PRE_INGEST_REVIEW.md`。此步驟只代表文字清理，不代表資料真實性完成核實。

## [2026-11-16] ingest | SRC-002～SRC-006（含 SRC-004-1、SRC-006-1、SRC-006-2）

- **Human review**：使用者明確核准 `PRE_INGEST_REVIEW.md` 中全部 **23 個候選 Claims**，要求保留證據限制；沒有要求提升 `unverified` 的狀態。
- **Approved IDs**：C002-01, C002-02, C002-03, C003-01, C003-02, C003-03, C003-04, C004-01, C004-02, C004-03, C004A-01, C004A-02, C004A-03, C005-01, C005-02, C005-03, C005-04, C006-01, C006-02, C006-03, C006B-01, C006B-02, C006B-03.
- **Integration**：新增 7 份 Source Notes；保留既有 SRC-001 的 6 個核准 Claims；更新垃圾桶、迷因文化及 Rickroll 既有頁；建立歡愉版本、HoYoFair、社群解讀、來源區分與綜合分析頁；重建索引。
- **Evidence handling**：把 `source_authenticity` 和逐條 `canonical_status` 分開；保留缺少 URL 的來源 `url: unknown`；論壇評價限定為第一頁樣本；開發改稿猜測維持 `unverified`。
- **Raw file handling**：既有 `raw/` 未被覆寫；此交付僅包含 Wiki 與審核附件，完整來源快照仍位於使用者原始資料／先前清理包。
- **Not done**：未驗證所有外部網址是否可用；未直接比對遊戲內全部原始文本；未生成 HTML Slides，不能聲稱這些工作通過。

- **Mechanical lint（本次實際執行）**：`python scripts/lint_wiki.py` → Source notes: 8；Unique claim IDs: 29；Errors: 0 Warnings: 2；WARNING wiki/sources/SRC-006-2.md: original URL missing；WARNING wiki/sources/SRC-004-1.md: original URL missing；不含外部網址或內容真偽檢查。
