# Star Rail Meme Wiki

## 專案簡介

本專案以《崩壞：星穹鐵道》的迷因文化與官方敘事為主題，建立一個由 LLM 輔助整理、並經過人工審核的 Markdown Wiki。

研究案例包含開拓者與垃圾桶的互動、Rickroll 彩蛋、HoYoFair 愚人節創作，以及「歡愉」相關版本內容。

最終利用 Wiki 作為知識來源，製作一份 **13 頁的互動式 HTML 教學簡報《從垃圾桶到阿哈》**，讓未接觸過遊戲的讀者也能理解基本世界觀與迷因文化的關係。

## 專案成果

- [教學 HTML 簡報](https://daisyliu0225.github.io/star-rail-meme-wiki/slides/index.html)
- [LLM Wiki](./wiki/index.md)
- [AI 工作規範](./AGENTS.md)
- [Claim 與投影片對應](./slides/CLAIM_TO_SLIDE.md)
- [Wiki 更新紀錄](./wiki/log.md)
- [簡報產生紀錄](./slides/GENERATE_LOG.md)

## LLM Wiki 建立成果

目前 Wiki 收錄：

- 10 份 Source Notes
- 37 條具有唯一識別碼的 Claims
- Concepts、Cases、Syntheses 等知識頁面

來源包括遊戲官方公告、遊戲媒體報導與玩家社群資料。專案區分來源可信度、遊戲正史地位及玩家推測，避免將不同性質的內容混為一談。

## Loop / Graph 設計

```text
Source Collection
        ↓
Source Cleaning
        ↓
Metadata Validation
        ↓
Claim Extraction
        ↓
Human Review
        ↓
Wiki Integration
        ↓
Lint / Query
        ↓
HTML Slide Generation
        ↓
Browser Review
```

當來源資訊有問題時，回到 Source Cleaning 或 Metadata Validation。

當主張缺乏證據時，回到 Claim Extraction 或補充來源。

當簡報缺少必要背景時，回到 Wiki Integration 補充知識，再重新產生簡報。

當圖片或版面不符合教學需求時，修改簡報呈現方式並重新測試。

## 實際執行與檢查

整合 SRC-007（星神）及 SRC-008（命途）後，Wiki 的結構檢查結果如下：

```text
Source notes: 10
Unique claim IDs: 37
Errors: 0
Warnings: 4
```

警告主要來自部分來源缺乏完整原始網址，已保留限制說明，沒有將其當成完全驗證的來源。

以上為整合階段的檢查結果，最終提交前會再次執行 Lint。

## Workflow 反思

### 哪個節點最容易出錯？

本次執行中，Source Cleaning 與 Metadata Validation 特別需要注意。

網頁擷取可能包含不必要的格式資料，而不同來源的標題、作者與網址也可能在整理時發生混淆。

### 如何調整檢查流程？

原本可能在 Wiki Integration 才發現來源問題，因此將 Source Cleaning 與 Metadata Validation 提前到 Claim Extraction 之前，並加入 Human Review。

此外，在製作簡報時發現缺少「星神與命途」的背景知識，因此新增兩篇來源，經審核後重新整合 Wiki，並將教學簡報由 12 頁擴充為 13 頁。

這次修改顯示：LLM Wiki 不只是一次性產生的文件，而是能透過人工回饋持續修正的知識庫。

## 本機檢查方式

在 Repository 根目錄執行：

```powershell
python scripts/lint_wiki.py
```

在本機開啟簡報：

```powershell
start .\slides\index.html
```

## 資料與使用說明

本專案使用生成式 AI 協助資料整理、Claim Extraction、Wiki 建立、程式撰寫與 HTML 簡報製作。

來源選擇、重要主張核准、內容修正和最終驗收由使用者執行。

第三方文章原始擷取內容不在公開 Repository 中提供，請透過各 Source Note 所列的原始網址參閱相關資料。

遊戲名稱、角色及相關素材之權利屬各自權利人。本專案僅供課程研究與教學使用。