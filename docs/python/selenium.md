# selenium

## 一. selenium是什么
> 我们可以通过它来控制浏览器，做出自动打开、输入、点击等操作，就像是有一个真正的用户在操作一

## 二. selenium怎么用
> 1. 安装：pip3 install selenium
> 2. 下载：https://npm.taobao.org/mirrors/chromedriver/ 

### 1. 自动打开浏览器
```py
from selenium import webdriver
import time
# 下载解压后移动到python对应的文件夹中，或指定位置
# 例如： webdriver.Chrome('C:/Python36-32/chromedriver.exe')
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
time.sleep(5)
# 使用后手动关闭，不然占内存资源
driver.close()
```
> <image-preview imgUrl="python/selenium1.png" width='200'></image-preview>

### 2. WebElement
```py
label = driver.find_element_by_class_name('s-bottom-layer-content')
# label = driver.find_element_by_id('bottom_layer')
# label = driver.find_element_by_tag_name('p')
# label = driver.find_element_by_link_text('京公网安备11000002000001号')
# label = driver.find_element_by_partial_link_text('京公网')
print(type(label)) # <class 'selenium.webdriver.remote.webelement.WebElement'>

# 获取链接的两个方法没有获取到链接，只拿到了内容
# find_elements_by_class_name获取多个
```
> <image-preview imgUrl="python/selenium-diff.png" width='200'></image-preview>

### 3. 获取网页源代码
> 使用区别
```py
# selenium
label = driver.page_source

# BeautifulSoup
res = requests.get('xxxxx')
html = res.text
label = BeautifulSoup(html, 'html.parser')
```

### 4. 自动登录
```py
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://xiaoke.kaikeba.com/example/X-Man/')
# 注意，打开网页的时候会有加载过程。延时可根据情况设定
time.sleep(5)

teacher = driver.find_element_by_class_name('form-teacher')
teacher.send_keys('小K老师')

assistant = driver.find_element_by_class_name('form-assist')
assistant.send_keys('都喜欢')

time.sleep(2)

button = driver.find_element_by_id('submit')
button.click()

time.sleep(5)
driver.close()
```
> <image-preview imgUrl="python/selenium-click.png" width='200'></image-preview>

### 5. 设置静默模式
```py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Otions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
```