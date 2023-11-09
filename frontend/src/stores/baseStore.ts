import { defineStore } from 'pinia'
import type { IBaseStore } from '@/types/baseTypes'
import i18n from '@/vueI18n'

export const useBaseStore = defineStore('base', {
  state: (): IBaseStore => ({
    language: 'en'
  }),

  actions: {
    changeLanguage(newLanguage: string) {
      this.language = newLanguage
      i18n.global.locale.value = newLanguage
    }
  },
  persist: true
})
