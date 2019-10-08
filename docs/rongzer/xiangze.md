## 翔择项目中组件用法
### tabContentSection结构
> length
> 
> title
> 
> collapse
> 
> list
> 
>> message
>>
>> array // 数组
>>> table：{} / formList: {}
>>
>> button
>>
>>> class
>>> 
>>> style
>>> 
>>> list
>>> 
### 例子
> <image-preview :imgUrl="'tableContentSection1.png'" />
>> <image-preview :imgUrl="'code1.png'" />
***
> <image-preview :imgUrl="'tableContentSection2.png'" />
>> <image-preview :imgUrl="'code2.png'" />
***
> <image-preview :imgUrl="'tableContentSection3.png'" />
>> <image-preview :imgUrl="'code3.png'" />
:::tip
注意：

  1.startValidate， 初始值设置为 '' 。 作用：用来校验 formList或者 获取formList、table的值<br>
  ```js
  //  a).为'save'时：不校验， 有的话就保存formList、table的值

  //  b).为'submit'时：先校验，校验成功后才会返回formList、table的值

  // 注：每个formList、table都必须有一个valueId, 例如： array[0].formList.valueId = 'formRef1'

  'on-change-validate-status': (val, table, form) => {
    startValidate = val // 必须
    // table返回的值，对象格式
    // form返回的值， 对象格式
    // 即 form =  {
    //   formRef1: ...
    // }
  } 
  ```

  2.list数组中每项有collapse，是控制'踏勘信息'、'踏勘分析'这种小类的收起、展开
:::