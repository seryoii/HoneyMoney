import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'

loadFonts()
const pinia = createPinia()

createApp(App)
  .use(pinia)
  .use(vuetify)
  .use(router)
  .mount('#app')
