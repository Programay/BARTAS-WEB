<template>
  <div class="flex justify-content-center">
    <div class="w-10">
      <h1 class="text-center">Bartender Assistant</h1>
      <PImage :src="getImageUrl('bar_crop.jpg')" image-class="w-12" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { getImageUrl } from '@/utils/static'
</script>

<style></style>
