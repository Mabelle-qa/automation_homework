from ui_waiter import wait_for_element


def main():
    snapshots = [
    ["#login"],
    ["#login", "#username"],
    ["#login", "#username", "#password"],
    ["#login", "#username", "#password", "#submit"]
    ]
    target = "#submit"
    max_retry = 5


    found, attempt_count = wait_for_element(snapshots, target, max_retry)
 
    print("===== 等待結果 =====")
    print(f"target          : {target}")
    print(f"max_retry       : {max_retry}")
    print(f"found           : {found}")
    print(f"實際檢查次數    : {attempt_count}")
 
    # ---- 加碼測試幾種邊界情況 ----
    print("\n===== 額外測試 =====")
 
    # 案例 A:max_retry 太小,還沒等到 #submit 出現就停了
    found_a, n_a = wait_for_element(snapshots, "#submit", max_retry=2)
    print(f"max_retry=2  → found={found_a}, attempt_count={n_a}")
 
    # 案例 B:target 根本不存在
    found_b, n_b = wait_for_element(snapshots, "#nope", max_retry=5)
    print(f"target=#nope → found={found_b}, attempt_count={n_b}")
 
    # 案例 C:第一張就找到
    found_c, n_c = wait_for_element(snapshots, "#login", max_retry=5)
    print(f"target=#login→ found={found_c}, attempt_count={n_c}")
 
 
# 這段是 Python 的慣例寫法:
# 只有「直接執行 main.py」時才會跑 main()
# 如果是被 import,就不會自動執行
if __name__ == "__main__":
    main()