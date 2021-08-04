
# email模块构造邮件、smtplib模块复杂发送邮件
# SMTP是发送邮件的协议
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib

def send_email(msg):
    from_addr = '1157850031@qq.com'
    from_pass = 'kbniofyclhjsbabe' # 来自于邮箱 -> 设置 -> 账户 -> POP3/SMTP服务 开启后的授权码
    to_addr = '905421273@qq.com'
    smtp_server = 'smtp.qq.com' # qq邮箱服务地址, smtp加密协议的端口是465

    def _format_attr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg = MIMEText(msg, 'plain', 'utf-8')
    # 添加主题\发件人等,参考下图
    msg['From'] = _format_attr(u'mengtianxiang <%s>' % from_addr)
    msg['To'] = _format_attr(u'管理员 <%s>' % to_addr)
    # msg['To'] = '1157850031@qq.com, 905421273@qq.com'
    msg['Subject'] = Header(u'每日预报', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, from_pass)
    print(4)
    try:
        server.sendmail(from_addr, [to_addr], msg.as_string())
        print('邮件发送成功')
        return True
    except:
        print('邮件发送失败')
        return False

    server.quit()