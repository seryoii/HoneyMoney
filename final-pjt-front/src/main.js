import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import router from './router'
import '@/styles.css' // 스타일 파일 추가
loadFonts()
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

createApp(App)
  .use(pinia)
  .use(vuetify)
  .use(router)
  .mount('#app')
