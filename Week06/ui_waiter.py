"""
ui_waiter.py
模擬 UI 自動化的「等元素出現」。
給 main.py 使用。
"""
 
 
def wait_for_element(snapshots, target, max_retry=3):
    """
    逐次檢查每一張 snapshot,看 target 元素有沒有出現。
 
    參數:
        snapshots (list[list[str]]): 每一張 snapshot 是當下畫面上看到的元素清單
        target (str)              : 要等的目標元素 (例如 "#submit")
        max_retry (int)           : 最多檢查幾次,預設 3
 
    回傳:
        (found, attempt_count) (tuple[bool, int]):
            found         : 有沒有找到
            attempt_count : 實際檢查的次數
    """
 
    # 實際能檢查的次數 = min(snapshots 長度, max_retry)
    # 因為就算 max_retry=10,但只有 4 張 snapshot,我們也只能檢查 4 次
    limit = min(len(snapshots), max_retry)
 
    attempt_count = 0   # 實際檢查的次數計數器
 
    for i in range(limit):
        attempt_count += 1                # 每進來一次就 +1
        current_snapshot = snapshots[i]   # 取出第 i 張 snapshot
 
        if target in current_snapshot:
            # 找到 target → 提早結束,回傳 True 和目前已檢查的次數
            return True, attempt_count
 
    # for 跑完都沒 return → 代表都沒找到
    return False, attempt_count