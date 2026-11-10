# SwiftUI MVP Skill

協助學員把已寫好的 Prompt 變成可操作的 SwiftUI iOS MVP。先從「價值、操作體驗、例外情況、取捨、驗收」各問一題，再根據回答安排功能順序並直接開發。

## 下載到專案

在 AI Agent 開啟你的 SwiftUI 專案後，貼上：

```text
幫我把 https://github.com/pennychen0/swiftui-mvp 裡的 swiftui-mvp 資料夾，完整下載到這個專案根目錄的 .agents/skills/ 裡，包含 SKILL.md 與 references 資料夾。若同名資料夾已存在，先告訴我，不要直接覆蓋。
```

下載後的結構應為：

```text
你的專案/
└── .agents/
    └── skills/
        └── swiftui-mvp/
            ├── SKILL.md
            └── references/
                └── simulation-examples.md
```

若使用的 Agent 不支援此技能目錄，可請它直接閱讀 `.agents/skills/swiftui-mvp/SKILL.md` 並依照內容執行。

## 使用方式

1. 準備已建立且能執行的 SwiftUI 專案。
2. 將學習單上寫好的 Prompt 交給 Agent，並指定使用 `swiftui-mvp` Skill。
3. 回答依照你的內容產生的五個問題。
4. Agent 依回答決定功能範圍與開發順序，直接實作；後續細節由 AI 採用建議方案，使用者可隨時要求修改。
5. 依交付的驗收任務操作 App，記錄下一輪改善項目。

預設在五題回答後開始計算 10 分鐘工作預算：約 6–7 分鐘開發，其餘時間建置、修正與交付。這是範圍控制方式，不保證所有點子都能在 10 分鐘完成；實際結果依需求、模型與開發環境而定。

## 內容

- [Skill 指示](swiftui-mvp/SKILL.md)
- [穿搭、朋友分帳與作業管理模擬案例](swiftui-mvp/references/simulation-examples.md)

案例只示範提問深度與決策方式。實際五題必須根據使用者的內容重新設計，不能照抄範例，也不能把範例的假設回答當成使用者的決定。
