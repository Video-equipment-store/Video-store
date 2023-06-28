<script setup>
import { defineComponent } from 'vue'
import { Carousel, Navigation, Slide } from 'vue3-carousel'

import 'vue3-carousel/dist/carousel.css'


</script>
<template>
  <Carousel :items-to-show="3.5" :wrap-around="true">
    <Slide class="m-3" v-for="slide in 10" :key="slide">
      <ProductCard />
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<style scoped>

</style>