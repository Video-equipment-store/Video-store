<script setup>
import router from '../router'

</script>

<template>
    <nav>
        <div class="nav-content">
            <div class="row">
                <div class="col nav-content-item">
                    <img src="/lable.svg">
                </div>
                <div class="col nav-content-item">
                    <span>Слоган/другой текст</span>
                </div>
                <div class="col nav-content-item">
                    <span>+7-999-999-99-99</span>
                </div>
                <div class="col nav-content-item">
                    <div class="d-flex justify-content-between">
                        <img class="nav-icon" src="/icon-phone.svg">
                        <img class="nav-icon" src="/icon-wp.svg">
                        <img class="nav-icon" src="/icon-telega.svg">
                    </div>
                </div>
                <div class="col nav-content-item">
                    <button class="btn nav-submit-btn">Оставить заявку</button>
                </div>

            </div>
            <div class="d-flex justify-content-between">
                <button type="button" class="btn btn-outline-secondary" @click="router.push({ name: 'home' })">Главная</button>
                <button type="button" class="btn btn-outline-secondary">Видеонаблюдение</button>
                <button type="button" class="btn btn-outline-secondary">Домофония</button>
                <button type="button" class="btn btn-outline-secondary">Контроль</button>
                <button type="button" class="btn btn-outline-secondary">Наши работы</button>

                <button type="button" class="btn btn-outline-secondary" @click="router.push({ name: 'about' })">О компании</button>

            </div>
        </div>

    </nav>
</template>

<style scoped>
.nav-content {
    margin-left: 80px;
    margin-right: 80px;
    border: 1px solid;
}

.nav-content-item {
    margin: 5px;
}

.nav-icon {
    max-width: 30px;
    max-height: 30px;
}

.nav-submit-btn {
    background-color: yellow;
}
</style>
