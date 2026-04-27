from bet_summary import summarize_bets

def main():
    bet_results = [
    {"event_id": 1, "stake": 100, "ok": True,  "reason": ""},
    {"event_id": 2, "stake": 120, "ok": False, "reason": "invalid_odds"},
    {"event_id": 3, "stake": 50,  "ok": False, "reason": "inactive_event"},
    {"event_id": 4, "stake": 300, "ok": True,  "reason": ""},
    ]

    # 一次接收三個回傳值 (tuple unpacking)
    pass_rate, failed_reasons, top_failed_reason = summarize_bets(bet_results)

    # 印出結果
    print("===== 下注結果列印 =====")
    print(f"成功率 pass_rate       : {pass_rate:.2f}%")
    print(f"失敗原因 failed_reasons: {failed_reasons}")
    print(f"最常見失敗 top_failed  : {top_failed_reason!r}")
 
 
# 這段是 Python 的慣例寫法:
# 只有「直接執行 main.py」時才會跑 main()
# 如果是被 import,就不會自動執行
if __name__ == "__main__":
    main()