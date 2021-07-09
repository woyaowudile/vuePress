
const isProduction = ['production', 'prod'].includes(process.env.NODE_ENV);


export default {
    url: isProduction ? 'http://qianniu.mengtianxiang.top/' : '/'
    // url: 'http://qusnggapx.hn-bkt.clouddn.com/'
}