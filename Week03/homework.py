# homework.py
# Chapter 8 | 回家作業 + 進階挑戰題
# 題目：下注自動決策 CLI 工具（實務版）
#
# 功能說明：
# 1. 從使用者讀取「年齡、餘額、是否驗證、是否 VIP、是否封鎖」等資訊
# 2. 將字串輸入轉成對應的型別（int、float、bool）
# 3. 做基本格式檢查（防呆：格式錯誤直接結束）
# 4. 呼叫 bet_input_check 進行條件檢查與策略輸出

from check_bet_input import bet_input_check


def main():
    # 提示使用者輸入，欄位以「英文逗號 ,」分隔
    # 範例：18, 1200, y, n, n
    raw_input_data = input(
        "請輸入：年齡, 餘額, 驗證與否(y/n), VIP與否(y/n), 封鎖與否(y/n)："
    )

    # 先用逗號分隔欄位，再對每個欄位做 strip() 去掉前後空白
    try:
        user_age_str, user_balance_str, verified_flag, is_vip_flag, is_blocked_flag = [
            x.strip() for x in raw_input_data.split(",")
        ]
    except ValueError:
        # split 之後不是剛好 5 個欄位，就代表輸入格式有問題
        print("❌ 輸入格式錯誤，請依照『年齡, 餘額, 驗證(y/n), VIP(y/n), 封鎖(y/n)』輸入！")
        return

    # 初始化布林旗標
    user_verified = False
    is_vip = False
    is_blocked = False

    # 1) 將年齡轉成 int
    try:
        user_age = int(user_age_str)
    except ValueError:
        print("❌ 年齡必須是整數！")
        return

    # 2) 將餘額轉成 float
    try:
        user_balance = float(user_balance_str)
    except ValueError:
        print("❌ 餘額必須是數字！")
        return

    # 3) 將「驗證與否」轉成 boolean
    verified_flag = verified_flag.lower()  # 統一轉小寫後判斷
    if verified_flag == "y":
        user_verified = True
    elif verified_flag == "n":
        user_verified = False
    else:
        print("❌ 請輸入驗證與否為 y 或 n！")
        return  # 防呆：輸入錯誤直接結束，不往下做

    # 4) 將「VIP 與否」轉成 boolean
    is_vip_flag = is_vip_flag.lower()
    if is_vip_flag == "y":
        is_vip = True
    elif is_vip_flag == "n":
        is_vip = False
    else:
        print("❌ 請輸入 VIP 與否為 y 或 n！")
        return

    # 5) 將「是否封鎖」轉成 boolean
    is_blocked_flag = is_blocked_flag.lower()
    if is_blocked_flag == "y":
        is_blocked = True
    elif is_blocked_flag == "n":
        is_blocked = False
    else:
        print("❌ 請輸入封鎖與否為 y 或 n！")
        return

    # 6) 呼叫「下注決策檢查」模組函式
    #    - age: int      使用者年齡
    #    - balance: float 使用者餘額
    #    - verified: bool 是否已驗證
    #    - is_vip: bool   是否為 VIP
    #    - is_blocked: bool 是否被封鎖
    bet_input_check(user_age, user_balance, user_verified, is_vip, is_blocked)


# Python 模組慣用寫法：
# 只有在「直接執行這個檔案」的時候才會跑 main()
if __name__ == "__main__":
    main()
