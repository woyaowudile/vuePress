### js方法一览

```js
/**
 * 判断数据类型
 */
function istype(value) {
    return Object.prototype.toString.call(value).slice(8, -1);
}
/** *****************************E_N_D********************************** */

/**
 * 创建新类
 */
class CLASSCOST {
    constructor() {
        return JSON.parse(JSON.stringify([...arguments]));
    }
}
/** *****************************E_N_D********************************** */


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


// 深克隆
function changeJson(res) {
    let o = JSON.parse(JSON.stringify(res));
    return o;
}
/** *****************************E_N_D********************************** */

```

```js
// 使用 async await
function getApi(o = { api: '', data: {}, headers: {}, notShow: false,  callback: callback}, _this) {
    if(!notShow) {
      // vant用提示加载, 可根据使用的更改
        vant.Toast.loading({
            mask: true,
            message: '加载中...',
            duration: 0
        });
    }
    return new Promise(resolve => {
        _this.$dataSource({
            api: o.api,
            params: o.data,
            headers: {
                ...o.headers
            },
            success: res => {
                callback && callback();
                resolve(res);
            },
            fail: err => {
                resolve(err);
            }
        });
    });
}

function getApiRes(res, _this) {
    if (!(res && res.success)) {
      // iview用提示, 可根据使用的更改
        _this.$Message.config({
            top: 50,
            duration: 3,
            content: res && res.errorMessage || '调用失败'
        });
        return true;
    }
}

/** *****************************E_N_D********************************** */


/** *********************翔择用，其他使用可更改************************** */
// 对 form 中某项属性赋值
function setFormValue(o = { list: [], ref: '', model: '', res: {} }) {
    for (let i = 0; i < o.list.length; i++) {
        let v = o.list[i].array;
        if (!(v instanceof Array)) {
            continue;
        }
        for (let k = 0; k < v.length; k++) {
            let d = v[k].formList;
            if (d && d.valueId === o.ref) {
                if (!d.model) {
                    d.model = {};
                }
                if (!o.model) {
                    d.model = o.res;
                    return;
                }
                let obj = o.model;
                if (!(obj instanceof Array)) {
                    obj = [o.model];
                }
                obj.map(x => {
                    d.model[x] = o.res[x];
                });
            }
        }
    }
}

// 获取 list 中唯一含有属性res的那个对象
function getListAttr(list, res, attr = 'name') {
    if (typeof list !== 'object' && list === res) {
        return list;
    }
    if (list instanceof Object || list instanceof Array) {
        for (let k in list) {
            if (list[k]['invokeSectionMethod']) {
                // 这里的if 判断 是为了invokeSectionMethod这个方法用的，没有其他用途
                list[k][attr] = JSON.stringify(list[k][attr]);
            }
            if (list[k][attr] === res) {
                return list[k];
            }
            if (!list[k][attr] && (list[k] instanceof Object || list[k] instanceof Array)) {
                let req = getListAttr(list[k], res, attr);
                if (req) {
                    return req;
                }
            }
        }
    }
}

function invokeSectionMethod(
    o = {
        type: 'all',
        ref: '',
        name: '',
        status: 'save',
        params: {},
        callback: () => {}
    },
    _this
) {
    let options = _this.options;
    let res = getListAttr(options, '{}', 'invokeSectionMethod');
    res.invokeSectionMethod = {
        ...o
    };
    return new Promise((reslove, reject) => {
        _this.$nextTick(() => {
            if (options.main.data) {
                reslove(options.main.data);
            }
        });
    });
}

/** *****************************E_N_D********************************** */

// uuid
function getUuid() {
    function S4() {
        return ((1 + Math.random()) * 0x10000 | 0).toString(16).substring(1);
    }
    return S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4();
}
```