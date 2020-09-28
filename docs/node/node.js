var http = require('http')

http.createServer((request, response) => {
    response.writeHead(200, { 'Content-Type': 'text/plain' })

    response.end('hello, node')
}).listen(12306)

console.log('service ip is http://127.0.0.1:12306');