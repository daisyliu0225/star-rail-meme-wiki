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

本專案已完成 10 份 Source Notes 的整理與整合，包含 37 條經人工審核的 Claims，並以此建立 13 張互動式 HTML 教學簡報。

完成 Wiki 整合與簡報生成後，執行 `scripts/lint_wiki.py` 進行結構檢查。

檢查結果如下：

```text
Source notes: 10
Unique claim IDs: 37
Errors: 0
Warnings: 4
```

Lint 未發現結構性錯誤。四項警告來自部分來源缺少完整原始網址，相關資訊限制已保留於 Wiki 中。

此外，已透過瀏覽器檢查 HTML 簡報的頁面切換、圖片顯示及基本互動功能，並將簡報部署至 GitHub Pages。

**線上簡報：**  
https://daisyliu0225.github.io/star-rail-meme-wiki/slides/index.html

## Workflow 反思

### 哪個節點最容易出錯？

本次執行中，Source Cleaning 與 Metadata Validation 是最需要注意的節點。

在處理網頁資料時，曾遇到大量無關的 HTML、SVG 與 Base64 內容，也發生過來源 Metadata 混淆的問題。如果沒有及時檢查，這些錯誤可能進一步影響 Claim Extraction 與 Wiki Integration。

### 如何調整檢查流程？

因此，本專案將 Source Cleaning 與 Metadata Validation 安排在 Claim Extraction 之前，並加入 Human Review，確認來源資訊、主張內容與證據限制後，才正式整合至 Wiki。

在 HTML 簡報製作階段，也發現原本缺少「星神與命途」的背景介紹。為改善初學者的理解程度，重新蒐集並審核 SRC-007 與 SRC-008，更新 Wiki 後再次生成簡報，將投影片由 12 張擴充為 13 張。

此外，透過瀏覽器測試發現部分圖片尺寸、顯示位置及背景透明度不符合預期，因此重新調整版面並進行人工驗收。

### 本次執行的主要收穫

本次作業顯示，LLM Wiki 不只是一次性生成的文件，而是可以透過來源檢查、人工審核、結構驗證與簡報回饋持續改善的知識庫。

透過將檢查安排在資料整合之前，可以降低錯誤向下游傳遞的機會；而簡報製作過程中發現的知識缺口，也能反向促使 Wiki 補充與修正。

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
