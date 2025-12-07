# check_bet_input.py
# 進階挑戰題：下注自動決策 CLI 工具（實務版）
#
# 函式：bet_input_check
# 目標：
#   根據題目要求，依序檢查：
#   1. 年齡是否 >= 18
#   2. 餘額是否 >= 100
#   3. 帳號是否已驗證
#   4. 帳號是否被封鎖
#   5. 依條件輸出對應「下注策略」與結果報告 payload


def bet_input_check(age, balance, verified, is_vip, is_blocked):
    # payload 用來存放決策輸出結果（年齡 / 餘額 / 策略 / 下注結果）
    payload = {}

    # 1) 先檢查年齡是否滿 18 歲
    if age < 18:
        print("❌ 未滿18！！！")
        return  # 不符合條件，直接結束

    # 2) 檢查餘額是否足夠（至少 100）
    if balance < 100:
        print("⚠️ 餘額不足！！！")
        return

    # 3) 檢查帳號是否經過驗證
    if not verified:
        print("❌ 未驗證，請先驗證！！！")
        return

    # 4) 檢查帳號是否被封鎖
    if is_blocked:
        print("❌ 風險高用戶，請聯繫客服！！！")
        return

    # 5) 通過前面所有條件後，根據 VIP 與餘額決定下單策略
    #    策略對照：
    #    - VIP 且餘額 >= 2000 → 🔥 超高風險策略
    #    - VIP 且餘額 >= 1000 → 💎 高風險策略
    #    - 非 VIP 且餘額 >= 1000 → 🥇 穩定策略
    #    - 非 VIP 且餘額 >= 500 → 🥈 中階策略
    #    - 其他 → 🔰 保守策略

    if is_vip and balance >= 2000:
        payload = {
            "Age": age,
            "Balance": balance,
            "Strategy": "🔥 超高風險策略！！！",
            "Result": "下注成功！！！",
        }
    elif is_vip and balance >= 1000:
        payload = {
            "Age": age,
            "Balance": balance,
            "Strategy": "💎 高風險策略！！！",
            "Result": "下注成功！！！",
        }
    elif (not is_vip) and balance >= 1000:
        payload = {
            "Age": age,
            "Balance": balance,
            "Strategy": "🥇 穩定策略！！！",
            "Result": "下注成功！！！",
        }
    elif (not is_vip) and balance >= 500:
        payload = {
            "Age": age,
            "Balance": balance,
            "Strategy": "🥈 中階策略！！！",
            "Result": "下注成功！！！",
        }
    else:
        payload = {
            "Age": age,
            "Balance": balance,
            "Strategy": "🔰 保守策略！！！",
            "Result": "下注成功！！！",
        }

    # 將決策結果印出（也可以改成 return 給呼叫端使用）
    output_text = "\n".join([f"{key}: {value}" for key, value in payload.items()])
    print(output_text)
    return payload
