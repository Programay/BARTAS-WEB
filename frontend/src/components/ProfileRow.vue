<template>
  <div class="grid bg-black-alpha-10 my-2">
    <div class="col-5">
      <p>{{ labelText }}</p>
    </div>
    <div class="col-7 flex justify-content-center">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, defineProps } from 'vue'
import { useI18n } from 'vue-i18n'

const props = defineProps<{
  label: string
}>()
const i18n = useI18n()

const labelText = computed(() => {
  return i18n.t(`profile.${props.label}`)
})
</script>
