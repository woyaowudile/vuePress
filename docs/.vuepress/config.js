const isProduction = ["production", "prod"].includes(process.env.NODE_ENV);

console.log("环境:", process.env.NODE_ENV);

let configList = isProduction
    ? [
          { text: "主页", link: "/" },
          {
              text: "内容分类",
              items: [
                  { text: "股票", link: "/gupiao/" },
                  // { text: '期货', link: '/future/' },
              ],
          },
      ]
    : [
          { text: "主页", link: "/" },
          {
              text: "内容分类",
              items: [
                  { text: "vpn", link: "/vpn/" },
                  { text: "vue", link: "/vue/" },
                  // { text: 'es6', link: '/es6/' },
                  // { text: 'js', link: '/js/' },
                  { text: "node", link: "/node/" },
                  { text: "css", link: "/css/" },
                  { text: "web", link: "/web/" },
                  { text: "python", link: "/python/" },
                  // { text: 'Rongzer', link: '/rongzer/' },
                  // { text: 'test', link: '/test1/' },
                  // { text: '期货', link: '/future/' },
                  { text: "股票", link: "/gupiao/" },
                  { text: "npm", link: "/npm/" },
              ],
          },
          // { text: '关于', link: '/about/' },
          // { text: 'Github', link: 'https://mengtx-6192.github.io' },
      ];

module.exports = {
    title: "回到开始",
    description: "mtx",
    dest: "public",
    markdown: {
        lineNumbers: true,
    },
    head: [
        ["link", { rel: "icon", href: "/img/logo.ico" }],
        ["link", { rel: "mainifest", href: "/maifest.json" }],
    ],
    themeConfig: {
        log: "", // 图片链接或资源目录
        nav: configList,
        sidebar: {
            "/vpn/": [""],
            "/vue/": ["", "vue"],
            "/es6/": [""],
            "/js/": ["", "skills"],
            "/node/": ["", "exports和export"],
            "/css/": ["", "sass"],
            "/web/": ["git", "note", "webpack", "linux", "", "study", "markdown"],
            "/python/": [
                "",
                "for、while",
                "import和格式符",
                "数组、字典",
                "方法体",
                "类与继承",
                "文件读、写",
                "爬虫",
                "selenium",
                "time",
                "多协程、队列",
            ],
            "/rongzer/": ["", "xiangze"],
            "/test1/": [""],
            "/future/": [""],
            "/gupiao/": [
                "",
                "norm",
                "action",
                "risk",
                // "analysis",
            ],
            "/npm/": ["", "publish"],
        },
        sidebarDepth: 4, // 将 #、## 的标题显示到左侧侧边栏
        lastUpdated: "更新时间", // 显示更新
    },
};
