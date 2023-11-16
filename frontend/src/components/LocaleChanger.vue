<template>
  <div class="card flex justify-content-center locale_changer">
    <PDropdown
      v-model="i18n.global.locale.value"
      :options="i18n.global.availableLocales"
      placeholder="Choose lang"
      class="w-full md:w-14rem"
    />
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue'
import { useBaseStore } from '@/stores/baseStore'
import i18n from '@/vueI18n'

const baseStore = useBaseStore()

watch(
  () => i18n.global.locale.value,
  (newVal) => {
    baseStore.changeLanguage(newVal)
  }
)
</script>

<style>
.locale_changer {
  padding: inherit;
}
</style>
