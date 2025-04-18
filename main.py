import requests
import json
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
paper_id = "xxx"
cookies  = {
    "Cookie": "xxx"
}
email = "xxx"

sender_email = "xxx"
password = "xxx"  

def get_status_id(paper_id,cookies,email_id,flag):
    url = f"https://cmt3.research.microsoft.com/api/odata/ICMR2025/Submissions({paper_id})"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    try:
        # 发送 GET 请求，携带 Cookie
        response = requests.get(url, cookies=cookies, headers=headers, timeout=10)

        if response.status_code == 200:
            res = json.loads(response.text)
            print(f"{datetime.now()}, 当前论文{paper_id}状态: { res['StatusId'] }")
            status_id = res['StatusId']
            if flag is False and status_id != 1:
                mailer_send( status_id,email_id )
                flag = True
                return flag
            if flag is True and status_id == 1:
                mailer_send( status_id,email_id )
                flag = False
                return flag
        else:
            print(f"请求失败，HTTP 状态码：{response.status_code}")
            return flag

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误：{e}")

def mailer_send(status_id,reciver_email):
    message = MIMEMultipart()
    message["Subject"] = "论文结果出炉！！！"
    message["From"] = sender_email
    message["To"] = reciver_email
    if status_id == 1:
        body = "坏了，状态重置了!!!"
    elif status_id == 2:
        body = "恭喜录用!!!"
    elif status_id == 3:
        body = "下次加油!!!"
    message.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP_SSL("xxx", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciver_email, message.as_string())
            print("✅ 群发邮件成功！")
    except Exception as e:
        print(f"❌ 发送失败：{e}")    


def main():
    flag = False
    while True:
        flag = get_status_id(paper_id,cookies,email,flag)
        time.sleep(60)
        
main()