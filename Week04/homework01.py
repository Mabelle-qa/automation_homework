# homework01.py
# Chapter 7: 數字過濾器 (基礎)
# 
# 功能說明：
# 1. 若數字為偶數，印出「✅ 偶數」
# 2. 若數字為奇數，印出「⚠️ 奇數」
# 3. 做基本格式檢查（防呆：格式錯誤直接結束）


def main():
    """
    主要執行邏輯：透過迴圈持續接收使用者輸入，並根據數值屬性進行篩選與分類。
    """
    while True:
        user_input = input("請輸入正整數 (範圍 1~50，輸入超過 50 結束)：")
        
        try:
            # 1. 嘗試轉換型別，若失敗則觸發 ValueError
            num = int(user_input)

            # 2. 邊界條件檢查：超過 50 立即終止
            if num > 50:
                print("【終止】數字超過 50，程式結束。")
                break

            # 3. 數值範圍檢查：排除非正整數 (0 與 負數)
            if num <= 0:
                print("❌ 輸入無效：請輸入大於 0 的正整數。")
                continue

            # 4. 核心邏輯：判定奇偶數 (使用餘數運算子 %)
            if num % 2 == 0:
                print(f"✅ {num} 是偶數")
            else:
                print(f"⚠️ {num} 是奇數")

        except ValueError:
            # 防呆處理：當輸入包含文字、小數點或空白時執行
            print("❌ 格式錯誤：請確保輸入為「整數」數字。")
            break # 依照您的需求，格式錯誤直接結束程式

if __name__ == "__main__":
    main()
