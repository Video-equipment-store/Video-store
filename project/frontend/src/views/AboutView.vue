<script setup>
import { ref, reactive } from 'vue'

const objectOfAttrs = ref({
  id: 'container',
  class: 'wrapper'
})
const off = () => {
  objectOfAttrs.value = false
  console.log(objectOfAttrs)
}
const message = "hello world"
const seen = ref(true)
</script>

<template>
  <main>
    <div class="d-flex justify-content-center">
      <div>
        <h4 class="text-center">About view</h4>
        {{ message.split('').reverse().join('') }}
        <!-- <h3>{{ new Date(2011, 0, 1, 0, 0, 0, 0) }}</h3> -->
        <button @click="seen = !seen">seen</button>
        <p v-if="seen">Now you see me</p>

      </div>

    </div>

  </main>
</template>
