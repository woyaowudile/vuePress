module.exports = {
    title: '回到开始',
    description: 'mtx',
    dest: 'public',
    markdown: {
        lineNumbers: true,
    },
    head: [
        [
            'link', { rel: 'icon', href: '/img/logo.ico' }
        ],
        [
            'link', { rel: 'mainifest', href: '/maifest.json' }
        ]
    ],
    themeConfig: {
        log: '', // 图片链接或资源目录
        nav: [
            { text: '主页', link: '/' },
            { text: '内容分类',
              items: [
                { text: 'vue', link: '/vue/' },
                { text: 'es6', link: '/es6/' },
                { text: 'js', link: '/js/' },
                { text: 'node', link: '/node/' },
                { text: 'css', link: '/css/' },
                { text: 'web', link: '/web/' },
                // { text: 'Rongzer', link: '/rongzer/' },
                // { text: 'test', link: '/test1/' },
                // { text: '期货', link: '/future/' },
              ]
            },
            // { text: '关于', link: '/about/' },
            { text: 'Github', link: 'https://mengtx-6192.github.io' },
        ],
        sidebar: {
            '/vue/': [
                "",
                "vue"
            ],
            "/es6/":[
                "",
            ],
            "/js/":[
                "",
                "skills"
            ],
            "/node/":[
                ""
            ],
            "/css/":[
                "",
                "sass"
            ],
            "/web/":[
                "",
                "study",
                "markdown",
                "note",
                "linux",
                "git",
                "webpack"
            ],
            "/rongzer/":[
                "",
                "xiangze",
            ],
            "/test1/":[
                "",
            ],
            "/future/":[
                "",
            ],
        },
        sidebarDepth: 4, // 将 #、## 的标题显示到左侧侧边栏
        lastUpdated: '更新时间', // 显示更新
    }
};