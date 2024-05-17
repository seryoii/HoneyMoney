<template>
  <v-app>
    <v-main>
      <RouterLink :to="{ name: 'About' }">About</RouterLink>
      <RouterLink :to="{ name: 'MapView' }">MapView</RouterLink>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
import About from "@/views/About.vue";
import MapView from "@/views/MapView.vue";
import { RouterLink, RouterView } from "vue-router";

export default {
  name: "App",

  components: {
    About,
    MapView,
  },
};
</script>
