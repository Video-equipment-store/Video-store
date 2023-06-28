<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <main class="main-content">
    <NavBar />
    <RouterView />
    <Footer />

  </main>
</template>

<style scoped>
.main-content{
  background-color: rgba(121, 121, 125, 0.492);
}
</style>
