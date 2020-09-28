#  搭建 vuepress

## 一. 安装

1. 使用yarn或者npm (点击<a target="_blank" href="https://yarn.bootcss.com/docs/install">yarn</a>或者<a target="_blank" href="http://nodejs.cn/download/">node</a>进行安装)。下载后直接双击打开下一步即可。

2. 创建一个空文件夹,例如press，初始化创建一个package.json
><image-preview :imgUrl="'init.jpg'" />

3. 在package.json中 <strong style="color: red">添加</strong> 运行/打包命令(这里添加了上传网站的命令)，名字可以随便定义！
```json
"scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs",
    "deploy": "bash deploy.sh"
}
```

4. 同目录下创建docs文件夹，进入docs，创建.vuepress文件夹，进入，然后创建config.js
><image-preview :imgUrl="'config.jpg'" />

5. 在docs文件夹下，创建README.md，也就是上图中主页显示的内容，这个就相当于index.html

6. 这时候你将看到以下目录
   >press
   >>package.json
   >>
   >>docs
   >>>README.md
   >>>
   >>>.vuepress
   >>>>config.js

7. 运行命令先安装npm install -g vuepress，启动或打包。打包后会发现多了两个文件夹
   >press
   >>package.json
   >>
   >>docs
   >>>README.md
   >>>
   >>>.vuepress
   >>>>config.js
   >>
   >>node_modules
   >>
   >>public
   ***
   运行启动命令后如下，说明成功
   ><image-preview :imgUrl="'dev.jpg'" />

## 二. 部署
><p>1. 首先得有自己的虚拟/云主机，可以在阿里云、百度云等网站上购买</p>
><p>2. 或者使用免费的github pages搭建静态网站</p>
>
>> a). 登陆github创建一个新项目，项目名：github账号名 + github.io
>><image-preview :imgUrl="'name.jpg'" />
>> b). 然后，将打包后的public中的文件提交上传即可。成功后浏览器输入https://Mengtx-6192.github.io
>
><p>3. 最后，可以将代码上传github。这里最好先设置.gitignore将node_mouldes和public设置进去。因为你要是先提交，后添加忽略文件的话，会发现并没有生效，这时候需要你先清除之前的缓存。</p>
   
## 结尾
>每次更新代码，还要输入打包命令，添加文件提交代码，然后上传...
>***
>我就是懒，怎么办呢？现在回头看看之前的package.json中，除了运行命令，打包命令，还有个deploy
>***
>在根目录下新建一个deploy.sh的文件
>><image-preview :imgUrl="'github.jpg'" />
>写入内容如下：($1就是提交信息)
>><image-preview :imgUrl="'gitbash.jpg'" />
>当你需要更新代码的时候，就可以运行命令 "npm run deploy '提交信息'"
:::warning 注意
既然是用了git命令，那么在cmd里面可用不了，在git bash中运行。
在当前文件夹中右键，如果能看不到 git bash，说明没有安装
:::

:::tip
如果遇到The remote end hung up unexpectedly
则在当前目录下的.git -> config 中添加
[http]
postBuffer = 524288000
:::