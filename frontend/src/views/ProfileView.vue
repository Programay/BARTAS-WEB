<template>
  <div class="flex justify-content-center">
    <div class="lg:w-4 pt-5">
      <PCard>
        <template #title
          ><p class="text-3xl text-center">{{ $t('profile.title') }}</p></template
        >
        <template #content>
          <div class="grid bg-black-alpha-10">
            <div class="col">
              <p>{{ $t('profile.language') }}</p>
            </div>
            <div class="col">
              <LocaleChanger />
            </div>
          </div>
        </template>
      </PCard>
    </div>
  </div>
</template>

<style></style>
<script setup lang="ts">
import LocaleChanger from '@/components/LocaleChanger.vue'
</script>
