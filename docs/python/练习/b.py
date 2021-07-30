# cookie免登逻辑
import requests
import json

url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# 除了log、pwd其他都是默认参数
data = {
    'log': 'kaikeba',
    'pwd': 'kaikeba888',
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}

session = requests.session()
session.post(url, headers=headers, data=data)

# 将生成的cookie转换成 字典
cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
# 将字典转换成 字符串
cookie_str = json.dumps(cookie_dict)

# 将cookie写入文件存起来
f = open('cookie.txt', 'w')
f.write(cookie_str)