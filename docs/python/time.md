# 定时任务

## 一. 邮件
```python

# email模块构造邮件、smtplib模块复杂发送邮件
# SMTP是发送邮件的协议
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib

def send_email():
    from_addr = '11xxxxx1@qq.com'
    from_pass = 'abcdefghigklmnopqrstuvwxyz' # 来自于邮箱 -> 设置 -> 账户 -> POP3/SMTP服务 开启后的授权码
    to_addr = '90xxxxxx3@qq.com'
    smtp_server = 'smtp.qq.com' # qq邮箱服务地址, smtp加密协议的端口是465

    def _format_attr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg = MIMEText('hello python: send email', 'plain', 'utf-8')
    # 添加主题\发件人等,参考下图
    msg['From'] = _format_attr(u'mengtianxiang <%s>' % from_addr)
    msg['To'] = _format_attr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'先试一下发给个人的邮件', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, from_pass)
    try:
        server.sendmail(from_addr, [to_addr], msg.as_string())
        print('邮件发送成功')
        return True
    except:
        print('邮件发送失败')
        return False
        
    server.quit()

# 问题总结：
# 1. SMTPAuthenticationError: STMP服务未开启，需要到邮箱中设置
```
<image-preview imgUrl="python/send-email-1.png" width='200'></image-preview>

## 二. schedule模块
> 安装 pip3 install schedule

```py
import schedule
#部署每10分钟执行一次job()函数的任务
schedule.every(10).minutes.do(job)
#部署每×小时执行一次job()函数的任务
schedule.every().hour.do(job)
#部署在每天的10:30执行job()函数的任务
schedule.every().day.at("10:30").do(job)
#部署每个星期一执行job()函数的任务
schedule.every().monday.do(job)
#部署每周三的13：15执行函数的任务
schedule.every().wednesday.at("13:15").do(job)
```

## 三. 定时发送邮件
```py
import time
import schedule

import requests
from bs4 import BeautifulSoup

# email模块构造邮件、smtplib模块复杂发送邮件
# SMTP是发送邮件的协议
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib



def init1():
    # get_weather、get_movie 在爬虫页
    msg = get_weather('101181001') # 101181001商丘
    msg = msg + '\n' +  get_movie()
    send_email(msg)


schedule.every().day.at('09:14').do(init1)

while True:
    schedule.run_pending()

    time.sleep(3)
```