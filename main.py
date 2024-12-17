import requests
import json
import time
from datetime import datetime


# 把这里的xxxxx改成自己的paper id，比如1234
url = "https://cmt3.research.microsoft.com/api/odata/ICASSP2025/Submissions(xxxxxx)"

# 把这里的xxxxx改成自己的cookie，具体填什么看readme
cookies = {
    "Cookie": "xxxxx"
}

# 可选：自定义 HTTP 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

while True:
    try:
        # 发送 GET 请求，携带 Cookie
        response = requests.get(url, cookies=cookies, headers=headers, timeout=10)

        if response.status_code == 200:
            res = json.loads(response.text)
            print(f"{datetime.now()}, 当前论文状态: { res['StatusId'] }")
        else:
            print(f"请求失败，HTTP 状态码：{response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误：{e}")
    
    time.sleep(60)
