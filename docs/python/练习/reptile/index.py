# 豆瓣电影排名： 名称 + 评分
import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
res = requests.get('https://movie.douban.com/chart', headers=headers)
html = res.text

soup = BeautifulSoup(html, 'html.parser')
cont = soup.find_all('div', class_='pl2')

for item in cont:
    name = item.find('div', class_='clearfix').text.replace(' ', '').replace('\n', '')
    a = item.find('a').text.replace(' ', '').replace('\n', '')
    print(a + ' : ' + name)


