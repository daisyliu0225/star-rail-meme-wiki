# Wiki Integration Import Guide

這是**單一整合交付包**，並非逐篇解壓縮。

1. 將 ZIP 解壓後的 `wiki/` 資料夾複製到既有 `star-rail-meme-wiki/` 根目錄，允許覆蓋先前 SRC-001 的 `wiki/index.md`、`wiki/log.md` 與案例／概念頁；`wiki/sources/SRC-001.md` 已合併保留。
2. `staging/review/` 是人類審核與清理紀錄；`staging/cleaned/` 是供查詢的清理版來源全文。**若 GitHub 為公開 repo，請勿把 `raw/` 或 `staging/cleaned/` 中的第三方文章全文推上去**，可保留本地版本。
3. 若本地有尚未上傳給助理的新版本 Wiki，先備份／比較差異，避免覆蓋。
4. 如未安裝 PyYAML，先執行 `python -m pip install -r scripts/requirements.txt`。再執行 `python scripts/lint_wiki.py` 做本地連結／ID／Metadata 結構檢查；此檢查**不驗證事實內容、來源網址有效性或圖片授權**。
5. 根據結果做 `git status`、`git add wiki/ staging/review/ scripts/`、`git commit`。

這份 ZIP **不包含完整 raw 文章**（它們已在使用者手上的原始資料與前一份清理包），也不會覆寫 `AGENTS.md`。

## 計數方法

- 來源快照共 8 份；其中 `SRC-004-1` 和 `SRC-006-2` 缺完整 URL，不能計入「來源追溯完整」的項目。
- 原始來源網址已記錄 6 份（包含 SRC-001），但尚未逐一外部連線核驗。
- 審核表先前統計為 20 條，逐項重新核對其實共有 23 條；核准 Claims：SRC-001 = 6；本次 SRC-002～006（含補充）= 23；合計 29。
