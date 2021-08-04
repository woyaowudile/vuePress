from gevent import monkey
monkey.patch_all()


import gevent, time, requests
from gevent.queue import Queue
from bs4 import BeautifulSoup

import openpyxl

work = Queue()

url = 'https://book.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

page = 25
size = 10
for i in range(page):
    params = {
        'start': size * i 
    }
    work.put_nowait(params)

def crawler():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '豆瓣读书排行榜'
    sheet.append(['书名，作者', '评分'])
    
    while not work.empty():
        
        params = work.get_nowait()
        res = requests.get(url, headers=headers, params=params)
        res.encoding='utf-8'

        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        names = soup.find_all('div', class_='pl2')
        rates = soup.find_all('div', class_='star')
        str = '豆瓣读书排行榜：\n'
        for i in range(len(names)):
            name = names[i].text.replace(' ', '').replace('\n', '')
            rate = rates[i].text.replace(' ', '').replace('\n', '')
            # str = str + name + '：' + rate + '\n'
            sheet.append([name, rate])
    # return str
    wb.save('qoueue.xlsx')
    wb.close()

crawler()
