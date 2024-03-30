<template>
  <div>
    <PToast />
  </div>
</template>
<script setup lang="ts">
import { useAuthStore } from '@/stores/authStore'
import { watchEffect } from 'vue'
import { useToast } from 'primevue/usetoast'
const authStore = useAuthStore()
const toast = useToast()
watchEffect(() => {
  if (authStore.errors.isOccurred) {
    toast.add({
      severity: 'error',
      summary: 'Authentication Error',
      detail: authStore.errors.message,
      life: 3000
    })
    authStore.cleanError()
  }
})
</script>

<style scoped></style>
