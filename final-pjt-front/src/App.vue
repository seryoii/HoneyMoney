<template>
  <v-app>
    <v-main>
      <RouterLink :to="{ name: 'MapView' }">Map</RouterLink>
      |
      <RouterLink :to="{ name: 'SignupView' }">Signup</RouterLink>
      |
      <RouterLink :to="{ name: 'LoginView' }">Login</RouterLink>
      |
      <a @click="userStore.logoutUser">Logout</a>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup>
import { useUserStore } from "./stores/user";
import { RouterLink, RouterView } from "vue-router";
const userStore = useUserStore();
</script>
