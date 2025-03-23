
// main.js
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import Vue3Lottie from 'vue3-lottie'

// 导入封装的 vuetify 配置
import vuetify from './plugins/vuetify.js'
// 导入封装的 Loading 组件
import Loading from './components/loading/loading.js'
// 引入 Lottie 动画库
import '@lottiefiles/lottie-player'; // 引入 Web Component




// 创建 Vue 应用并挂载 Vuetify
const app = createApp(App)
app.use(router)
app.use(vuetify)
app.mount('#app')
app.use(Loading)
app.use(Vue3Lottie);
