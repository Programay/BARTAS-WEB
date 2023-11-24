import { createI18n } from 'vue-i18n'

// import translations
import pl from '@/locales/pl.json'
import en from '@/locales/en.json'

const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages: { pl, en }
})

export default i18n
