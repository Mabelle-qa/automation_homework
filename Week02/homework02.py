# homework02.py
# 作業 2：自動化 Payload Builder（進階實作）


def main():
    user_mail = input("請輸入email帳號：")
    user_age = input("請輸入年齡：")
    user_stake = float(input("請輸入投注金額："))
    user_odds = float(input("請輸入賠率："))
    try:
        # 1) 先做mail檢查
        # a) 先做空白檢查
        if user_mail == "":
            print("⚠️ 輸入不得為空！")
            return  # 直接結束；
        # b) 接著做email驗證
        if "@" in user_mail and "." in user_mail:
            print("✅ Email 格式正確！")
            # 2) 再做年齡檢查
            if int(user_age) < 18:
                print("❌ 未成年，禁止下注")
                return
            else:
                # 3) 再做賠率跟下注金額檢查
                if user_stake > 0 and user_odds > 0:
                    print(
                        f'{{"email": {user_mail}, '
                        f'"age": {user_age}, '
                        f'"amount": {user_stake}, '
                        f'"odds": {user_odds}, '
                        f'"expected_profit": {user_stake * user_odds}}}'
                    )

                else:
                    print("❌ 金額或賠率必須大於 0！")
                    return
        else:
            print("❌ Email 格式不正確，請重新輸入！")
            return
    except ValueError:
        print("請輸入正確的資訊格式！")


if __name__ == "__main__":
    main()
