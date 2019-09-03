module.exports = {
    title: '个人主页',
    description: 'mtx',
    base: '/index/',
    dest: 'public',
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
            { text: '博文',
              items: [
                { text: 'vue', link: '/vue/' },
                { text: 'es6', link: '/es6/' },
                { text: 'web', link: '/web/' }
              ] 
            },
            { text: '关于', link: '/about/' },
            { text: 'Github', link: 'https://www.github.com/codeteenager' },
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
                ""
            ],
        },
        sidebarDepth: 2,
        lastUpdated: 'Last Updated', 
    }
}