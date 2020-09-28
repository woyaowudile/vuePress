# webpack

## webpack-plugin

### 一. 准备
> 初始化文件
> <image-preview :width="'400'" :imgUrl="'webpack/1.init.png'" />
> 创建文件并安装依赖
> <image-preview :width="'400'" :imgUrl="'webpack/2-npm和文件结构.png'" />

### 二. 插件
> addtime-webpack-plugin.js
```js
class AddtimeWebpackPlugin {
    constructor(options) {
        this.filename = options && options.filename ? options : 'filename.js';
    }

    apply(compiler) {
        compiler.hooks.emit.tapAsync('AddtimeWebpackPlugin', (compilation, cb) => {
            // 1. 获取打包文件的集合
            const assets = compilation.assets;
            // 2. 设置文件内容和大小
            const time = new Date().toLocaleString();
            assets[this.filename] = {
                source() {
                	// 内容
                	console.log(time);
                    return `console.log('${time}')`;
                },
                size() {
                	// 打包时显示的大小
                    return time.length;
                }
            };
            cb();
        });
    }
}

module.exports = AddtimeWebpackPlugin;
```

> webpack.config.js
```js
const path = require('path');
const htmlWebpackPlugin = require('html-webpack-plugin');
// 注意： html 和 clean包的导入方式
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const AddtimeWebpackPlugin = require('./js/addtime-webpack-plugin.js');

module.exports = {
    'entry': './js/index.js',
    'output': {
        'path': path.resolve(__dirname, 'dist'),
        'filename': '[name].js'
    },
    'plugins': [
        new htmlWebpackPlugin({
            'hash': true, // 清除缓存，在html中引入的js后面添加hash
            'template': './index.html'
        }),
        new CleanWebpackPlugin(),
        new AddtimeWebpackPlugin()
    ]
};
```

```html
<!DOCTYPE html>
<html>
<head>
	<title>打包时间添加</title>
</head>
<body>
<!-- 打包后的main.js将在这里引入 -->
</body>
<script type="text/javascript" src="filename.js"></script>
</html>
```

### 三. 结果
> <image-preview :width="'400'" :imgUrl="'webpack/3.result.png'" />