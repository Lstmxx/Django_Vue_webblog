// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App'
import router from './router'

import qs from 'qs'
Vue.use(ElementUI)
Vue.use(VueAxios, axios)
axios.defaults.baseURL = "http://127.0.0.1:8000"
axios.defaults.withCredentials = true
Vue.prototype.$Qs = qs;
Vue.prototype.$axios = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
