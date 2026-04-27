# validate_stake.py
# 功能：檢查使用者下注金額 stake 是否合法
# 回傳：(ok, reason)
#   ok: True / False
#   reason: "below_min" / "above_max" / "invalid_step" / ""
 
def validate_stake(user, stake, limits):
    # 1) 低於最低下注額
    if stake < limits["min"]:
        return (False, "below_min")
 
    # 2) 高於最高下注額（VIP 與一般用戶不同）
    if user["vip"]:
        max_allowed = limits["vip_max"]
    else:
        max_allowed = limits["normal_max"]
 
    if stake > max_allowed:
        return (False, "above_max")
 
    # 3) 必須是 step 的倍數（例如 step=10 時，27 不合法）
    if stake % limits["step"] != 0:
        return (False, "invalid_step")
 
    # 全部都通過 → 合法
    return (True, "")