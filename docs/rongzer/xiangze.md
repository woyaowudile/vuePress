## 翔择项目中组件用法

<!-- <vant-notify :message="'新增 获取list中任意属性值， 详见第五条'" /> -->
<vant-notify :message="'添加 第四条: 升级版 的 属性options! 添加 第四条: 升级版 的 属性options! 添加 第四条: 升级版 的 属性options!'" />

### 一. tabContentSection结构
> length -------------------（Number）
> 
> title -------------------（String）
> 
> collapse -------------------（Boolean）
> 
> list -------------------（必， Array）
> 
>> message -------------------（String）
>>
>> array -------------------（必， Array）
>>> table：{} / formList: {} -------------------（Object）
>>
>> button -------------------（Object）
>>
>>> class -------------------（Object）
>>> 
>>> style -------------------（Object）
>>> 
>>> list -------------------（Array）
>>> 
> ```js
> // 结构一览
> tabcontent: {
>      data: {},
>      invokeSectionMethod: {}, // 必写
>      length: 0,
>      title: '工程踏勘_子公司',
>      collapse: true,
>      list: [
>          {
>              message: '踏勘信息',
>              unShow: true, // 当前踏勘信息是否显示，为true不显示(默认值为false)
>              // collapse: !options.tabcontent.collapse,
>              array: [
>                  {
>                      formList: {
>                          valueId: 'formListRef1',
>                          model: {},
>                          isViewMode: false,
>                          cols: 2,
>                          type: 'table',
>                          showChangeTip: true,
>                          labelWidth: 160,
>                          formItemList: [
>                              {
>                                  label: '例1',
>                                  type: 'input',
>                                  append: 'm²',
>                                  placeholder: '请输入',
>                                  name: 'x1',
>                                  validator: [
>                                      {
>                                          required: true,
>                                          message: '不能为空',
>                                          trigger: 'change'
>                                      }
>                                  ]
>                              },
>                              {
>                                  label: 'upload',
>                                  type: 'custom',
>                                  component: 'formUploadSection',
>                                  config: {  // 没有config默认是摄像头样式
>                                      defineWord: '上传文件',
>                                  },
>                                  name: 'x2'
>                              },
>                          ]
>                      }
>                  }
>              ],
>              button: {
>              }
>          },
>          {
>              message: '踏勘分析',
>              array: [
>                  {
>                      table: {
>                          valueId: 'tableRef1',
>                          localData: [
>                              {
>                                  y1: '11111',
>                              }
>                          ],
>                          columns: [
>                              {
>                                  title: '操作',
>                                  buttons: [
>                                      {
>                                          name: '查看',
>                                          onClick: 'on-preview'
>                                      },
>                                  ]
>                              },
>                              {
>                                  title: '例2',
>                                  key: 'y1'
>                              },
>                          ]
>                      }
>                  }
>              ],
>              button: {
>                  style: {
>                      'text-align': 'right',
>                      margin: '5px 0px',
>                      position: 'absolute',
>                      right: 0,
>                      top: '-0'
>                  },
>                  list: [
>                      {
>                          name: '添加',
>                          type: 'default',
>                          size: 'default',
>                          onClick: 'on-add'
>                      },
>                  ]
>              }
>          },
>      ]
>  }
> ```

### 二. 例子
> <image-preview :imgUrl="'tableContentSection1.png'" />
>> <image-preview :imgUrl="'code1.png'" />
***
> <image-preview :imgUrl="'tableContentSection2.png'" />
>> <image-preview :imgUrl="'code2.png'" />
***
> <image-preview :imgUrl="'tableContentSection3.png'" />
>> <image-preview :imgUrl="'code3.png'" />
> list数组中每项有collapse，是控制'踏勘信息'、'踏勘分析'这种小类的收起、展开。<br>
> 而list数组同级的collapse，控制'工程踏勘_子公司'这种大类的
:::warning
> 注意：

  array中，每个formList / table 都应该有个 唯一的 valueId， 例如：
  > <image-preview :imgUrl="'valueId.png'" />
  > 名字可以自定义，和下文startValidate一起使用
:::

### 三. 获取 formList / table 的值
<br>

:::tip

  ```js
  main: {
    tabcontent: {
      data: {},
      invokeSectionMethod: {},
      title: '工程踏勘_子公司',
      collapse: true,
      list: [
        {
          array: [ {} ]
        }
      ]
    }
  }
  // 新增属性： data、 invokeSectionMethod

  // 注：每个formList、table都必须有一个valueId, 例如： array[0].formList.valueId = 'formRef1'

  /*******************如果没有valueId，就会忽略******************/
  /*******************如果没有valueId，就会忽略******************/
  /*******************如果没有valueId，就会忽略******************/

  options.main.tabcontent.invokeSectionMethod = {
      type: 'table', // 'table', 'formList', 'all'， 默认'all'
      ref: 'tableRef1', // 唯一标识id, 即array每项中的valueId
      name: 'reload', // noco上的方法
      status: 'save', // 'save', 'submit'（必要参数），且submit使用formList
      params: {}, // 参数 （例如table下，name为reload时刷新表格）
      callback: () => {} // function：回调函数
  };
  // 例如：
  options.main.tabcontent.invokeSectionMethod = {
      // 默认不写type和 type: all时一个意思。获取所有table、formList
      status: 'save',
  };
  options.main.tabcontent.invokeSectionMethod = {
      // 将所有table表格的值取出来
      type: 'table',
      status: 'save',
  };
  options.main.tabcontent.invokeSectionMethod = {
      // 将table表格中为tableRef1的值取出来
      type: 'table',
      ref: 'tableRef1',
      name: 'getTableData'
      status: 'save',
  };

  // 取出来的值放在options.main.tabcontent.data中

  ```

:::

### 四. 升级版
> 因为options.main.tabcontent.invokeSectionMethod 赋值给data 的操作是异步的，实际应用会麻烦
> 
> 所以 又写了个通用方法: 
```js
// 两个参数： 
// 第一个（新增）： options, 目标，例如：options.main.tabcontent
// 第二个： 对象，用法和第三条一样， status必传，
// 第三个：this，在vue文件中用this, 在js文件中用vm

vm.$methodsJs.invokeSectionMethod(options, {status: 'save'}, this)
```
```js
// 子页面
// 用法和之前一样，将methods导出去
let events = {
    $page: {
        'on-ready'(next) {
            vm.litOptions.methods = methods;
            next && next();
        }
    },
    main: {
        'on-back': () => {},
        oninit1() {}
    }
};
let methods = {
    save() {
        // 之前
        // options.main.tabcontent.invokeSectionMethod = {
        //     // 默认不写type和 type: all时一个意思。获取所有table、formList
        //     status: 'save',
        //     callback: () => {}
        // };

        // 现在
        return vm.$methodsJs.invokeSectionMethod(options, {status: 'save'}, vm);
    }
};
```
```js
// 父页面
// 逻辑自己写, 重点是调用 vm.litOptions.methods.save 方法后
// 返回的res是一个 promise 对象, 可以 .then的形式 获取 数据
let events = {
    main: {
        'on-save': () => {
            let o = vm.$methodsJs.getListAttr(options.main.tabcontent, '_this', 'flag');
            o.tabs.map( (v, i) => {
                if (!v.litOptions.methods.save) {return;}
                let res = v.litOptions.methods.save();
                res.then( v => {
                    console.log('reslove1111', v);
                });
            });
        },
        'on-reset': () => {},
        'on-submit': () => {},
    }
};
```
> <image-preview :imgUrl="'invokeSectionMethod.jpg'" />

### 五. 赋值给formList中某项

> <image-preview :imgUrl="'setFormValue.png'" />
> 代码如下：
<!-- > <image-preview :imgUrl="'setFormValue2.png'" /> -->

>```js
>let events = {
>  // 1. 先获取table表格数据
>  main: {
>    'on-click': () => {
>      let o = {
>          type: 'table',
>          ref: 'dataRef1',
>          name: 'getTableData',
>          status: 'save'
>      };
>      options.main.invokeSectionMethod = {
>          ...o,
>          // fn: methods.fn(o.ref)
>          callback: methods.fn
>      };
>    }
>  }
>}
>
>let methods = {
>    fn() {
>        // 2. 遍历去到的数据累加
>        let res = options.main.data['dataRef1'].reduce( (x, y) => {
>            return（x.age5 || 0) / 1 + (y.age5 / 1 || 0);
>        });
>        // 3. 将累加的值 赋值给某项
>        vm.$methodsJs.setFormValue({
>           list: options.main.list, // (必要)
>           ref: 'formListRef1', // (必要)
>           model: 'ownerLinkMan',  // (见下)
>           res: res, // (必要)
>       });
>    }
> };


 上面说过了挂载公共方法到methodsJs上（见上一章最后）
 
 <span style="color: #a1b5a8">setFormValue这个方法的四个参数可以理解为：</span>
 
 <span style="background: #fff1f1;padding: 5px;">找到invokeSectionMethod属性同级的list中，一个valueId叫 formListRef1 的表单，将这个表单参数model中的  ownerLinkMan 的值 修改成 传入的值 res。<br>
 <strong>如果参数model没写，则res赋值给整个model</strong>
 <strong>如果参数model赋值其中两个， model: ['ownerLinkMan1', 'ownerLinkMan2']</strong>
 </span>

<strong style="color:red">注意：</strong> 
:::danger
 因为使用 options.main.invokeSectionMethod --
 ----- 将获取的值，放在 options.main.data 是异步操作， --
 ----- 所以有两种写法： --
 ----- 1. 将方法写在callback中
 ----- 2. this.$nextTick( () => { ... })
:::

 

### 六. 获取list中含有指定属性的对象
```js
let options = {
    main: {
        tabcontent: [
            {
                title: '立项申请',
                collapse: true,
                list: [
                    {
                        array: [
                            {
                                tab: {
                                    current: 'tab1',
                                    tabs: [
                                        {
                                            label: '审批结果',
                                            page: 'designResultPage',
                                            name: 'tab1',
                                            litOptions: {
                                              methods: {}
                                            },
                                        },
                                        {
                                            label: '项目基本信息',
                                            page: 'applicationInfoPage',
                                            name: 'tab2',
                                            litOptions: { }
                                        },
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
};
// > 现在要获取 litOptions 中 methods的值
// > 正常写法： options.main.tabcontent[0].list[0].array[0].tab.tabs[0].litOptions.methods
// > 使用全局方法：vm.$methodsJs.getListAttr(options.main.tabcontent, 'tab1');
// > 返回当前属性所在对象， 即： 
// {
//     label: '审批结果',
//     page: 'designResultPage',
//     name: 'tab1',
//     litOptions: {
//       methods: {}
//     },
// },
// > 默认查找name属性， 如果要找label，则
// > vm.$methodsJs.getListAttr(options.main.tabcontent, '审批结果', 'label');

```
:::tip
应用：<br>
> <image-preview :imgUrl="'getListAttr1.png'" />
> 
> 
> 点击暂存按钮，这时候需要获取 开工报告、工程保修....页面的数据

```js
//  在开工报告子页面中，将方法给litOptions
let events = {
    $page: {
        'on-ready'(next) {
            vm.litOptions.methods = methods['testMethod'];
            // vm.litOptions.methods.testMethod = methods['testMethod'];
            // vm.litOptions.methods.testMethod1 = methods['testMethod1'];
            next && next();
        }
    },
};
let methods = {
    'testMethod'() {
        console.log('this is tabs methods');
    },
    'testMethod1'() { },
};

// 在父页面中
let events = {
    main: {
      // 暂存按钮save方法
        'on-save': () => {
            let a = vm.$methodsJs.getListAttr(options.main.tabcontent, 'tab1');
            a.litOptions.methods()
            // a.litOptions.methods.testMethod()
        },
    }
};
```
:::

### 七. 样式设置
> <image-preview :imgUrl="'setClassName1.jpg'" />
> 一般只有厨房图纸设计 这一个可以折叠大类， 现在要求有两个大类
> <image-preview :imgUrl="'setClassName-code1.jpg'" />

```js
layout: {
    componentList: [
        {
            type: 'section',
            name: 'kitchenDesignWrap',
            componentList: [
                {
                    name: 'topInfo',
                    component: 'topInfoSection'
                },
                {
                    type: 'section',
                    class: '', // 
                    componentList: [
                        {
                            name: 'main',
                            component: 'publicSection'
                        },
                        {
                            name: 'ex1',
                            component: 'publicSection'
                        }
                    ]
                }
            ]
        }
    ]
},
```