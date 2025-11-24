# homework01.py
# 作業 1：投注資格檢查程式（基礎版）


def main():
    user_name = input("請輸入姓名：")
    user_age = input("請輸入年齡：")

    # 1) 先做年齡檢查
    if int(user_age) < 18:
        print("❌ 未成年，禁止下注")
        return
    else:
        user_stake = float(input("請輸入投注金額："))
        # 2) 再做投注金額檢查
        if user_stake < 0:
            print("❌ 金額必須大於 0！")
            return
        print("✅ 可以參與下注")
        print(f"嗨！{user_name}歡迎來到FCOM，希望你有很愉快的使用體驗！")


if __name__ == "__main__":
    main()
