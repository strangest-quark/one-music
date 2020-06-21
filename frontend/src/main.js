import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router/router';
import store from './store/store';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import './assets/main.scss'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueAxios, axios);

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  return next();
});

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
