# main.py
# 主程式：把 validate_stake 與 suggest_stake 套到測試資料上
 
from validate_stake import validate_stake
from suggest_stake import suggest_stake
 
 
# 下注限制規則（固定）
limits = {
    "normal_max": 1000,
    "vip_max": 2000,
    "min": 10,
    "step": 10
}
 
# 使用者資料（範例 1：一般用戶）
user_normal = {
    "id": 101,
    "vip": False
}
 
# 使用者資料（範例 2：VIP 用戶）
user_vip = {
    "id": 202,
    "vip": True
}
 
# stake 測試值
stakes_to_test = [5, 27, 120, 2500, 1990]




def run_for_user(user):
    label = "VIP user" if user["vip"] else "Normal user"
    print(f"\n===== 使用者 id = {user['id']}（{label}）=====")
    for stake in stakes_to_test:
        ok, reason = validate_stake(user, stake, limits)
        if ok:
            print(f"stake={stake} → 合法 ✅")
        else:
            suggested = suggest_stake(user, stake, limits)
            print(f"stake={stake} → 不合法 ❌ 原因={reason}，建議改為 {suggested}")
 
# 這段是 Python 的慣例寫法:
# 只有「直接執行 main.py」時才會跑 main()
# 如果是被 import,就不會自動執行
if __name__ == "__main__":
    run_for_user(user_normal)
    run_for_user(user_vip)    
