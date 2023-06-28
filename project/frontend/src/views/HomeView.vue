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
    <main>
      <div class="d-flex justify-content-center">
        <MainBanner />
      </div>

      <div class="popular-solutions d-flex flex-wrap  justify-content-center">
        <PopularSolutionsCard class="solution-card" v-for="solution in solutions_list" />
      </div>

      <div class="range-of-cameras">
        <ProductsCarousel/>
      </div>

      <div class="work-exaples mt-3">
        <h3 class="text-center mb-3">Примеры наших работ</h3>
        <WorkExamples />
      </div>


    </main>


  </main>
</template>

<style scoped>
.popular-solutions {
  margin: 50px;
}

.solution-card {
  margin: 10px;
}
.range-of-cameras{
  margin-left: 150px;
  margin-right: 150px;
}
.work-exaples{
  margin-left: 150px;
  margin-right: 150px;
}
</style>