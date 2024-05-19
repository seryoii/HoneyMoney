<template>
  <v-app>
    <v-main v-if="!isMainView" class="app-background">
      <v-row class="mt-6 d-flex justify-center align-center">
        <v-col cols="auto" class="py-0">
          <v-img class="cursor" @click="mainMove" :src="logo" width="150"></v-img>
        </v-col>
      </v-row>
      <v-container class="mx-auto under-bar"></v-container>
      <v-container>
        <v-row justify="center">
          <v-col class="py-6" cols="auto">
            <v-tab class="mx-4 font-weight-bold" value="one" @click="moveProducts">Products</v-tab>
            <v-tab class="mx-4 font-weight-bold" value="two" @click="moveFindBank">Find Bank</v-tab>
            <v-tab class="mx-4 font-weight-bold" value="three" @click="moveExchange">Exchange</v-tab>
            <v-tab class="ms-4 me-8 font-weight-bold" value="four" @click="moveRecommend">Recommend</v-tab>
            <v-menu class="mx-4" v-if="more.length">
              <template v-slot:activator="{ props }">
                <v-btn class="align-self-center font-weight-bold" height="100%" rounded="0" variant="plain" v-bind="props">
                  more
                  <v-icon icon="mdi-menu-down" end></v-icon>
                </v-btn>
              </template>
              <v-list class="bg-grey-lighten-3">
                <v-list-item v-for="item in more" :key="item" :title="item" @click="handleMoreClick(item)"></v-list-item>
              </v-list>
            </v-menu>
          </v-col>
        </v-row>
        <RouterView />
      </v-container>
    </v-main>
    <v-main v-else class="app-background">
      <v-row class="mt-6 d-flex justify-center align-center">
        <v-col cols="auto" class="py-0">
          <v-img class="cursor" @click="mainMove" :src="logo" width="150"></v-img>
        </v-col>
      </v-row>
      <v-container class="mx-auto under-bar"></v-container>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup>
import { useUserStore } from "./stores/user";
import { useRouter, useRoute, RouterLink, RouterView } from "vue-router";
import { ref, computed } from "vue";

const userStore = useUserStore();
import logo from "@/assets/logo_dev.png";
const router = useRouter();
const mainMove = function () {
  router.push({ name: "MainView" });
};
const route = useRoute();
const isMainView = computed(() => route.name === "MainView");

const isLoggedIn = computed(() => userStore.isLogin);

const moveProducts = () => {
  router.push({ name: "ProductsView" });
};
const moveFindBank = () => {
  router.push({ name: "MapView" });
};
const moveExchange = () => {
  router.push({ name: "ExchangeView" });
};
const moveRecommend = () => {
  router.push({ name: "RecommendView" });
};

const more = computed(() => {
  return isLoggedIn.value ? ["COMMUNITY", "PROFILE", "LOGOUT"] : ["LOGIN", "SIGNUP"];
});

const handleMoreClick = (item) => {
  switch (item) {
    case "SIGNUP":
      router.push({ name: "SignupView" });
      break;
    case "LOGIN":
      router.push({ name: "LoginView" });
      break;
    case "LOGOUT":
      userStore.logoutUser();
      break;
    case "PROFILE":
      router.push({ name: "UserProfileView" });
      break;
    case "COMMUNITY":
      router.push({ name: "CommunityView" });
      break;
  }
};
</script>

<style>
.navbar-text {
  text-decoration: none;
  color: black;
  font-weight: bold;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande", "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}
.app-background {
  background-color: rgba(253, 248, 222, 0.658);
  height: 100%;
  height: inherit;
}

.font {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande", "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}

.under-bar {
  border-bottom: 1.5px solid rgba(148, 111, 94, 0.531);
}
.cursor {
  cursor: pointer;
}
</style>
