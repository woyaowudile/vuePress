# 发布

## 一. 初始化
> <image-preview :imgUrl="'npm/1.jpg'" width="50%" height="50%" />

> <image-preview :imgUrl="'npm/2.jpg'" width="50%" height="50%" />

## 二. 登录
> <image-preview :imgUrl="'npm/3.jpg'" width="50%" height="50%" />

## 三. 发布
> <image-preview :imgUrl="'npm/4-1.jpg'" width="50%" height="50%" />

> npm version patch 可自动对版本号 + 1
>> <image-preview :imgUrl="'npm/4-2.jpg'" width="50%" height="50%" />


> <image-preview :imgUrl="'npm/4-3.jpg'" width="50%" height="50%" />

> <image-preview :imgUrl="'npm/5.jpg'" width="50%" height="50%" />

> <image-preview :imgUrl="'npm/6-1.jpg'" width="50%" height="50%" />

> <image-preview :imgUrl="'npm/6-2.jpg'" width="50%" height="50%" />

> npm unpublish --force 直接删除包的所有版本（好像是只能删除72小时内的）
>> <image-preview :imgUrl="'npm/7.jpg'" width="50%" height="50%" />

> 使用
>> <image-preview :imgUrl="'npm/8.jpg'" width="50%" height="50%" />

## 四. 测试版本
> npm publish --tag=beta
> 在pcakage.json里  "version": "1.0.0-beta"

## 五. 本地使用
> npm run build
> npm pcak
>> 生成包 xxxx.tgz

```js
// 然后在项目中
npm i 路径/包的名字.tgz
```