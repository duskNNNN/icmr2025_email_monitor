# icmr2025_monitor
ICMR20252025 论文状态监控小脚本 \
参考网址：https://github.com/liuup/icassp_monitor \
2 -> 论文接收  \
3 -> 论文拒绝  \
其他状态码 -> 还在审  \

所有状态码定义在 https://cmt3.research.microsoft.com/api/odata/ICMR2025/SubmissionStatuses

# 步骤
1. 用浏览器登录官方的cmt系统 https://cmt3.research.microsoft.com/ICMR2025/Submission/Index

2. 用浏览器打开接口 https://cmt3.research.microsoft.com/api/odata/ICMR2025/Submissions(xxxx) 这里的xxxx换成自己的论文id，比如1234

3. 在接口的界面按键盘F12打开网页调试器，刷新一下界面，打开Submissions(xxxx)的接口
   <img width="533" alt="image" src="https://github.com/user-attachments/assets/6d92cbad-f59f-4fad-8b0a-6c0ced41d8ac" />

4. 把右边的Cookie这一坨复制到main.py的代码中
   <img width="1135" alt="image" src="https://github.com/user-attachments/assets/17b357a0-86aa-42ca-b9a7-dfde868b6439" />

5. 下载本项目，修改main.py，把第8行的paper_id改成自己的论文id，把第10行修改成自己的cookie，
   将第12行的email换成自己的邮箱，将第14行的sender_email换成往你邮箱发送的邮箱名，
   将第15行的password改成邮箱对应的密码（此处需要开启对应邮箱的IMAP/SMTP服务），
   第59行的xxx换成公共服务的域名（比如163邮箱：smtp.163.com）

6. 运行`python main.py`

