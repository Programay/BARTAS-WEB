<template>
  <div>
    <h2 class="text-center">Bartender Assistant</h2>
    <PImage :src="getImageUrl('bar.jpg')" image-class="full-width" />
  </div>
</template>

<script setup lang="ts">
const getImageUrl: string = (imageName: string) => {
  return `/images/${imageName}`
}
</script>

<style>
.full-width {
  width: 85vw;
  display: block;
  margin: auto;
  padding: 10px;
}
</style>
