import Axios from 'axios';
import Vue from 'vue'
import {CHINA_BOUNDARY} from './config'
let axios = Axios.create()
axios.defaults.timeout = 1000 * 60 * 2;
window._pending = [];
const cancelToken = Axios.CancelToken;
const removePending = ever=>{
    for(let p in window._pending ){
        if(window._pending [p].u===`${ever.url}&${ever.method}`){
            window._pending [p].f();
            window._pending .splice(p,1);
        }
    }
}
axios.interceptors.request.use(
    config=>{
        // removePending(config);
        config.cancelToken = new cancelToken((c)=>{
            window._pending .push({u:`${config.url}&${config.method}`,f:c,noCancel:config.url===CHINA_BOUNDARY})
        })
        return config;
    },
    err=> Promise.reject(err)
)
axios.interceptors.response.use(res => {
    // removePending(res.config);
    return res;
}, err => {
    if (err.response) {
        Vue.prototype.$message.error(`状态码：${err.response.status},错误信息：${err.response.statusText}`);
    }
    return Promise.reject(err)
})
export default axios;