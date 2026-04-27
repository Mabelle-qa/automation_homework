# suggest_stake.py
# 功能：若下注金額不合法，建議「最接近的合法 stake」
# 例：27 → 30、2500(vip=False) → 1000、5 → 10

from validate_stake import validate_stake


def suggest_stake(user, stake, limits):
    # 先檢查是否已經合法，合法就直接回傳原值
    ok, _ = validate_stake(user, stake, limits)
    if ok:
        return stake

    # 找出此使用者的最大限額
    if user["vip"]:
        max_allowed = limits["vip_max"]
    else:
        max_allowed = limits["normal_max"]

    min_allowed = limits["min"]
    step = limits["step"]

    # 1) 太小 → 直接拉到最低下注額
    if stake < min_allowed:
        return min_allowed

    # 2) 太大 → 壓到最高下注額
    if stake > max_allowed:
        return max_allowed

    # 3) 不是 step 倍數 → 取最接近的 step 倍數
    #    用 round() 取四捨五入後再乘回 step
    suggested = round(stake / step) * step

    # 保險：建議值仍要在合法範圍內
    if suggested < min_allowed:
        suggested = min_allowed
    if suggested > max_allowed:
        suggested = max_allowed

    return suggested