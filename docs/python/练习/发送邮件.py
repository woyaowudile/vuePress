# -*- coding: UTF-8 -*-

to_addr = []
while True:
    to_addr.append(input('请输入收件人邮箱地址To: '))
    num = input('是否继续添加收件人: 1. 是， 2. 否')
    print(num == 2)
    if num == 2:
        break;
1

print(to_addr)