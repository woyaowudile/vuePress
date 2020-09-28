## Es6简单介绍(不限于)

### 一. let、const
> ```js
>     {
>         let a = 1
>     }
>     console.log(a) // a is not defined
> ```
> |var|let|const|
> |:--|:--|:--|
> |变量声明提升|1.不会提升;<br>2.只在当前块级作用域生效|1，2同let，<br>3.已声明的变量不可修改|

### 二. 模板字符串
> ```js
> var str = '字'
> var str2 = `模板${str}符串`
> console.log(str2) // 模板字符串
> ```

### 三. 解构赋值
> ```js
> let o = {
>     a: 1,
>     b: 2,
>     c: 3
> }
> const { a, b, c } = o
> console.log(a, b, c) // 1, 2, 3
> ```
> 这种情况不好理解的话，可以参考下面import用法来理解
>> 
>> test.js
>> ```js
>> let a = 111, b = [1,2,3], c = function () {}
>> export {
>>   a, b, c
>> }
>> ```
>> main.js
>> ```js
>> import { a } from './test.js'
>> ```

### 四. 展开运算符
> 基本用法： 将一个变量中的所有元素添加到另一个变量中
> ```js
> var o1 = { a: 1, b:2, c:3}
> var o2 = {...o1}
> o1 === o2 // false
> ```
> 说明展开运算符可以完成浅拷贝
> ```js
> var o1 = { a: 1, b: 2, c: {d: 4}}
> var o2 = {...o1}
> o1.a = 11
> o1.c.e = 5
> console.log(o1) // { a: 11, b: 2, c: {d: 4, e: 5}}
> console.log(o2) // { a: 1, b: 2, c: {d: 4, e: 5}}
> ```
> 二级对象中修改就不行了，需要注意

### 五. 循环
> ```js
> var a = [1,2]
> a[4] = null
> a[5] = undefined
> console.log(a) // [1, 2, empty x 2, null, undefined]
> 
> // map
> a.map(x => x*2) // [2, 4, empty × 2, 0, NaN]
> // 由此了解： '(null相乘为0， undefined相乘NaN， empty相乘无变化)'
> 
> // filter
> a.filter(x => x*2) // [1, 2]
> 
> // reduce，map和filter的结合，功能更强，i是索引，arr就是a
> // 可做做累计运算，以下累乘，x初始为a[0]，y初始a[1]。
> // 第一次循环完了后，x变成了x*y = 2,y = a[2]...
> a.reduce( (x, y, i, arr) =>  x*y ) // NaN 
> 
> // flat 和filter相似，但是只能过滤empty。
> a.flat(x => x*2) // [1, 2, null, undefined]
> 
> // flat还可以扁平化数组，但只能有二级数组
> [1,2,3,[4,5]].flat() // [1,2,3,4,5]
> [1,2,3,[4,5,[6]]].flat() // [1,2,3,4,5,[6]]
> 
> // every
> [1,2,''].every( x => x) // false
> 
> // some
> [1,2,''].some( x => x) // true
> ```

### 六. async/awit
> ```js
> setTimeout( () => {
>   console.log('timeout') 
> }, 1000)
> console.log('start')
> // 先打印哪个，后打印哪个
> ```

<!-- <van-collapse v-model="2">
    <van-collapse-item title="标题1" name="1">内容</van-collapse-item>
</van-collapse> -->

### 七. class
