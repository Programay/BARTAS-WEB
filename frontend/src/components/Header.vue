<template>
  <Menubar :model="menuItems" class="sticky top-0 z-1 header-footer" />
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
  const unauthenticatedUserMenuItems: MenuItem[] = [
    {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      to: '/'
    },
    {
      label: 'About',
      icon: 'pi pi-fw  pi-info-circle',
      to: '/about'
    },
    {
      label: 'Login',
      icon: 'pi pi-fw  pi-user',
      command: showLoginModal
    }
  ]
  if (!authStore.isAuthenticated) {
    return unauthenticatedUserMenuItems
  }

  const authenticatedUserItems: MenuItem[] = [
    {
      label: 'Home',
      icon: 'pi pi-fw pi-home',
      to: '/'
    },
    {
      label: 'Sample1',
      icon: 'pi pi-fw pi-home',
      to: '/'
    },
    {
      label: 'Sample2',
      icon: 'pi pi-fw pi-home',
      to: '/'
    },
    {
      label: 'Logout',
      icon: 'pi pi-fw  pi-user',
      command: handleLogout
    }
  ]

  return authenticatedUserItems
})
</script>
<style scoped></style>
