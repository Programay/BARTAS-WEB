<template>
  <Dialog
    v-model:visible="authStore.isLogoutModalVisible"
    modal
    header="Logout"
    class="lg:w-3"
    :draggable="false"
  >
    <p>{{ $t('general.auth.messages.logoutMessage') }}</p>
  </Dialog>
</template>

<script lang="ts" setup>
import { useAuthStore } from '@/stores/authStore'
import Dialog from 'primevue/dialog'
// Authentication store
const authStore = useAuthStore()
</script>
