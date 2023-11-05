<template>
  <footer
    class="flex justify-content-center w-full text-white sticky bottom-0 z-1 footer header-footer"
  >
    <p>&copy; {{ currentYear }} Programay</p>
  </footer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const currentYear = ref(new Date().getFullYear())
</script>
<style scoped>
.footer {
  position: absolute;
  bottom: 0;
  color: rgba(255, 255, 255, 0.6) !important;
}
</style>
