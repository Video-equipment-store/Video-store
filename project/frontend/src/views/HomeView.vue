<script setup>

const product_list = [
  { id: 1, name: "Product1" },
  { id: 2, name: "Product2" },
  { id: 3, name: "Product3" },
  { id: 4, name: "Product4" },
  { id: 5, name: "Product5" },
  { id: 6, name: "Product6" }
]

</script>

<template>
  <main>
    <main>
      <div class="d-flex justify-content-center">
        <MainBanner />
      </div>

      <div class="product-cards d-flex flex-wrap  justify-content-center">
        <ProductCard class="product-card" v-for="product in product_list" />
      </div>


    </main>


  </main>
</template>

<style scoped>
.product-cards {
  margin: 50px;
}

.product-card {
  margin: 10px;
}
</style>