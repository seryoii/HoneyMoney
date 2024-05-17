import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import MapView from "@/views/MapView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/map",
    name: "MapView",
    component: MapView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
