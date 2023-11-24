import { defineStore } from 'pinia'
import { LOGIN_ENDPOINT, REFRESH_LOGIN_ENDPOINT } from '@/stores/api/authAPI'
import axios from 'axios'
import type { ILoginResponse, IUserLogin } from '@/types/authTypes'
import { IAuthStore, IRefreshLoginResponse } from '@/types/authTypes'
import router from '@/router'
import i18n from '@/vueI18n'

export const useAuthStore = defineStore('auth', {
  state: (): IAuthStore => ({
    accessToken: '',
    refreshToken: '',
    isAuthenticated: false,
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
          this.cleanError()
          this.isLoginModalVisible = false
          router.push('/')
        })
        .catch((error) => {
          if (error.response.status === 400) {
            this.setError(i18n.global.t('general.auth.messages.incorrectUsernameOrPassword'))
          } else {
            console.log(error)
            this.setError(i18n.global.t('general.auth.messages.authenticationProblem'))
          }
        })
    },
    logout() {
      this.accessToken = ''
      this.refreshToken = ''
      this.isAuthenticated = false
      router.push('/')
      this.isLogoutModalVisible = true
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
        .catch((error) => {
          if (error.response.status === 400) {
            this.setError(i18n.global.t('general.auth.messages.tokenExpire'))
          } else {
            console.log(error)
            this.setError(i18n.global.t('general.auth.messages.authenticationProblem'))
          }
          this.logout()
        })
    },
    showLoginModal() {
      if (!this.isLoginModalVisible && !this.isAuthenticated) {
        this.isLoginModalVisible = true
      }
    },
    cleanError() {
      this.errors.message = ''
      this.errors.isOccurred = false
    },
    setError(errorMessage: string) {
      this.errors.message = errorMessage
      this.errors.isOccurred = true
    }
  },
  persist: true
})
