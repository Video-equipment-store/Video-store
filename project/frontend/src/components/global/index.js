import ExampleCard from "./ExampleCard.vue";

const components = [{ name: "ExampleCard", component: ExampleCard }];

export default {
  install(app) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
