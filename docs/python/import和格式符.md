# import

## 延时用法
```python
import time
time.sleep(2) # 2s
```

## 随机数
```python
import  random
random.randint(1, 100)  # 1-100 包含1和100
```

## 格式符
```python
# %s 格式化字符串
# %f  浮点数
# %d 整数
print('字符串%s 小于 %d' %( '100', 9999))
print('{} 小于 {}'.format(100, 2000))
print('{0} 小于 {1}'.format(200, 3000))
print('{pre} 小于 {next}'.format(next=8888, pre=300))
```

## import 、import .. as ..、 from...import
```python
import index
index.init()

# 多文件引入
import x,y,z
x.init()
y.init()
z.init()

import index as inx
inx.index()

# 按需引入
from index import init,init2,init3
init()
init2()
init3()
```

## 拓展
```python
# 表示当前文件是最终的文件入口，则运行里面的代码
if __name__ == '__main__':
	init()

# 例：a.py、b.py、index.py
# index.py
def init:
	print('init')

# b.py
import index
print('b.py')
if __name__ == '__main__':
	index.init()

# a.py
import b # 这时 只能打印出'b.py',因为现在的'__main__'是 a.py
```

## csv模块
```python
import csv
# 版本2.7.16报错encoding。 可引入模块io，io.open(...)其他不变，即可；或者不使用encoding
with open('./test.csv', encoding='utf-8-sig') as r:
	print '内容如下\n'
	reader = csv.reader(r)
	for i in reader:
		print(i)

with open('./test.csv', 'a') as r:
	writer = csv.writer(r)
	for i in [[11,12,13], [21,22,23], [31,32,33]]:
		writer.writerow(i)
```

## time 模块
```python
import time;  # 引入time模块

#时间戳   每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
ticks = time.time()
print ("当前时间戳为:", ticks)  # 1605255540.484838

#本地时间  从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localtime = time.localtime()
print ("本地时间为 :", localtime) # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=13, tm_hour=16, tm_min=19, tm_sec=0, tm_wday=4, tm_yday=318, tm_isdst=0)

#根据需求选取时间格式
localtime = time.asctime()
print ("本地时间为 :", localtime) # Fri Nov 13 16:19:00 2020

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S") ) # 2020-11-13 16:23:52

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y") ) # Fri Nov 13 16:23:52 2020

# 将格式字符串转换为时间戳    和 time.time()的区别在于小数位
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))) # 1459175064.0
```

## 邮件
```python
# email模块构造邮件、smtplib模块复杂发送邮件
# SMTP是发送邮件的协议
from email.mime.text import MIMEText
import smtplib

msg = MIMEText('邮件的内容', 'plain', 'utf-8') # MIME的subtype: text/plain两种

# 1. 获取邮箱地址、端口，QQ邮箱SMTP服务器地址：smtp.qq.com, 端口465, QQ邮箱默认的端口是25,这里使用的是加密端口465。
server = smtplib.SMTP_SSL('邮箱供应方的地址', '端口(int型)')
server.set_debuglevel(1) # 调试级别： 1就可以打印出和SMTP服务器交互的所有信息。
# 2. 发件人登录邮箱
server.login('发件人邮箱地址', '密码')
# 3. 发送
server.sendmail('发件人的邮箱地址', ['收件人的邮箱地址'], msg.as_string()) # 将msg的邮件内容MIMEText对象变成str。
# 4. 完成退出
server.quit()

# 问题总结：
# 1. SMTPAuthenticationError: STMP服务未开启，需要到邮箱中设置
```