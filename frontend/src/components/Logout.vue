<template>
  <Dialog
    v-model:visible="authStore.isLogoutModalVisible"
    modal
    header="Logout"
    class="w-3"
    :draggable="false"
  >
    <p>You are logout</p>
  </Dialog>
</template>

<script lang="ts" setup>
import { useAuthStore } from '@/stores/authStore'
import Dialog from 'primevue/dialog'
// Authentication store
const authStore = useAuthStore()
</script>
