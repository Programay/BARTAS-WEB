<template>
  <div class="flex justify-content-center">
    <div class="w-10">
      <PImage :src="getImageUrl('bar_2_crop.jpg')" image-class="w-12" />
      <PCard>
        <template #title
          ><p class="text-3xl">{{ $t('aboutPage.title') }}</p></template
        >
        <template #content>
          <p class="m-1 text-2xl">{{ $t('aboutPage.summary') }}</p>
        </template>
      </PCard>
    </div>
  </div>
</template>

<style></style>
<script setup lang="ts">
import { getImageUrl } from '@/utils/static'
</script>
