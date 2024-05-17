<template>
  <v-app>
    <v-main>
      <RouterLink :to="{ name: 'MapView' }">Map</RouterLink>
      |
      <RouterLink :to="{ name: 'SignupView' }">Signup</RouterLink>
      |
      <RouterLink :to="{ name: 'LoginView' }">Login</RouterLink>

      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
import MapView from "@/views/MapView.vue";
import MainView from "@/views/MainView.vue";
import SignupView from "@/views/SignupView.vue";
import LoginView from "@/views/LoginView.vue";
import { RouterLink, RouterView } from "vue-router";

export default {
  name: "App",

  components: {
    MainView,
    MapView,
    SignupView,
    LoginView,
  },
};
</script>
