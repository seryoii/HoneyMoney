<template>
  <v-app>
    <v-main>
      <RouterLink :to="{ name: 'MainView' }">Main </RouterLink>
      <RouterLink :to="{ name: 'ProductsView' }">| Products </RouterLink>
      <RouterLink :to="{ name: 'CommunityView' }">| Community </RouterLink>
      <RouterLink :to="{ name: 'ExchangeView' }">| Exchange </RouterLink>
      <RouterLink :to="{ name: 'UserProfileView' }">| Profile </RouterLink>
      <RouterLink :to="{ name: 'MapView' }">| Map </RouterLink>
      <RouterLink v-if="!userStore.isLogin" :to="{ name: 'SignupView' }">| Signup </RouterLink>
      <RouterLink v-if="!userStore.isLogin" :to="{ name: 'LoginView' }">| Login </RouterLink>
      <a v-if="userStore.isLogin" @click="userStore.logoutUser">| Logout </a>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup>
import { useUserStore } from "./stores/user";
import { RouterLink, RouterView } from "vue-router";
const userStore = useUserStore();
</script>
