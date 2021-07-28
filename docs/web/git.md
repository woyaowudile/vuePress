# git

## 一. 安装

## 二. 基础命令
#### 1.新建仓库
> git init
> git remote add origin 'http://xxxxxx'
> npm config set registry http://192.168.1.181:4873 // 设置npm安装ip

##### 2. 获取远端分支
> 如果是新的仓库，这里只有master分支 <br />
>> 查看本地分支 git branch <br />
>> 查看远端分支 git branch -r <br />
>> 查看所有分支 git branch -a

> 如果远程分支被删，本地还有被删除的分支
>> 更新本地分支 git remote prune origin

> 如果是已经在开发的仓库，本地git init后也只能看到master分支 <br />
>> 使用命令： git fetch 获取远端所有分支

##### 3. 切换分支
> git checkout xxxx <br />
> 新建分支： git branch xxxx <br />
> 首次切换远程分支到本地 git checkout -b 'xxx' origin/xxxx <br />
>> xxx表示本地的名字，origin/xxxx 表示远端的分支名字

##### 4. 放弃修改
> 已经add的代码 <br />
>> git reset HEAD xxx / git resrt HEAD . 撤销指定文件 / 所有文件

##### 5. 回退版本
> git log 获取提交历史 <br />
> git reset --hard HEAD^ 回退上一次 <br />
> git reset --hard commitid 'xx' 回退指定历史版本 <br />
> git reflog 也是获取提交历史 <br />
> git reset HARD 

#### 6. 合并
> 1.将代码提交到当前分支 <br />
> 2.切换到要合并的分支，比如将a合并到master <br />
>> git checkout master <br />
>> git merge a <br />
>> git push origin master <br />
注： 切换到新分支最好拉取代码解决冲突后再提交

## 三. 配置用户名、密码、邮箱（全局加上 --global）
> git config user xxxx <br />
> git config email xxxx <br />
> git config password xxxx
:::tip 提示
但是每次拉取、推送，还需要输入用户名、密码，所以配置： <br />
`git config --global(全局时使用) credential.helper store` <br />
:::


## 四. 代码关联多个仓库
> 本地项目 project，现在要同时上传到 githubA、githubB
> 1. project已经是拉取的项目A
> 2. git remote set-url --add origin http://githubB
> 3. git push origin master
```text
如果报错：
    有一个项目提示要先拉取再提交，那么就单独关联一下，即
    1.
        git remote add other htt://githubB
        git pull other master （将代码拉到本地，冲突合并等等处理完后）
        git pull origin master (将最新的代码也拉取到本地)
        git push origin master (最后直接推送即可)
        最后可以 git remote remove other
    2.
        git push origin master:master (当前本地所在分支:远程分支)
```
