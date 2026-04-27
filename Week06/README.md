# Python 程式設計基礎：實務練習

本專案收錄了 Python 程式設計課程第八章的三份核心作業。內容聚焦於 **自定義模組化 (Module Import)**、**函式多值回傳 (Tuple Return)**、**字典 (dict) 統計處理**，以及模擬實務開發中的 **下注驗證、UI 自動化等待、合法值建議** 等應用情境。

## 📁 作業內容說明

### 1. 下注結果統計報表 (基礎題) - `homework_week6_01.py`

**題目目標：** 將「下注結果列表」傳入自定義模組，自動計算成功率、失敗原因分布，並找出最常見的失敗原因。

* **功能邏輯：**
  + **模組化呼叫**：由 `bet_summary.py` 提供 `summarize_bets()`，主程式僅負責資料準備與結果輸出。
  + **多值回傳 (Tuple Unpacking)**：一次接收 `pass_rate`、`failed_reasons`、`top_failed_reason` 三個回傳值。
  + **防呆機制**：當 `total = 0` 時避免除以零錯誤。
  + **字典統計**：使用 `dict.get()` 累計各失敗原因次數，並用 `max() / min()` 找出出現最多次的原因（同次數時取字母最小者）。
* **學習重點：** 自定義模組 (`from ... import ...`)、Tuple 解包、`sum()` 條件式計數、`dict` 累計統計。

---

### 2. UI 自動化等待元素 (進階題) - `homework_week6_02.py`

**題目目標：** 模擬前端 UI 自動化測試中「等待目標元素出現」的情境，依序檢查每張畫面快照 (snapshot)，並在找到目標時立即停止。

* **功能邏輯：**
  + **模組化呼叫**：由 `ui_waiter.py` 提供 `wait_for_element()`，主程式負責準備 snapshot 與目標元素。
  + **重試上限控制**：實際檢查次數 = `min(len(snapshots), max_retry)`，避免超出 snapshot 範圍。
  + **早停機制 (Early Exit)**：一旦在某張 snapshot 找到 `target`，立即 `return` 並回傳已檢查次數。
  + **邊界情境測試**：包含「max_retry 太小」、「target 不存在」、「第一張就找到」等案例驗證。
* **學習重點：** 巢狀資料結構 (`list[list[str]]`)、迴圈中的提早結束、Tuple 多值回傳、邊界 (Edge Case) 測試思維。

---

### 3. 下注金額驗證與建議 (整合挑戰題) - `homework_week6_03.py`

**題目目標：** 模擬下注系統中「金額是否合法」的驗證流程，若不合法則自動推算「最接近的合法下注金額」回饋給使用者。

* **功能邏輯：**
  + **多模組整合**：同時匯入 `validate_stake.py` 與 `suggest_stake.py`，分別負責「驗證」與「建議」。
  + **角色分流**：依使用者 `vip` 屬性 (`True / False`) 套用不同上限 (`vip_max` vs `normal_max`)。
  + **三層驗證規則**：低於最低額 (`below_min`) → 高於最高額 (`above_max`) → 非 step 倍數 (`invalid_step`)。
  + **智慧建議**：太小 → 拉到最低；太大 → 壓到最高；非倍數 → 用 `round(stake / step) * step` 取最接近合法值。
* **學習重點：** 多模組協作、布林旗標 (Flag) 設計、條件分支設計、`round()` 數值修正、職責分離 (Validate vs Suggest)。

---

## 🚀 執行方式

1. **下注結果統計：**

   ```bash
   python3 homework_week6_01.py
   ```

2. **UI 等待元素：**

   ```bash
   python3 homework_week6_02.py
   ```

3. **下注金額驗證與建議：**

   ```bash
   python3 homework_week6_03.py
   ```

## 📸 執行結果截圖

| 作業 | 截圖 |
|------|------|
| 下注結果統計 | `Week6_hw01.png` |
| UI 等待元素 | `Week6_hw02.png` |
| 下注金額驗證與建議 | `Week6_hw03.png` |
