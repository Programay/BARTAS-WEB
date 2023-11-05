export interface IAuthStore {
  accessToken: string
  refreshToken: string
  isLoginModalVisible: boolean
  isLogoutModalVisible: boolean
  isAuthenticated: boolean
  errors: IAuthErrors
}

interface IAuthErrors {
  isOccurred: boolean
  message: string
}

export interface IUserLogin {
  username: string
  password: string
}

export interface ILoginResponse {
  access_token: string
  refresh_token: string
}

export interface IRefreshLoginResponse {
  access_token: string
}
