import MainBanner from "./MainBanner.vue";
import PopularSolutionsCard from "./PopularSolutionsCard.vue";
import ProductsCarousel from "./ProductsCarousel.vue";
import ProductCard from "./ProductCard.vue";

const components = [
  { name: "MainBanner", component: MainBanner },
  { name: "PopularSolutionsCard", component: PopularSolutionsCard },
  { name: "ProductsCarousel", component: ProductsCarousel },
  { name: "ProductCard", component: ProductCard },
];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
