# -*- coding: UTF-8 -*-

# 构造右键 相关模块
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
# 发送邮件
import smtplib

from_addr = '1157850031@qq.com'
from_pass = 'unjgalcmecehggbf' # 来自于邮箱 -> 设置 -> 账户 -> POP3/SMTP服务 开启后的授权码
to_addr = '905421273@qq.com'
smtp_server = 'smtp.qq.com' # qq邮箱服务地址, smtp加密协议的端口是465

def _format_attr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText('hello python: send email', 'plain', 'utf-8')
msg['From'] = _format_attr(u'mengtianxiang <%s>' % from_addr)
msg['To'] = _format_attr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'先试一下发给个人的邮件', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, from_pass)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()