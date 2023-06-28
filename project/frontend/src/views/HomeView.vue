<script setup>

const solutions_list = [
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
    <h3 class="text-center mt-3 mb-3">Системы контроля доступа в Москве и Московской области для дома и вашего бизнеса
    </h3>
    <div class="d-flex justify-content-center mb-3">
      <MainBanner />
    </div>
    <h3 class="text-center mt-3 mb-3">Популярные решения (Рекомендуемые решения)</h3>

    <div class="d-flex flex-wrap  justify-content-center">
      <PopularSolutionsCard class="solution-card" v-for="solution in solutions_list" />
    </div>
    <h3 class="text-center mt-3 mb-3"> У нас большой ассортимент камер</h3>
    
    <ProductsCarousel class="mt-3 mb-3" />

    <div class="mt-5 mb-5">
      <h3 class="text-center mb-3">Примеры наших работ</h3>
      <WorkExamples />
    </div>
  </main>
</template>

<style scoped>
main {
  margin-left: 150px;
  margin-right: 150px;
}

.solution-card {
  margin: 10px;
}
</style>