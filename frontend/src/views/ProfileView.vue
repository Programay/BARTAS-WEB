<template>
  <div class="flex justify-content-center">
    <div class="lg:w-4 pt-5">
      <PCard>
        <template #title>
          <p class="text-3xl text-center">{{ $t('profile.title') }}</p>
        </template>
        <template #content>
          <profile-row label="username">
            <p>{{ username }}</p>
          </profile-row>
          <profile-row label="language">
            <LocaleChanger />
          </profile-row>
        </template>
      </PCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAuthStore } from '@/stores/authStore'

import ProfileRow from '@/components/ProfileRow.vue'
import LocaleChanger from '@/components/LocaleChanger.vue'

const authStore = useAuthStore()
const username = computed(() => authStore.username)
</script>
