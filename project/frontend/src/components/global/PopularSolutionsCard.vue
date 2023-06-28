<script setup>
function get_color() {
    const collors = ['green', 'blue', 'grey', 'yellow']
    return collors[Math.floor(Math.random() * collors.length)];
}
</script>

<template>
    <div class="solution-card" :style="{ background: get_color() }">
        <h4 class="text-center">Предложение "базовая безопасность"</h4>
        <img class="rounded mx-auto d-block" width="150px" src="/base-solution.svg">
        <div>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic, delectus?</p>
        </div>
        <div class="d-flex justify-content-between">
            <button class="btn btn-success btn-sm p-1">В калькулятор</button>
            <button class="btn btn-info btn-sm p-1">Заказать звонок</button>
        </div>

    </div>
</template>

<style scoped>
.solution-card {
    border-radius: 25px;
    /* background: #2138ad83; */
    padding: 20px;
    width: 270px;
    height: 400px;
}
</style>