# Pre-Ingest Human Review — SRC-002～SRC-006

> 狀態：待人工審核。此文件列出候選 Claims；尚未更新 `wiki/`。

## 第一輪清理紀錄

| Source | 類別 | 清理重點 | 待核對事項 |
|---|---|---|---|
| SRC-001-trash-can.md | secondary | 原本已人工核准，不再次變更 Claims；只做形式清理。 | 已核准 |
| SRC-002.md | community | 原始 Metadata 錯誤：作者/媒體/類別已改；發文日期待查。 | 待 Human Review |
| SRC-003.md | official | 移除 Base64 圖片；保留官方公告正文；更新日不等於文章發表日。 | 待 Human Review |
| SRC-004.md | secondary | 移除網頁導覽與 SVG；仍是媒體報導，非 HoYoFair 第一手影片。 | 待 Human Review |
| SRC-004-1.md | community | 去除知乎關鍵字追蹤連結；缺文章 URL/作者。 | 待 Human Review |
| SRC-005.md | community | 移除論壇 UI／等級／GP；僅第一頁，不能當整體輿情統計。 | 待 Human Review |
| SRC-006-1.md | official | 移除 Base64 圖片；保留官方公告正文；更新日不等於文章發表日。 | 待 Human Review |
| SRC-006-2.md | secondary | 保留文章與前瞻資訊；原始文章網址及作者待核對（先前巴哈論壇連結不一定是此文章）。 | 待 Human Review |

## 審核規則

- 每個 Claim 以 `Accept / Revise / Reject` 標記，並可補寫原因。
- `source_authenticity` 判斷文件發布者；`canonical_status` 判斷單一主張對正史的關係。
- 來源明確報導遊戲設定，不表示已由遊戲內第一手文本交叉證實。
- 同一來源中的「事實／解讀／推論」要分開審核。
- 沒有完整原文 URL 的補充資料可先保留草稿，但不得當成通過完整來源驗證。

## 候選 Claim 清單


### SRC-002 — 【心得】一定要養成隨手翻垃圾桶的好習慣

#### C002-01
- **Claim:** 樓主記錄長樂天一處可互動且無法打破的瓶子。
- **source_authenticity:** `community`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 樓主描述「長樂天地圖」「有一個打不破的瓶子」。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C002-02
- **Claim:** 樓主稱交付五包垃圾後可取得道具。
- **source_authenticity:** `community`
- **canonical_status:** `unverified`
- **Evidence pointer:** 樓主描述「帶五包垃圾袋」「給你一些道具」；需與遊戲內物品名稱核對。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C002-03
- **Claim:** 回覆玩家以 RPG 探索習慣解釋翻垃圾桶的行為。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 2 樓稱回合制 RPG 經驗使其養成翻箱倒櫃的習慣。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-003 — 4.0版本「滿月是神不在的時間」版本更新說明

#### C003-01
- **Claim:** 4.0 官方版本名為「滿月是神不在的時間」，更新日期為 2026-02-13。
- **source_authenticity:** `official`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 版本更新說明的版本標題與更新時間。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C003-02
- **Claim:** 二相樂園是 4.0 開拓任務的故事舞台。
- **source_authenticity:** `official`
- **canonical_status:** `canon`
- **Evidence pointer:** 「開拓任務『二相樂園』」與全新場景段落。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C003-03
- **Claim:** 4.0 新增與歡愉有關的角色及戰鬥機制（例如阿哈時刻、笑點）。
- **source_authenticity:** `official`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 「全新角色」描述爻光／火花技能與歡愉機制。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C003-04
- **Claim:** 官方版本公告亦使用自我戲謔、社群化的表述。
- **source_authenticity:** `official`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 如「入場前請自行檢查今日幽默感是否達標」；屬本文作者分析。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-004 — 《崩壞：星穹鐵道》火花據傳將推出全新 Cover 單曲？大概吧…

#### C004-01
- **Claim:** Paradaily 將該短片稱為 HoYoFair 發布的愚人節同人作品，而非遊戲正式情報。
- **source_authenticity:** `secondary`
- **canonical_status:** `non_canon`
- **Evidence pointer:** 文章明確區分「並非官方正式情報」與「官方支持的同人作品」。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C004-02
- **Claim:** 報導指出短片以 Never Gonna Give You Up 為題並由火花演唱。
- **source_authenticity:** `secondary`
- **canonical_status:** `non_canon`
- **Evidence pointer:** 正文說明 MV 內容；需依 HoYoFair 官方影片佐證。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C004-03
- **Claim:** 報導稱作品具有歌曲使用授權及配音演出。
- **source_authenticity:** `secondary`
- **canonical_status:** `unverified`
- **Evidence pointer:** 作者報導授權和 Lizzie Freeman；待核 HoYoFair 官方影片說明。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-004-1 — 愚人節《崩壞：星穹鐵道》Rickroll 動畫相關評論（擷取頁未含標題）

#### C004A-01
- **Claim:** 一篇知乎評論稱動畫中角色模仿 Rickroll 並使用反差幽默。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 文章段落談及火花、銀狼、刃等角色的舞蹈。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C004A-02
- **Claim:** 評論者認為 Rickroll 在崩鐵早期亦曾出現。
- **source_authenticity:** `community`
- **canonical_status:** `unverified`
- **Evidence pointer:** 文章稱早期介紹阿哈時已經玩過此梗；可與 SRC-001 交叉比對。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C004A-03
- **Claim:** 評論者正面評價作品的製作品質與授權處理。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 文章評論段落；不得推論所有玩家持相同意見。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-005 — 【劇情】4.0版本主線討論集中串「滿月是神不在的時間」

#### C005-01
- **Claim:** 玩家對 4.0 敘事有正反評價。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 第 4、5、7、11、18 樓等評價有明顯差異；限本次擷取的第一頁樣本。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C005-02
- **Claim:** 部分玩家認為 4.0 使用幽默演出、迷因影響劇情體驗。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 第 8、11、18 樓的觀察與評價。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C005-03
- **Claim:** 部分玩家從畫面及地名推測開發方案可能被調整。
- **source_authenticity:** `community`
- **canonical_status:** `unverified`
- **Evidence pointer:** 第 15 樓以主觀語氣推測；不是開發商證詞。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C005-04
- **Claim:** 部分玩家將二相樂園與其他遊戲／日本文化作比較。
- **source_authenticity:** `community`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 第 20 樓提及日本文化與其他作品的聯想。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-006-1 — 4.7版本「此刻，将群星付之一笑」版本更新说明

#### C006-01
- **Claim:** 4.7 官方版本名為「此刻，將群星付之一笑」，於 2026-11-11 更新。
- **source_authenticity:** `official`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 版本更新標題、更新時間。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C006-02
- **Claim:** 版本公告將「星神★阿哈」列為新五星角色並描述歡愉命途機制。
- **source_authenticity:** `official`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 「全新角色」中星神★阿哈條目。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C006-03
- **Claim:** 官方新增二相樂園後續開拓任務、場景點星船與瞬息歡愉。
- **source_authenticity:** `official`
- **canonical_status:** `canon`
- **Evidence pointer:** 「全新劇情」與「全新場景」段落。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`


### SRC-006-2 — 《崩壞：星穹鐵道》4.7 版本前瞻資訊（擷取頁未含文章標題）

#### C006B-01
- **Claim:** 媒體前瞻將 4.7 故事描述為二相樂園篇章高潮。
- **source_authenticity:** `secondary`
- **canonical_status:** `interpretation`
- **Evidence pointer:** 開頭敘述；前瞻定位，不等於事後劇情評析。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C006B-02
- **Claim:** 報導提到阿哈、奧博洛斯與幻月遊戲相關的故事預告。
- **source_authenticity:** `secondary`
- **canonical_status:** `unverified`
- **Evidence pointer:** 前瞻敘述；具體情節應與遊戲正式版本核對。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

#### C006B-03
- **Claim:** 前瞻兌換碼包含 NEVERGONNAGIVE、NEVERGONNAMAKE。
- **source_authenticity:** `secondary`
- **canonical_status:** `not_applicable`
- **Evidence pointer:** 報導末尾列出兩組代碼；不可推導官方長期劇情規劃。
- **Review:** `[ ] Accept`　`[ ] Revise`　`[ ] Reject`

## 需要人工決定的問題

1. SRC-002 中「五包垃圾袋」是否應標成原文用語而不認定正式道具名稱？（建議是）
2. SRC-005 的玩家推測是否只保留為「未證實推測」案例？（建議是）
3. SRC-004-1 是否能補原始文章網址？若無，先不當成正式已驗證來源。
4. SRC-006-2 的原始 URL／文章作者要不要繼續核對？

## 此輪尚未執行

- 未建立或修改任何 `wiki/sources/`、`wiki/cases/`、`wiki/index.md`、`wiki/log.md`。
- 未核准 SRC-002～006 的任何 Claim；因此不得把上述候選計入已完成 Ingest。
- 未聲稱完成外部連結有效性驗證或圖片可用性檢查。
