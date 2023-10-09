<template>
  <div class="app-container py-2">
    <Header />
    <Login />
    <router-view class="router-view-body mx-4" />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Login from '@/components/Login.vue'
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.router-view-body {
  flex: 1;
}
</style>
