<template>
  <div>
    <p>Test: {{ msg }}</p>
  </div>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
let msg = ref('')
const getMessage = () => {
  axios
    .get('/')
    .then((res) => {
      console.log(res.data)
      msg.value = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}
onMounted(() => {
  getMessage()
})
</script>
