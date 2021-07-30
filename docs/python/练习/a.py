# -*- coding: UTF-8 -*-

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('邮件的内容', 'text/plain', 'utf-8') # MIME的subtype: text/plain两种

# 1. 获取邮箱地址、端口，QQ邮箱SMTP服务器地址：smtp.qq.com, 端口465, QQ邮箱默认的端口是25,这里使用的是加密端口465。
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.set_debuglevel(1) # 调试级别： 1就可以打印出和SMTP服务器交互的所有信息。
# 2. 发件人登录邮箱
server.login('905421273@qq.com', 'mengtx611992')
# 3. 发送
server.sendmail('905421273@qq.com', ['1157850031@qq.com'], msg.as_string()) # 将msg的邮件内容MIMEText对象变成str。
# 4. 完成退出
server.quit()