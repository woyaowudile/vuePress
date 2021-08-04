
import requests
from bs4 import BeautifulSoup

def get_weather(code):
    url = 'http://www.weather.com.cn/weather/'+ code +'.shtml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    
    res = requests.get(url, headers=headers)
    res.encoding='utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    
    title = soup.find('div', class_='ctop')
    box = soup.find_all('li', class_='skyid')
    str = title.text.replace(' ', '').replace('\n', '') + '\n'
    str = str.split('>')[2] + ':\n'
    for i in box:
        str = str + (i.text.replace(' ', '').replace('\n', '') + '\n')
    
    print(2)
    return str
    # print(str)



def get_movie():
    url = 'https://movie.douban.com/chart'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    
    res = requests.get(url, headers=headers)
    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div', class_='pl2')
    str = '最新电影：\n'
    for i in div:
        a = i.find('a').text.replace(' ', '').replace('\n', '')
        rate = i.find('div', class_='clearfix').text.replace(' ', '').replace('\n', '')
        str = str + a + '：' + rate + '\n'
    # print(str)
    print(5)
    return str
