# linux安装环境

## 获取管理员权限
> sudo su root

## 安装linux工具

> 例如安装node：wget https://nodejs.org/dist/v12.14.1/node-v12.14.1-linux-arm64.tar.gz

## 安装完后，需要解压

> tar xvf  node-v12.14.1-linux-arm64.tar.gz

## 修改文件名字

> mv node-v12.14.1-linux-arm64 node-v12.14.1

## 将node移动到某个文件夹中

> mv  /root /node-v12.14.1-1.0/  /usr/sbin/
:::tip 提示
（mv 既能修改名字也能做move用）
:::

## 全局注册
> node：ln -s /usr/sbin/node-v12.14.1-1.0/bin/node  /usr/local/bin/ </br>
> npm: ln -s /usr/sbin/node-v12.14.1-1.0/bin/npm  /usr/local/bin/

*********************************************************************************
>以上在deepin v15.11上安装失败。使用sudo apt install node 一键安装成功
>> 安装node版本管理 npm install -g n
>>> n ls 查看版本， 安装最新版本 n 12.16.2 </br>
>>> n rm xxx 移除版本, n use xxx使用版本
>> 一般来说到这里就结束了，但是在项目中npm run serve报错
>>> `ound bindings for the following environments: - Windows 64-bit with Node.js 12.x ` </br>
>>> 一般来说就是node和sass版本的问题：重新安装npm rebuild node-sass

>> 安装git ： apt-get install git </br>
>> 安装vue-cli: npm i -g vue-cli (注意：如果失败，则在/usr/local/bin下重新安装)
>>> 使用vue命令安装uni-app, 但是需要vue3.0， 命令: npm i -g @vue/cli </br>
>>> a. 卸载npm uninstall -g vue-cli，再安装npm install -g @vue/cli </br>
>>> b. 创建uni-app项目， vue create -p dcloudio/uni-preset-vue xxxx
\



*********************************************************************************

配置淘宝镜像： npm    install    -g    cnpm    --registry=https://registry.npm.taobao.org

设置rar软件:
下载：
mkdir -p  /home/oldboy/tools
cd /home/oldboy/tools
wget http://www.rarlab.com/rar/rarlinux-3.8.0.tar.gz
安装：
tar zxvf rarlinux-3.8.0.tar.gz
cd rar
make
make install
压缩：
rar a etc.rar /etc  // 将文件夹etc压缩成etc.rar
解压缩：
rar x etc.rar  // 解压缩etc.rar
unrar -e etc.tar // 获取rar命令


文件夹含义
/usr/bin    系统预设的可执行文件，如开关机在这里，优先级最高
/usr/local/bin   用户本身相关的可执行文件，如自己安装的软件推荐放在这里，会提升到全局
/usr/sbin    基本同上

删除（-r递归向下，-f不提示）
删除文件夹：rm -rf /xxxx/xxx
删除文件：rm -f /xxx/xxx.txt

解压压缩相关
    z:代表的是压缩
    c:代表的是打包
    x:代表的是解压
    v:代表的是过程
    f:代表的是指定文件名
    因此zcvf :   打包压缩
    例如:  (tar   -zcvf    xxx.tar.gz    aaa.txt   bbb.txt   ccc.txt)   把aaa.txt   bbb.txt   ccc.txt打包压缩为一个名叫xxx.tar.gz 压缩包
    xvf: 解压缩
    例如(tar  -xvf   xxx.tar.gz    -C/usr)   -C代表解压的位置  把xxx.tar.gz解压缩到根目录下的usr目录


Deepin系统中手动开启swap的方法

swap（交换空间）的大小建议设置和你的实际物理内存一样大，如你的内存是8G的，则可将下面的count的值设为8192（当然这只是参考值，你可根据你系统运行的情况自行调整）。

sudo dd if=/dev/zero of=/root/swapfile bs=1M count=4096　#增加4G交换空间

sudo mkswap /root/swapfile　#建立swap的文件系统

sudo swapon /root/swapfile　#启用swap文件

echo "/root/swapfile swap swap defaults 0 0" | sudo tee -a /etc/fstab　#更新fstab文件