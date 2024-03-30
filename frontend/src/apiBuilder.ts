import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'
import { useI18n } from 'vue-i18n'

const i18n = useI18n()

const authStore = useAuthStore()

const api: axios = axios.create()

// Add token to headers
api.interceptors.request.use((config) => {
  if (authStore.token) {
    config.headers.Authorization = `Bearer ${authStore.token}`
  }
  return config
})

// Add token expire exception
api.interceptors.response.use(
  (response) => response, // Correct response
  (error) => {
    if (error.response) {
      // authentication error
      if (error.response.status === 401) {
        authStore.refreshToken()
      } else {
        authStore.setError(i18n.t('general.auth.messages.tokenExpire'))
      }
    } else {
      authStore.setError(i18n.t('general.auth.messages.loginTechnicalProblems'))
    }
    return Promise.reject(error)
  }
)

export default api
