<template>
  <footer
    class="bg-purple-800 flex justify-content-center w-full text-white sticky bottom-0 z-1"
    style="position: absolute; bottom: 0"
  >
    <p>&copy; {{ currentYear }} Programay</p>
  </footer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const currentYear = ref(new Date().getFullYear())
</script>
<style scoped></style>
