import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'
import { REFRESH_LOGIN_ENDPOINT } from '@/stores/api/authAPI'
import type { IRefreshLoginResponse } from '@/types/authTypes'

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
        authStore.errors.isOccurred = true
        authStore.errors.message =
          'Your token expire or some other errors occurred. Please Login again'
      }
      // Other error
    } else {
      authStore.errors.isOccurred = true
      authStore.errors.message = "We can't log you in. Please contact with us."
    }
    return Promise.reject(error)
  }
)

export default api
