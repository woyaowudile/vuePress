module.exports = {
    title: '个人主页',
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
        nav: [
            { text: '主页', link: '/' },
            { text: '内容分类',
              items: [
                { text: 'vue', link: '/vue/' },
                { text: 'es6', link: '/es6/' },
                { text: 'web', link: '/web/' },
                { text: 'Rongzer', link: '/rongzer/' },
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
            "/web/":[
                "",
                "study",
                "markdown"
            ],
            "/rongzer/":[
                "",
                "xiangze",
            ],
        },
        sidebarDepth: 2,
        lastUpdated: 'Last Updated', 
    }
}