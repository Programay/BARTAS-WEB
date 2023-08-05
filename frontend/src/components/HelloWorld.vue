<template>
  <div>
    <h1 class="text-3xl font-bold underline">{{ props.data?.message }} Test</h1>
    <PButton label="Submit" icon="pi pi-user"></PButton>
  </div>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { reactive, onMounted } from 'vue'

interface Response {
  message: string
}
interface StateResponse {
  data: Response | null
}
const props: StateResponse = reactive({
  data: null
})

const getMessage = () => {
  axios
    .get('/')
    .then((res) => {
      console.log(res.data)
      props.data = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}
onMounted(() => {
  getMessage()
})
</script>
