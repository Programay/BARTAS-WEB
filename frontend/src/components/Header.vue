<template>
  <Menubar :model="menuItems" class="sticky top-0 z-1 header-footer" />
</template>
<script setup lang="ts">
import Menubar from 'primevue/menubar'
import { computed } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import type { MenuItem } from 'primevue/menuitem'
import i18n from '@/vueI18n'
import router from '@/router'
const authStore = useAuthStore()

const handleLogout = () => {
  authStore.logout()
}
const showLoginModal = () => {
  authStore.showLoginModal()
}

const routerMenuItems = {
  home: {
    label: i18n.global.t('general.menubar.home'),
    icon: 'pi pi-fw pi-home',
    command: () => router.push('/')
  },
  about: {
    label: i18n.global.t('general.menubar.about'),
    icon: 'pi pi-fw  pi-info-circle',
    command: () => router.push('/about')
  },
  login: {
    label: i18n.global.t('general.menubar.login'),
    icon: 'pi pi-fw  pi-user',
    command: showLoginModal
  },
  logout: {
    label: i18n.global.t('general.menubar.logout'),
    icon: 'pi pi-fw  pi-power-off',
    command: handleLogout
  },
  profile: {
    label: i18n.global.t('general.menubar.profile'),
    icon: 'pi pi-fw pi-user',
    command: () => router.push('/profile')
  }
}

const menuItems = computed(() => {
  const unauthenticatedUserMenuItems: MenuItem[] = [
    routerMenuItems.home,
    routerMenuItems.about,
    routerMenuItems.login
  ]
  if (!authStore.isAuthenticated) {
    return unauthenticatedUserMenuItems
  }

  const authenticatedUserItems: MenuItem[] = [
    routerMenuItems.home,
    routerMenuItems.profile,
    routerMenuItems.about,
    routerMenuItems.logout
  ]

  return authenticatedUserItems
})
</script>
<style scoped></style>
