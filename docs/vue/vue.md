# vue 3.0

## 一. setup

### 注意
> import、export default、name、props、components 照旧 <br />
> 执行setup时, 组件实例尚未被创建.所以只能访问到:
>>props\attrs\slots\emit <br />

> 访问不到
>> data\computed\methods\refs

### setup() {}
```vue
<script>
    import xxxx from 'xxxxx'
    import { ref, reactive, onMounted, toRefs... } from 'vue'
    export default {
        name: 'xx',
        components: { xxxx },
        props: {
            msg: String
        }
        setup(props, context) {
            // 前三等同 $attrs, $emit, $slots。 expose 同 defineExpose。
            // context普通js对象，所以可以直接解构
            const { attrs, emit, slots, expose } = context
            // 注: attrs\slots只会在update周期中被改变, 且使用方式: attrs.xx, slots.xx

            // 1. 不能直接解构pros，因为props是响应式的，直接解构会消除响应性。使用 toRefs
            // cosnt { msg } = props
            const { msg } = toRefs(props)
            // 2
            const msg = props.msg

            const test1 = ref(0)
            const test2 = reactive({ a: 111 })

            // 需要使用变量接收, 然后return后才能使用到
            return { msg, test1, test2 }
        }
    }
</script>
<template>
    <xxxx>{{msg}}</xxxx>
</template>
```

### script setup
```vue
<script setup>
    // 具体参考 ‘可引入的值’
    import { ref, reactive, onMounted... } from 'vue'

    // import引入组件后可直接使用,组件名遵循大驼峰写法
    import Ab from 'xxxxx'

    // 设置变量
    const msg = '11111'
    // 绑定响应式的值, 即将初始值设置给test1，一般为 undefined、null、number、string等
    const test1 = ref(0)
    // 同ref，区别是深度响应，即 Array\Object
    const test2 = reactive({ a: [1,2,3,4] })
    // 打印的话需要test1.value, template使用则可以直接test1.因为在编译的时候，已经浅解析了
    console.log(test1.value, test1.a[0]) // 0, 1
    
    // 事件点击
    const clickAb = () => { ... }
    // 或者
    function clickAb() { ... }
   
   
   // watch
    watch(test1, (nv, ov) => { ... })
    watch(() => test2.a, (nv, ov) => { ... })
    watch([test1, test2.a...], ([nv, ov], [nv, ov]...) => { ... })
   
   // computed
    const gettest1 = computed(() => test1 + 1) // 1
    gettest1++ // 错误，需要使用set设置
    // computed get\set
    let gettest1 = computed({
        get: () => test1.value,
        set: val => test1.value = val - 1
    })
    console.log(gettest1.value) // 0
    gettest1.value = 3
    console.log(gettest1.value) // 2
    // ref
    const compAb = ref(null)
    onMounted(() => {
        // todo...这里用setup语法糖获取到的始终是proxy，而setup(){}方法体中使用，可以获取到dom
        console.dir(compAb)
    })

    // 子组件导出可用属性，在父组件中使用ref只能获取到test1, test2获取不到
    defineExpose({
        test1,
        // test2
    })
    
    // props直接使用，也可定义接受类型和默认值，和以前相同，变量名随便写不写
    const pps = defineProps({
        item: '就是传入的值'
    })
    // 子组件传递 > 父组件
    const Emit = defineEmit(['update:name'])
    const clickAb = () => Emit('update:name', 'xxx参数')
   

    // provide、inject
    // 父组件中...建议设置只读
    provide('testProvide1', readonly(ref('testProvide---1'))) // 添加响应式：ref、reactive
    // 子组件中...
    inject('testProvide1', '默认值(可选)')
</script>
<template>
    <Ab ref="compAb" @click="clickAb">{{msg}} --- {{item}}</Ab>
    <!-- 或者使用动态组件 -->
    <component :is='Ab'></component>
</template>
```


### 可引入的值

<details>
  <summary><mark><font color=darkred>import {} from 'vue'</font></mark></summary>
  <div>响应式：ref, reactive, readonly</div>
  <div>生命周期： onBeforeMount, onMounted, onBeforeUnmount, onUnmounted, nextTick</div>
  <div>use：useSlots, useAttrs</div>
  <div>监听：watch、computed</div>
  <div>传参：provide、inject</div>
  <div></div>
</details>