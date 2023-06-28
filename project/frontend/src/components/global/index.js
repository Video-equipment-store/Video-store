import MainBanner from "./MainBanner.vue";
import ProductCard from "./ProductCard.vue";

const components = [
  { name: "MainBanner", component: MainBanner },
  { name: "ProductCard", component: ProductCard },
];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
