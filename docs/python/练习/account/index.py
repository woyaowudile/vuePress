import csv #引入csv模块
import math #引入math模块
from kkb_tools import open_file
#获取用户输入的贷款总额与贷款年限
# total_loan = int(input('请输入贷款总额（贷款总额为整数）：'))

#调用open()方法，文件名是detaillist.csv，追加模式"a", 文件名在代码中称为listfile
with open("detaillist.csv","a",newline='',encoding='GBK') as listfile:
    #使用csv.writer（）函数创建writer对象，用于写入
    writer = csv.writer(listfile, dialect='excel')
    #列表头部第一行的字段
    header = ['期次','偿还本息（元）','偿还本金（元）','偿还利息（元）']
    # 使用writer对象写入表头
    writer.writerow(header)
    #循环计算所有月份的数据
    for i in range(1, 5):
        writer.writerow(['a'+i, 'b'+i, 'c'+i, 'd'+i])
    #累计利息
    #累计字段
    total_header = ['总期次', '累计还款总额', '所借本金', '累计支付利息']
    # 使用writer对象写入表头
    writer.writerow(total_header)
open_file("detaillist.csv")