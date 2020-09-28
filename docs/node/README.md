# node的使用

> `点击👇编辑代码`
> <Node-Edit />
> `例如：启动服务后，将下面html的代码复制进来，更改ip后点击按钮`


## 一. hello node
```js
var http = require('http')

http.createServer((request, response) => {
    response.writeHead(200, { 'Content-Type': 'text/plain' })

    response.end('hello, node')
}).listen(12306)

console.log('service ip is http://127.0.0.1:12306');
```

## 二. 创建第一个服务
```js
let  http = require('http')
let express = require('express')
let app = express()

app.listen('6192', () => {
    console.log('http://127.0.0.1:6192  service is running...')
})

app.get('/first', (req, res) => {
    // res.query: ?  res.params: /
    res.json('第一个接口返回值！')
})
```
> 在html中调用
```html
var xhr = new XMLHttpRequest()
xhr.open('get', 'http://127.0.0.1:6192/first?a=1', true)
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr)
    }
}
xhr.send()
```
> 跨域
```js
// 设置跨域请求头
app.all('*', function (req, res, next) {
    // 允许跨域的ip， * 表示全部
    res.header("Access-Control-Allow-Origin", "*");
    // 判断客户端的请求是Ajax请求还是其他请求，X-Requested-With: null 传统同步请求，XMLHttpRequest ajax请求，见下图
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
    next();
})
```
> X-Requested-With
> <image-preview :imgUrl="'node/X-Requested-With.png'" width="200" height="200" />

## 三. 调试代码
> 1.cmd中运行 node --inspect xxxx
> <image-preview :imgUrl="'node/debugger-start.png'" width="400" height="200" />
> 2.打开浏览器控制台，点击绿色六边形
> <image-preview :imgUrl="'node/debugger-check.png'" width="400" height="200" />
