# npm

## 一. <a href="https://www.npmjs.com/">点击注册</a>

## 二. 使用

### 1. 设置源

```text
var origin = http://registry.npm.taobao.org

npm config set registry origin
```

### 2. 多个源切换

```text
npm config set registry origin1

npm config set registry origin2

...
```
```
可以使用nrm来管理源

安装： npm i -g nrm
查看： nrm ls
使用： nrm use xxx
增加： nrm add registry origin(变量名)
删除： nrm del registry

```

### 例子： 
> #### 默认情况下：
>> <image-preview :imgUrl="'npm/nrm-ls.png'" width="50%" height="50%" />
> #### 新增一个源： nrm add rz http://192.168.1.11:1111
>> <image-preview :imgUrl="'npm/nrm-add.png'" width="50%" height="50%" />
> #### so，删除即 nrm del rz



## 三. 登录npm

#### 1. 首先用nrm 切换至对应的 npm源

#### 2. 如果是第一次，先 npm adduser
> <image-preview :imgUrl="'npm/npm-adduser.png'" width="50%" height="50%" />

#### 3. npm login
> 和第二步类似，也是需要用户名、密码、邮箱

#### 4. 显示登录成功后，可以查看登录的用户
> <image-preview :imgUrl="'npm/npm-login.png'" width="50%" height="50%" />
> 查看当前所在源
>> a>. nrm ls
>> b>. npm config get registry

