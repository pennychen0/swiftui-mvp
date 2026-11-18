# SwiftUI 分階段介面探索 Skill

承接學員從課堂網站複製的整段 Prompt，依序完成設計探索、單頁實作、同風格第二頁與 Navigation。學員可以從空資料夾開始；保留 `swiftui-mvp` 安裝名稱。

最終交付是能在 Xcode 開啟、編譯與執行的完整 SwiftUI iOS App。Go Wide 預覽圖是設計過程的產物，不取代最後的 App。

## 安裝

在 AI Agent 開啟本次工作資料夾後貼上：

```text
幫我把 https://github.com/pennychen0/swiftui-mvp 裡的 swiftui-mvp 資料夾，從 main 分支完整下載到這個專案根目錄的 .agents/skills/ 裡，包含 SKILL.md、references 與 scripts 資料夾。

若已有同名 Skill，請更新成倉庫最新版本，保留其他 Skill。
```

不需要預先建立 Xcode 專案。Agent 不支援此技能目錄時，請它直接讀取 `.agents/skills/swiftui-mvp/SKILL.md`。

## 課堂流程

| 網站貼入的 Prompt | Agent 的產出 |
| --- | --- |
| 1. Go Wide | 同一個手機畫面的五張不同設計預覽圖，編號 1–5；不建立 Xcode 專案、不寫 SwiftUI。 |
| 2. Remix | 整合選定的風格，直接實作可在 Xcode 執行的 SwiftUI 第一頁，並提供試用方式。 |
| 3. 完成作品 | 沿用第一頁，新增同風格第二頁，再整合 Navigation 與返回。收到範例資料 Prompt 時，加入適當資料與「邊緣測試」Preview。 |
| 4. 試用並上傳 | Agent 做可用的命令列檢查、準備交付；學員手動執行、試切換與返回、截圖並上傳。 |
| 5. 上傳作品 | 準備作品說明、兩張執行截圖與可編輯專案資料夾。網站另要求真實內容截圖時，由學員提供素材並完成對應版本。 |

課堂網站提供各階段的 Prompt 和填寫引導。學員把整段文字從網站貼給 Agent，Agent 依照收到的指令製作專案。每階段完成後，等學員貼上網站的下一份 Prompt。整體以課堂 30 分鐘目標及網站或使用者當次時間設定安排。

若網站的 Remix 模板仍有「畫一張設計圖」「先不要寫程式」，請用下列文字取代該段。保留上面學員選填的版本與元件。

```text
請把上面選好的設計元素混搭成同一個風格，直接在專案裡用 SwiftUI 做出可在 Xcode 執行的第一個手機畫面。請提供可以試按的第一頁及開啟方式，先只做這一頁。等我從網站貼上「完成作品」的指令後，再實作第二頁與頁面切換。
```

## 執行限制與品質

- 以下規則由 Agent 內部執行。對學員只呈現成果、具體修改與下一步，不主動說明 Skill 如何限制流程；遇到阻礙與尚未驗證項目仍如實說明。
- 全程不用 Computer Use，不代操 Xcode、模擬器、瀏覽器或網站；允許檔案工具、圖片生成／非互動渲染、`xcodebuild`、`xcrun simctl` 等非 UI 控制方式。
- 沒有產圖能力就如實說明，不用文字或 Xcode 程式冒充五張圖片；學員可依課堂安排找助教。
- 遵循 Apple HIG，注意主次、元件用途、字體可讀性、點按區域、不同尺寸與兩頁風格一致。
- 開發平台是 SwiftUI iPhone／iPad iOS App，不改做 macOS 或 Mac Catalyst。
- 設計圖、Xcode Preview 與實際執行截圖分開標示，未操作的切換與返回不宣稱已驗證。

## 120 MB 與 Xcode 入口

完整交付資料夾的檔案內容總量、ZIP 大小及 ZIP 內未壓縮檔案總量，**各不得超過 120,000,000 bytes（120 MB）**。所有隨交付附上的原始碼、設定、資源、資料、文件、設計圖與截圖都計入，不只計算 Swift 檔案。

```text
MyApp.zip
└── MyApp/
    ├── MyApp.xcodeproj/
    ├── MyApp/
    └── README.md
```

打開專案資料夾第一層就要看到真正的 `.xcodeproj`；必要的 `.xcworkspace` 並列保留。Remix 建立／接手後、交付副本、實際解壓後三次檢查入口；Go Wide 不建立專案。

附帶檢查工具：

```text
python3 <skill路徑>/scripts/check_delivery.py <專案資料夾>
python3 <skill路徑>/scripts/check_delivery.py <解壓後專案資料夾> --zip <ZIP路徑>
```

路徑含空白時需以引號包住。工具不操作 UI，也不證明引用、編譯與互動已通過。

## 內容

- [完整 Skill 指示](swiftui-mvp/SKILL.md)
- [階段辨識與混合 Prompt 情境](swiftui-mvp/references/simulation-examples.md)
- [入口、完整資料夾與 ZIP 大小檢查工具](swiftui-mvp/scripts/check_delivery.py)
