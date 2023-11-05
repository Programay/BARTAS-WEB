<template>
  <Dialog
    v-model:visible="authStore.isLoginModalVisible"
    modal
    header="Login"
    class="w-3"
    :draggable="false"
  >
    <form @submit.prevent="loginSubmit()">
      <span class="p-float-label mt-4">
        <PInputText class="w-full" id="username" v-model="user.username" />
        <label for="username">Username</label>
      </span>
      <span class="p-float-label my-4">
        <PInputText class="w-full" id="password" type="password" v-model="user.password" />
        <label for="password">Password</label>
      </span>
      <PButton class="w-full" label="Login" type="submit" rounded />
    </form>
  </Dialog>
</template>

<script lang="ts" setup>
import { reactive, watchEffect } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import Dialog from 'primevue/dialog'
import type { IUserLogin } from '@/types/authTypes'
// Authentication store
const authStore = useAuthStore()

const user: IUserLogin = reactive({
  username: '',
  password: ''
})

const loginSubmit = async () => {
  await authStore.login(user.username, user.password)
}

watchEffect(() => {
  const modalState = authStore.isLoginModalVisible
  if (!modalState) {
    user.username = ''
    user.password = ''
    authStore.cleanError()
  }
})
</script>
