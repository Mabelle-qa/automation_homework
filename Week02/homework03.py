# homework03.py
# 作業 3：下注模擬 CLI 工具（進階挑戰題）


def main():
    user_account, user_age, user_stake, user_odds, bet_type = input("請輸入輸入 Email、年齡、投注金額、賠率、下注類型（可為 \"single\" 或 \"multi\"，請用逗號分開）：" \
    "").strip().split(",")
    # 1) 先移除空白跟轉成小寫
    user_account=user_account.strip().lower()
    # 2) 檢查是否有@跟.
    if "@" in user_account and "." in user_account:
    # 3) 將年齡轉成int
        user_age = int(user_age)
    # 4) 判斷有沒有超過18歲並組合成payload字典
        if user_age >= 18:
    # 5) 將stake轉成float
            user_stake = float(user_stake)
            if user_stake > 0:
    # 6) 將odds轉成float
                user_odds = float(user_odds)
                if user_odds > 0:
                    if bet_type.lower() == "single":
                        total_win = user_stake*user_odds
                        payload = {"user": user_account, "age": user_age, "Stake": user_stake, "Odds": user_odds, "Total Win": total_win}
                        print(f"Payload是：{payload}\n下注成功！！！")
                    elif bet_type.lower() == "multiple":
    # 7) 多重投注加成
                        total_win = user_stake*user_odds*1.05
                        payload = {"user": user_account, "age": user_age, "Stake": user_stake, "Odds": user_odds, "Total Win": total_win}
                        print(f"Payload是：{payload}\n下注成功！！！")
                    else:
                        print("❌ 請輸入正確的bet type！！！")
                else:
                    print("❌ Odds必須大於0！！！")
                    exit()
            else:
                print("❌ Stake必須大於0！！！")
            
        else:
            print("❌ 未滿18！！！")
    else:
        print("❌ Mail帳號格式錯誤！！")



if __name__ == "__main__":
    main()