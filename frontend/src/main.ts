import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from '@/router'

import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'

import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Toast from 'primevue/toast'
import Image from 'primevue/image'

//theme
import 'primevue/resources/themes/bootstrap4-dark-purple/theme.css'

//CSS
import './assets/main.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'

// App instance
const app = createApp(App)

// Axios configuration
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:5000'

// Initialize pinia
app.use(createPinia())

// Initialize vue router
app.use(router)

// Initialize Prime-vue
app.use(PrimeVue)

// Prime-vue components
app.component('PButton', Button)
app.component('PInputText', InputText)
app.component('PToast', Toast)
app.component('PImage', Image)

// Prime-vue services
app.use(ToastService)

// app mounting
app.mount('#app')
