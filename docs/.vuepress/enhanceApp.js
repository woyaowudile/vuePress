import ViewUI from "view-design";
import "view-design/dist/styles/iview.css";

import vant from "vant";
import "vant/lib/index.css";

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


import { checkAuth } from './helper';
import env from '../env'
import Login from './login';

export default ({ Vue }) => {
    Vue.use(vant);
    Vue.use(ElementUI);
    Vue.mixin({
        provide () {
            return {
              env: env
            }
          },
        // 请确保只在 beforeMount 或者 mounted 访问浏览器 / DOM 的 API
        mounted() {
            const doCheck = () => {
                if (!checkAuth()) {
                    this.$dlg.modal(Login, {
                        width: 400,
                        height: 350,
                        title: '请登录您的账号',
                        singletonKey: 'user-login',
                        maxButton: false,
                        closeButton: false,
                        callback: data => {
                            if (data === true) {
                                // do some stuff after login
                            }
                        }
                    })
                }
            }

            if (this.$dlg) {
                doCheck()
            } else {
                import('v-dialogs').then(resp => {
                    Vue.use(resp.default)
                    this.$nextTick(() => {
                        doCheck()
                    })
                })
            }
        }
    })
};