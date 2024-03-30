import { defineStore } from 'pinia'
import { LOGIN_ENDPOINT, REFRESH_LOGIN_ENDPOINT } from '@/stores/api/authAPI'
import axios from 'axios'
import type { ILoginResponse, IUserLogin } from '@/types/authTypes'
import { IAuthStore, IRefreshLoginResponse } from '@/types/authTypes'
import router from '@/router'
import { handleLoginFailure, handleRefreshTokenFailure } from '@/stores/api/errorHandlers'

export const useAuthStore = defineStore('auth', {
  state: (): IAuthStore => ({
    username: '',
    accessToken: '',
    refreshToken: '',
    isAuthenticated: false,
    isLoginModalVisible: false,
    isLogoutModalVisible: false,
    errors: { isOccurred: false, message: '' }
  }),

  actions: {
    async login(cridentials: IUserLogin) {
      try {
        const response = await axios.post<ILoginResponse>(LOGIN_ENDPOINT, cridentials)
        this.setAuthToken(response.data)
        this.setUsername(cridentials.username)
        this.router.push('/')
      } catch (error) {
        const errorMessage = handleLoginFailure(error)
        this.setError(errorMessage)
      }
    },
    logout() {
      this.accessToken = ''
      this.refreshToken = ''
      this.isAuthenticated = false
      router.push('/')
      this.isLogoutModalVisible = true
    },
    async refreshToken() {
      if (!this.refreshToken) {
        this.logout()
        return
      }
      try {
        const response = await axios.post<IRefreshLoginResponse>(REFRESH_LOGIN_ENDPOINT, {
          refresh_token: this.refreshToken
        })
        this.setAuthToken(response.data)
      } catch (error) {
        const errorMessage = handleRefreshTokenFailure(error)
        this.setError(errorMessage)
        this.logout()
      }
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
  getters: {
    isLoggedOut: (state) => !state.isAuthenticated
  },
  methods: {
    setAuthToken(data: { access_token: string; refresh_token: string }) {
      this.$patch({
        accessToken: data.access_token,
        refresh_token: data.refresh_token,
        isAuthenticated: true
      })
    },
    setUsername(username: string) {
      this.username = username
    }
  },
  persist: true
})
