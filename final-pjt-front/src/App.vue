<template>
  <v-app>
    <v-main class="app-background">
      <RouterLink class="navbar-text" :to="{ name: 'MainView' }">Main</RouterLink>
      <RouterLink class="navbar-text" :to="{ name: 'ProductsView' }">| Products</RouterLink>
      <RouterLink class="navbar-text" :to="{ name: 'CommunityView' }">| Community</RouterLink>
      <RouterLink class="navbar-text" :to="{ name: 'ExchangeView' }">| Exchange</RouterLink>
      <RouterLink class="navbar-text" :to="{ name: 'UserProfileView' }">| Profile</RouterLink>
      <RouterLink class="navbar-text" :to="{ name: 'MapView' }">| Map</RouterLink>
      <RouterLink class="navbar-text" v-if="!userStore.isLogin" :to="{ name: 'SignupView' }">| Signup</RouterLink>
      <RouterLink class="navbar-text" v-if="!userStore.isLogin" :to="{ name: 'LoginView' }">| Login</RouterLink>
      <a class="navbar-text" v-if="userStore.isLogin" @click="userStore.logoutUser">| Logout</a>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup>
import { useUserStore } from "./stores/user";
import { RouterLink, RouterView } from "vue-router";
import logo from "@/assets/logo.png";
const userStore = useUserStore();
</script>

<style>
.navbar-text {
  text-decoration: none;
  color: black;
  font-weight: bold;
}
.app-background {
  background-color: rgba(253, 248, 222, 0.658);
  min-height: 100vh;
}
</style>
