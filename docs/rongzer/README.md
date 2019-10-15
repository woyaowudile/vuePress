
### 翔择平台管理项目

***
#### 1. gitlab下载代码
`http://192.168.1.226/xiangze/sims-cpm-platform-web.git`

---
#### 2. 下载node_modules
`npm i --registry=https://registry.npm.taobao.org`
:::tip
这个和指不指向到淘宝镜像没有关系，即使你已经指向了，安装时也得用全
:::

---
#### 3. 启动项目
`npm run start`

---
#### 4. 打包
`npm run build`

---
#### 5. 校验代码
`npm run lint`

---
#### 6. 目录结构
> src
>> pages // 所有页面存放位置，页面注册在当前文件夹下index.j中
>>
>> sections // 页面对应vue文件存放位置，section注册在当前文件夹下index.js中
>>> components // vue文件中使用通用组件存放位置
>>
>> statics // 静态资源
>>> css // 通用css文件
>>>
>>> js // 通用js方法文件
>>>
>> appconfig.js // 以上所有文件需要使用都要在appconfig中配置
>>
> noco.config.js // 配置代理ip地址

---
#### 7. 文件夹分类
> pages
>> sims-cpm-platform 我的工作台
>>
>> sims-cpm-prj 工程建设管理
>>
>> sims-cpm-sup 厂商管理
>>
>> sims-cpm-pur 采购管理
>>
>> sims-cpm-dwd 设计管理
>>
>> sims-cpm-cm 成本管理
>>
>> sims-cpm-ctm 合同管理
>>
>> sims-cpm-csb 项目管理
>>
>> sims-cpm-mto 物料订单
>>
>> sims-cpm-pcm 租户配置？

::: tip
文档最新更新后名称：<br>
工程项目：sims-cpm-prj(原：项目、工程、设计、合同、成本)<br>
物料采购：sims-cpm-mto（原：物料、采购）<br>
厂商管理：sims-cpm-sup（原：厂商）<br>
:::

---
#### 8. 定义全局自定义方法
```js
> 1.自定义方法写在 common.js 中，例如： function getApi() {}
> 
> 2.在app.config.js中引入 statics
> 
> 3.挂载在Vue.prototype.$methodsJs上
> 
> 4.page.js文件中 vm.$methodsJs.getApi()
>
> 注：
>> a). $methodsJs全局方法：
>>> 1. async/await
>>> 2. 路由跳转
>>> 3. 设置uuid
>>> 4. 设置form表单的值 (参考下章的三、四条)
>> b). $messageJs全局弹窗提示: 见代码 statics -> js -> message.js
```
