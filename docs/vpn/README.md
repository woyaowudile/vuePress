# clash

## 一. 使用教程

### 1.文档地址
> <a href="https://docs.ftt.me/" >点击前往： https://docs.ftt.me/</a>

### 2.注册 & 获取订阅链接
> 1).<a href="https://s.ftt.me/" >点击前往: https://s.ftt.me/</a>
:::tip 邀请码
<i style="color: '#ff00007a'; fontSize: '14px">提示：必须使用邀请码注册，不然注册不了。且每个链接只能使用一次！</i>
> https://s.ftt.me/home/ref/2481030771 <br />
> https://s.ftt.me/home/ref/5117980422 <br />
> https://s.ftt.me/home/ref/4033671448 <br />
> https://s.ftt.me/home/ref/6954309149 <br />
> https://s.ftt.me/home/ref/5001433292 <br />
> https://s.ftt.me/home/ref/9108327455 <br />
> https://s.ftt.me/home/ref/7445348313 <br />
> https://s.ftt.me/home/ref/2057543262 <br />
> https://s.ftt.me/home/ref/9441069939 <br />
> https://s.ftt.me/home/ref/8610948442 <br />
:::

> 2).<image-preview :imgUrl="'vpn/reizhi.png'" width="50%" height="50%" />

> 3).<a href="https://s.ftt.me/" >获取到订阅链接之后需要前往这里，点击前往: https://s.ftt.me/</a>
>> <image-preview :imgUrl="'vpn/Subscription-Converter.png'" width="50%" height="50%" />

> <a href="https://docs.ftt.me/" >之后就参考上面 ‘|文档地址|’ 的方法配置</a>

## 二. linux下使用
> 1.<a href="https://github.com/Dreamacro/clash/releases/" >点击跳转前往下载</a>
>> 一般来说，ubantu、deepin等都是amd，例如： clash-linux-amd64-v1.2.0.gz

> 2.创建一个文件夹，比如我放在/usr/local/sbin/clash/,将该压缩包复制过去
>> a).复制命令： sudo cp xxx/xxxx/xxx/clash-linux-amd64-v1.2.0.gz /usr/local/sbin/clash/   (备注： xxx表示你下载的路径) <br />
>> <br />
>> b).这里可以给clash-linux-amd64-v1.2.0.gz重命名
>>> mv clash-linux-amd64-v1.2.0 clash (注意：需要cd进入文件夹)

> 3.cd进入/usr/local/sbin/clash/ ，并解压缩
>> 命令： gunzip /clash-linux-amd64-v1.2.0.gz

> 4.给文件执行的权限
>> 命令： chmod +x clash 
>>> 注意： (clash是修改名称后的那个文件，如果没修改名称，则是clash-linux-amd64-v1.2.0)

> 5.控制台启动
>> 命令： ./clash
>> :::tip 备注
>> > 第一次启动的时候，会在 ~/.config/clash/ 下生成两个文件， 这个clash文件夹是自动生成的
>> >> <image-preview :imgUrl="'vpn/first-start-clash.png'" width="50%" height="50%" />
>> :::

> 6.设置condfig.yaml
>> 还记得上面点击 ‘|生成订阅链接|‘ 后，点击复制的吗？ <br />
>> 打开浏览器，将复制的链接 <br />
>> <image-preview :imgUrl="'vpn/getConfigyaml.png'" width="50%" height="50%" /> <br />
>> 下一步，将绿色框内容粘贴到condfig.yaml里面
>> 该阶段最后一步，将condfig.yaml再复制到之前创建的 /usr/local/sbin/clash/ 下即可。
:::warning 最终的文件
> <image-preview :imgUrl="'vpn/copyYaml.png'" width="50%" height="50%" />
:::

## 三. linux系统代理
> 1.配置代理
>> <image-preview :imgUrl="'vpn/proxy.png'" width="50%" height="50%" /> <br />
> 2.选择网页代理(默认会自动填写，可以在设置中查看或手动填写，<a href="http://clash.razord.top/" >点击前往：http://clash.razord.top/</a>)
>> <image-preview :imgUrl="'vpn/razord.png'" width="50%" height="50%" /> <br />
> 3.以上配置的内容从哪来的呢？还记得之前将订阅链接放入浏览器，然后复制的内容吗？
>> <image-preview :imgUrl="'vpn/yaml-config.png'" width="50%" height="20%" />
> 4.成功的样子
>> <image-preview :imgUrl="'vpn/razord2.png'" width="50%" height="50%" />

:::warning 退出
共两步：<br />
1.ctrl + c 关闭运行的控制台 <br />
2.必须将系统的代理改回无，否则无法上网
:::
