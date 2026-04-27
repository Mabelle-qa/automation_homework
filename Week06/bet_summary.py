"""
bet_summary.py
這個檔案負責提供 summarize_bets() 函式
給 main.py 使用。
"""

def summarize_bets(bet_results):
    """
    統計下注結果。
 
    參數:
        bet_results (list[dict]): 每一筆都包含
            - event_id (int)
            - stake (int / float)
            - ok (bool)         True = 成功, False = 失敗
            - reason (str)      失敗原因；成功時為 ""
 
    回傳:
        pass_rate (float)        : 成功率百分比 (0 ~ 100)
        failed_reasons (dict)    : 各失敗原因的次數統計
        top_failed_reason (str)  : 出現最多次的失敗原因；
                                   若沒有任何失敗則回傳 ""
    """

    total = len(bet_results)
 
    # ---- 1. 計算 pass_rate ----
    # 用 sum() + 條件式 算出 ok=True 的筆數
    passed = sum(1 for b in bet_results if b["ok"])
 
    # 防呆:如果 total = 0,避免除以 0
    if total == 0:
        pass_rate = 0.0
    else:
        pass_rate = passed / total * 100
 
    # ---- 2. 統計 failed_reasons ----
    failed_reasons = {}
    for b in bet_results:
        # 只統計失敗的(ok = False)
        if not b["ok"]:
            reason = b["reason"]
            # 如果這個原因還沒在 dict 裡 → 設為 0,然後 +1
            failed_reasons[reason] = failed_reasons.get(reason, 0) + 1
 
    # ---- 3. 找出最常見的失敗原因 ----
    if failed_reasons:
        max_count = max(failed_reasons.values())
        # 在「次數最多」的那群裡面,挑字母最小的
        top_failed_reason = min(
            r for r, c in failed_reasons.items() if c == max_count
        )
    else:
        top_failed_reason = ""
 
    return pass_rate, failed_reasons, top_failed_reason