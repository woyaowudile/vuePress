#!/usr/bin/env sh

# 确保脚本抛出遇到的错误
set -e

# 生成静态文件
npm run build

# 进入生成的文件夹
cd public

rm ./assets/img/*


# 如果是发布到自定义域名
# echo 'www.example.com' > CNAME

git init
git add -A
git commit -m $1

# 如果你想要部署到 https://USERNAME.github.io
git push -f git@mengtx:Mengtx-6192/Mengtx-6192.github.io.git master

# 退出命令
cd -

# npm run build-mengtx 'xxxxx'