import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'

//theme
import 'primevue/resources/themes/bootstrap4-dark-purple/theme.css'

//CSS
import './assets/main.css'
import 'primeicons/primeicons.css'
const app = createApp(App)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:5000'

app.use(createPinia())
app.use(router)
app.use(PrimeVue)

app.component('PButton', Button)

app.mount('#app')
