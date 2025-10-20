# hw_advance01.py
# 作業 進階挑戰：Email 格式驗證（實務導向）


def main():
    userMail = input("請輸入email帳號：")

    # 1) 先做空白檢查
    if userMail == "":
        print("⚠️ 輸入不得為空！")
        return  # 直接結束；

    # 2) 接著做email驗證
    if "@" in userMail and "." in userMail:
        print("✅ Email 格式正確！")
    else:
        print("❌ Email 格式不正確，請重新輸入！")


if __name__ == "__main__":
    main()
