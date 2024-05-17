<template>
  <v-app>
    <v-main>
      <RouterLink :to="{ name: 'MapView' }">MapView</RouterLink>
      |
      <RouterLink :to="{ name: 'SignupView' }">SignupView</RouterLink>

      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
import MapView from "@/views/MapView.vue";
import MainView from "@/views/MainView.vue";
import SignupView from "./views/SignupView.vue";
import { RouterLink, RouterView } from "vue-router";

export default {
  name: "App",

  components: {
    MainView,
    MapView,
    SignupView,
  },
};
</script>
