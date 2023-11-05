import { defineStore } from 'pinia'
import { LOGIN_ENDPOINT, REFRESH_LOGIN_ENDPOINT } from '@/stores/api/authAPI'
import axios from 'axios'
import type { ILoginResponse, IUserLogin } from '@/types/authTypes'
import { IAuthStore, IRefreshLoginResponse } from '@/types/authTypes'
import router from '@/router'

export const useAuthStore = defineStore('auth', {
  state: (): IAuthStore => ({
    accessToken: JSON.parse(localStorage.getItem('access_token')) || '',
    refreshToken: JSON.parse(localStorage.getItem('refresh_token')) || '',
    isAuthenticated: JSON.parse(localStorage.getItem('isAuthenticated')) || false,
    isLoginModalVisible: false,
    isLogoutModalVisible: false,
    errors: { isOccurred: false, message: '' }
  }),

  actions: {
    async login(username, password) {
      const loginData: IUserLogin = { username: username, password: password }
      axios
        .post(LOGIN_ENDPOINT, loginData)
        .then((res) => {
          const data: ILoginResponse = res.data
          this.accessToken = data.access_token
          this.refreshToken = data.refresh_token
          this.isAuthenticated = true
          localStorage.setItem('accessToken', JSON.stringify(this.accessToken))
          localStorage.setItem('refreshToken', JSON.stringify(this.refreshToken))
          localStorage.setItem('isAuthenticated', JSON.stringify(this.isAuthenticated))
          this.cleanError()
          this.isLoginModalVisible = false
          router.push('/')
        })
        .catch((e) => {
          const detail = e.response.data.detail
          this.setError(detail)
        })
    },
    cleanError() {
      this.errors.message = ''
      this.errors.isOccurred = false
    },
    setError(errorMessage: string) {
      this.errors.message = errorMessage
      this.errors.isOccurred = true
    },
    refreshToken() {
      if (!this.refreshToken) {
        this.logout()
        return
      }
      axios
        .post(REFRESH_LOGIN_ENDPOINT, { refresh_token: this.refreshToken })
        .then((res) => {
          const data: IRefreshLoginResponse = res.data
          this.accessToken = data.access_token
          this.isAuthenticated = true
        })
        .catch((e) => {
          console.log(e)
        }) // TODO logout on token expire
    },
    showLoginModal() {
      if (!this.isLoginModalVisible && !this.isAuthenticated) {
        this.isLoginModalVisible = true
      }
    },
    logout() {
      // TODO logout on BE needed
      this.accessToken = ''
      this.refreshToken = ''
      this.isAuthenticated = false
      localStorage.removeItem('accessToken', JSON.stringify(this.accessToken))
      localStorage.removeItem('refreshToken', JSON.stringify(this.refreshToken))
      localStorage.removeItem('isAuthenticated', JSON.stringify(this.isAuthenticated))
      router.push('/')
      this.isLogoutModalVisible = true
    }
  }
})
