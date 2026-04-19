# AI Slide Gen

Claude AI × PptxGenJS 驅動的投影片生成工具。

## 如何使用

直接用瀏覽器開啟 `index.html`，無需任何安裝或 build。

1. 輸入 **Anthropic API Key**（`sk-ant-...`）
2. 填寫客戶名稱、專案說明（越詳細越好）
3. 選擇語言、投影片數量、風格
4. 點擊「用 Claude 生成投影片」
5. 預覽後點「匯出 PPTX」下載真正的 PowerPoint 檔案

## 技術架構

```
ai-slide-gen/
├── index.html               # 主程式（單檔，可直接開啟）
└── src/                     # TypeScript 來源（參考用）
    ├── types/index.ts        # 型別定義
    ├── utils/
    │   ├── claudeApi.ts      # Claude API 整合
    │   └── pptxExport.ts     # PPTX 匯出邏輯
    └── components/
        └── SlideRenderer.ts  # 瀏覽器預覽 HTML 渲染
```

## 支援的投影片類型

| Type | 說明 |
|------|------|
| `cover` | 封面頁 |
| `agenda` | 議程 |
| `problem` | 問題分析 |
| `solution` | 解決方案 |
| `feature` | 功能特點 |
| `timeline` | 執行時程 |
| `team` | 團隊介紹 |
| `budget` | 預算規劃（含表格） |
| `metric` | 關鍵數據（大字展示） |
| `closing` | 結語 / 下一步 |

## 主題

- **Dark Pro** — 深色背景，橘色 accent
- **Light Clean** — 淺色背景，商務清爽
- **Navy Bold** — 深藍背景，藍紫色 accent

## 注意事項

- API Key 會存在 `localStorage`，不會上傳任何地方
- 直接從瀏覽器呼叫 Claude API（需要 `anthropic-dangerous-direct-browser-access` header）
- PPTX 由 [PptxGenJS](https://github.com/gitbrent/PptxGenJS) 在瀏覽器端生成
