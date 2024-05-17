import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import MapView from "@/views/MapView.vue";
import SignupView from "@/views/SignupView.vue";

const routes = [
  {
    path: "/",
    name: "MainView",
    component: MainView,
  },
  {
    path: "/map",
    name: "MapView",
    component: MapView,
  },
  {
    path: "/signup",
    name: "SignupView",
    component: SignupView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
