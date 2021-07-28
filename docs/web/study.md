# 使用 vuepress

## 一.文件目录
   press
   >.gitignore
   >
   >deploy.sh
   >
   >package.json
   >
   >docs
   >>README.md
   >>
   >>.vuepress
   >>>config.js
   >>>
   >>>enhanceApp.js  // 引入ui组件框架
   >>>
   >>>components
   >>>>image-preview.vue
   >>>>
   >>>>Header
   >>>>>Section.vue
   >>>
   >>>images // 图片
   >>>
   >>>styles // 样式
   >>>>palette.styl
   >>
   >>...
   >
   >node_modules
   >
   >public
***
## 二. 组件使用
>```js
>// 直接使用
><image-preview />
>```
>
>```js
>// 文件夹下使用， 传入参数
><Header-Section :data="data" />
>```
:::tip 提示
组件命名规则： 短横线和大驼峰
:::
***
## 三. 样式设置
<p>使用审查元素找到需要修改样式的元素</p>
<p>然后在styles文件夹下的palette.styl中</p>

>```css
>.page {
>    > div {
>        > blockquote {
>            word-break: break-word;
>        }
>    }
>    .theme-default-content {
>        .line-numbers-mode {
>            .line-numbers-wrapper {
>                width: 2.5rem;
>            }
>            &::after {
>                width: 2.5rem;
>            }
>        }
>    }
>}
>```
***

## 四. UI框架使用

<p>在.vuepress文件夹下新建一个enhanceApp.js</p>

>内容如下：
>```js
>    // 首先使用npm install vant下载
>    import vant from 'vant'
>    import 'vant/lib/index.css'
>
>    export default ({
>        Vue
>    }) => {
>        Vue.use(vant)
>    }
>```