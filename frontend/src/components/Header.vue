<template>
  <Menubar :model="menuItems" class="bg-purple-800 sticky top-0 z-1" />
</template>
<script setup lang="ts">
import Menubar from 'primevue/menubar'
import { computed } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import type { MenuItem } from 'primevue/menuitem'

const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
}
const showLoginModal = () => {
  authStore.showLoginModal()
}

const menuItems = computed(() => {
  const baseItems: MenuItem[] = [
    {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      to: '/'
    },
    {
      label: 'About',
      icon: 'pi pi-fw  pi-info-circle',
      to: '/about'
    }
  ]
  const loginItem = {
    label: 'Login',
    icon: 'pi pi-fw  pi-user',
    command: showLoginModal
  }
  const logoutItem = {
    label: 'Logout',
    icon: 'pi pi-fw  pi-user',
    command: handleLogout
  }

  if (authStore.isAuthenticated) {
    baseItems.push(logoutItem)
  } else {
    baseItems.push(loginItem)
  }
  return baseItems
})
</script>
<style scoped></style>
