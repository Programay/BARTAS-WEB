<template>
  <Menubar :model="menuItems" class="bg-purple-800 sticky top-0 z-1" />
</template>
<script setup lang="ts">
import Menubar from 'primevue/menubar'
import { computed } from 'vue'

const menuItems = computed(() => {
  return [
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
      to: '/login'
    }
  ]
})
</script>
<style scoped></style>
