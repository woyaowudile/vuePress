# require 和 import

## require
```js
// js
const list = [1,2,3]
let a = false

// 1
moudle.exports = {
    ...list,
    a
}
// 2
exports.list1 = list
exports.a = a

// 文件中引入
const res = require(./xxx.js)
// 1.
console.log(res) // { list:[1,2,3], a: false }
// 2
console.log(res) // { list1:[1,2,3], a: false }
```

## import
```js
const list = [1,2,3]
let a = false

export default = {
    list,
    a
}
export { list }

// 文件中引入
import res, { a } from './xxx.js'
console.log(res, a) // { list: [1,2,3], a: false }, false
```

:::tip
上面的都是以对象形式导出，exports可以重新定义名称<br/>
下面的可以写在一起，但只有export才可以有按需导入的形式
:::