<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <NavBar />
    <RouterView />
    <Footer />

  </header>
</template>

<style scoped></style>
