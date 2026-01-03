import random


def mock_api_request():
    """
    模擬 API 請求的回傳狀態。
    回傳值：'200 OK' (成功) 或其他錯誤訊息。
    """
    # 這裡可以調整機率，例如 200 OK 出現機率高一點
    return random.choice(["200 OK", "500 ERROR", "404 NOT FOUND"])
