import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedState from 'pinia-plugin-persistedstate'
import axios from 'axios'
import App from './App.vue'
import router from '@/router'
import i18n from '@/vueI18n'

import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'

import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Toast from 'primevue/toast'
import Image from 'primevue/image'
import Dropdown from 'primevue/dropdown'
import Card from 'primevue/card'

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
const pinia = createPinia()
// Initialize persisted storage
pinia.use(piniaPluginPersistedState)
app.use(pinia)

// Initialize vue router
app.use(router)

// Initialize Prime-vue
app.use(PrimeVue)

// Prime-vue components
app.component('PButton', Button)
app.component('PInputText', InputText)
app.component('PToast', Toast)
app.component('PImage', Image)
app.component('PDropdown', Dropdown)
app.component('PCard', Card)

// Prime-vue services
app.use(ToastService)

// Initialize translations
app.use(i18n)
import { useBaseStore } from '@/stores/baseStore'
const baseStore = useBaseStore()
i18n.global.locale.value = baseStore.language

// app mounting
app.mount('#app')
