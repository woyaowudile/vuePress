### js方法一览

```js
/**
 * 判断数据类型
 */
function istype(value) {
    return Object.prototype.toString.call(value).slice(8, -1);
}
/** *****************************E_N_D********************************** */
```

```js
/**
 * 创建新类
 */
class CLASSCOST {
    constructor() {
        return JSON.parse(JSON.stringify([...arguments]));
    }
}
/** *****************************E_N_D********************************** */
```


```js
// 将 数组对象 的键值， 重新赋值到 一个 规定的 键值组 中去
// 例如 from: [ {a:1,b:2}, {a:11,b22}] --> to: {a:''} ----> return:  [{a:1},{a:11}][0] --{a:1}
function changBean(from, to, isObj = true, index = 0) {
    /**
     *  from 为数组， to为对象, 
     *  默认返回值 是 对象，取值第一条。即： {a:1}
     *  如果需要返回的数组，可以 isObj = false
     */
    let o = [];
    from.map( (v, i) => {
        o[i] = {};
        for (let k in to) {
            o[i][k] = v[k];
        }
    });
    return isObj ? o[index] : o;
}
/** *****************************E_N_D********************************** */
```


```js
// 深克隆
function changeJson(res) {
    let o = JSON.parse(JSON.stringify(res));
    return o;
}
/** *****************************E_N_D********************************** */
```

```js
// uuid
function getUuid() {
    function S4() {
        return ((1 + Math.random()) * 0x10000 | 0).toString(16).substring(1);
    }
    return S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4();
}
/** *****************************E_N_D********************************** */
```

```js
/**
 * 递归
 * 1. 两个数组，一个树结构带children, 一个长度为3的数组
 * 2. 匹配两个数组，后一数组中的值，匹配到树结构中
*/
let deepMap = function(list, item) {
    list.forEach((v, i) => {
        if (v.id === item.itemId) {
            // 正常逻辑是，只需要修改判断条件，和这里的赋值即可
            v.detailAmount = item.detailAmount;
            v.detailNum = item.detailNum;
            v.detailPrice = item.detailPrice;
            v.custom_id = item.id;
        } else {
            if (v.children && v.children.length > 0) {
                v.children = deepMap(v.children, item);
            }
        }
        /*
         * todo:
         *   处理children, 以达到从底层往外层处理的效果
        */
    });
    return list;
};
let result = [];
arr.forEach((d, k) => {
    result = deepMap(treeArr, d);
});
/** *****************************E_N_D********************************** */
```
::: tip 提示
当然了， 如果需要将子级的某项值相加后赋值给父级这种需求，就可在todo处处理children
:::
