import { createApp } from 'vue'
import App from './App.vue'
import Equal from 'equal-vue'
import 'equal-vue/dist/style.css'
import router from './router'

createApp(App)
    .use(router)
    .use(Equal)
    .mount('#app')