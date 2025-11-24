# hw01.py
# 作業 1：CLI 登入系統（基礎版）


def main():
    account = input("請輸入帳號：")
    pwd = input("請輸入密碼：")

    # 做帳密驗證
    if account == "admin" and pwd == "1234":
        print("✅登入成功！！！")
    else:
        print("❌登入失敗！！！")


if __name__ == "__main__":
    main()
