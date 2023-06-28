<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <NavBar />
    <hr>
    <h3>
      <RouterLink to="/">Home</RouterLink>
    </h3>
    <h3>
      <RouterLink to="/about">About</RouterLink>
    </h3>
    <hr>
    <RouterView />
    <hr>
    <Footer />

  </header>
</template>

<style scoped></style>
