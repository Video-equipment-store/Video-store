<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <h1>Hello world</h1>
    <h3>
      <RouterLink to="/">Home</RouterLink>
    </h3>
    <h3>
      <RouterLink to="/about">About</RouterLink>
    </h3>

  </header>

  <RouterView />
</template>

<style scoped></style>
