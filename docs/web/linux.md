
## 一. linux安装环境

### 获取管理员权限
> sudo su root

### 安装linux工具

> 例如安装node：wget https://nodejs.org/dist/v12.14.1/node-v12.14.1-linux-arm64.tar.gz <br />
> 目前 deepin15 : apt-get install node / apt-get install git

### 安装完后，需要解压

> tar xvf  node-v12.14.1-linux-arm64.tar.gz

### 修改文件名字

> mv node-v12.14.1-linux-arm64 node-v12.14.1

### 将node移动到某个文件夹中

> mv  /root /node-v12.14.1-1.0/  /usr/sbin/
:::tip 提示
（mv 既能修改名字也能做move用）
:::

## 二. 设置服务器
> <a target="_blank" href="https://www.jianshu.com/p/7dc15bc448c7"> 原文地址 </a>

### 1. 开启ssh服务
> 查看是否有ssh服务：ssh localhost
>> 若出现：“ssh：connect to host localhost port 22: Connection refused”，则表明未安装 <br />

> 安装：sudo apt-get install openssh-server
>> 安装完成后，重新输入ssh localhost, 如果出现提示都选择yes <br />

> 查看是否开启ssh：ps -e|grep ssh
>> 输入密码后，有显示 sshd 表示成功<br />
>> 未成功：sudo /etc/init.d/ssh start<br />

### 2. putty连接服务器
><image-preview imgUrl="web/linux/putty.png" width='200'></image-preview>
><image-preview imgUrl="web/linux/putty-login.png" width='200'></image-preview>
> 设置超时时间
>> putty静置一段时间后，会提示连接错误<br />
>> <image-preview imgUrl="web/linux/putty-error.png" width='200'></image-preview>
>> <image-preview imgUrl="web/linux/putty-timeout.png" width='200'></image-preview>

### 3. 挂起任务
> 在终端运行一个程序,会占用终端,无法做其他事情
>> <image-preview imgUrl="web/linux/putty-jobs-1.png" width='200'></image-preview>
> 可以通过 ctrl + Z 挂起, 且可以通过jobs查看所有挂起的任务
>> <image-preview imgUrl="web/linux/putty-jobs-2.png" width='200'></image-preview>
>> bg %[number] 启动停止的任务<br />
>> fg %[number], 将后台任务放到前台运行<br />
>> kill %[number] 或者 jobs -l 获取到pid, 然后kill pid<br />

<br />

> nohup (cz挂起的任务,关闭终端后会被终止) 
>> nohup npm run serve > log.file 2>&1 &<br />
>> <image-preview imgUrl="web/linux/nohup-1.png" width='200'></image-preview>
> 查看: ps -ef|grep node , 关闭: kill + 端口<br />
> 查看: ps -aux|grep node , 效果同上,相差不大<br />
>> <image-preview imgUrl="web/linux/nohup-kill.png" width='200'></image-preview>

> 实时查看输出日志: 
>> tail -f log.file. <br /> 
>> 退出ctrl + c. 也可以挂起, 同jobs

:::warning
nohup挂起后, 退出putty 使用命令 exit
:::


### 4. 内网穿透
> 如果linux使用的wifi，外部访问l会提示连接不上<br />
> 原因：只有局域网内的设备才能互ping<br />
> 办法：使用内网穿透，也就是端口映射到外网上去
>> 这里使用的是ngrok,<a target="_blank" href="https://ngrok.com/download">linux的电脑访问ngrok</a>,按说明安装即可
</br>

> 配置隧道
```text
1. 设置 ngrok 隧道：（/root/.ngrok2/ngrok.yml）auth_token也在该文件中


tunnels:
    tunnel1:
        addr: 22
        proto: tcp
    tunnel2:
        addr: 3333
        proto: http
        -bing-tls: false 
        // false: 只使用http，true：只使用https
        // 不配置就二者都有，免费版只有4个隧道，例如3333就会占用2个隧道
    tunnel3:
        addr: 8080
        proto: http
        -bing-tls: false 

2. 启动
ngrok start --all // 启动所有端口
ngrok start tunnel1 tunnel2 // 启动指定端口
```