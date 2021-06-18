set -e

npm run build

cd public

git init 
git add -A
git commit -m $1

git push -f https://github.com/Mengtx-6192/Mengtx-6192.github.io.git master

cd -