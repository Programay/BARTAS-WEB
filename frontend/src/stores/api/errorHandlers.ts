import { useI18n } from 'vue-i18n'

export const handleLoginFailure = (error: unknown): string => {
  const i18n = useI18n()
  if (axios.isAxiosError(error) && error.response?.status === 400) {
    return i18n.t('general.auth.messages.incorrectUsernameOrPassword')
  } else {
    console.error(error)
    return i18n.t('general.auth.messages.authenticationProblem')
  }
}
export const handleRefreshTokenFailure = (error: unknown): string => {
  const i18n = useI18n()
  if (axios.isAxiosError(error) && error.response?.status === 400) {
    return i18n.t('general.auth.messages.tokenExpire')
  } else {
    console.error(error)
    return i18n.t('general.auth.messages.authenticationProblem')
  }
}
