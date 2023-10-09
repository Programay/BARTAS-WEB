import { defineStore } from 'pinia'
import { LOGIN_ENDPOINT, REFRESH_LOGIN_ENDPOINT } from '@/stores/api/authAPI'
import axios from 'axios'
import type { ILoginResponse, IUserLogin } from '@/types/authTypes'
import { IAuthStore, IRefreshLoginResponse } from '@/types/authTypes'
import router from '@/router'

export const useAuthStore = defineStore('auth', {
  state: (): IAuthStore => ({
    access_token: JSON.parse(localStorage.getItem('access_token')) || '',
    refresh_token: JSON.parse(localStorage.getItem('refresh_token')) || '',
    isAuthenticated: JSON.parse(localStorage.getItem('isAuthenticated')) || false,
    isLoginModalVisible: false,
    errors: { is_occurred: false, message: '' }
  }),

  actions: {
    async login(username, password) {
      const loginData: IUserLogin = { username: username, password: password }
      axios
        .post(LOGIN_ENDPOINT, loginData)
        .then((res) => {
          const data: ILoginResponse = res.data
          this.access_token = data.access_token
          this.refresh_token = data.refresh_token
          this.isAuthenticated = true
          localStorage.setItem('access_token', JSON.stringify(this.access_token))
          localStorage.setItem('refresh_token', JSON.stringify(this.refresh_token))
          localStorage.setItem('isAuthenticated', JSON.stringify(this.isAuthenticated))
          this.errors.is_occurred = false
          this.errors.message = ''
          this.isLoginModalVisible = false
          router.push('/')
        })
        .catch((e) => {
          const detail = e.response.data.detail
          this.errors.is_occurred = true
          this.errors.message = detail
        })
    },
    refreshToken() {
      if (!this.refresh_token) {
        this.logout()
        return
      }
      axios
        .post(REFRESH_LOGIN_ENDPOINT, { refresh_token: this.refreshToken })
        .then((res) => {
          const data: IRefreshLoginResponse = res.data
          this.access_token = data.access_token
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
      this.access_token = ''
      this.refresh_token = ''
      this.isAuthenticated = false
      localStorage.removeItem('access_token', JSON.stringify(this.access_token))
      localStorage.removeItem('refresh_token', JSON.stringify(this.refresh_token))
      localStorage.removeItem('isAuthenticated', JSON.stringify(this.isAuthenticated))
      router.push('/')
    }
  }
})
