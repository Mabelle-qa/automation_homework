# hw02.py
# 作業 2：密碼長度驗證（加強版）


def main():
    account = input("請輸入帳號：")
    pwd = input("請輸入密碼：")

    # 1) 先做長度檢查
    if len(pwd) < 8:
        print("⚠️  密碼長度不足，請重新設定（至少 8 碼）")
        return  # 直接結束；

    # 2) 再做帳密驗證
    if account == "admin" and pwd == "12345678":
        print("✅ 登入成功！")
    else:
        print("❌ 帳號或密碼錯誤")


if __name__ == "__main__":
    main()
