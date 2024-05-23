<template>
  <v-app>
    <v-main
      v-if="!isMainView"
      class="app-background"
      style="position: relative"
    >
      <v-row class="mt-6 d-flex justify-center align-center">
        <v-col cols="auto" class="py-0">
          <v-img
            class="cursor"
            @click="mainMove"
            :src="logo"
            width="200"
          ></v-img>
        </v-col>
      </v-row>
      <v-container class="mx-auto under-bar"></v-container>
      <v-container>
        <v-row justify="center">
          <v-col class="py-6" cols="auto">
            <v-tab
              class="mx-4 font-weight-bold"
              value="one"
              @click="moveProducts"
              >Products</v-tab
            >
            <v-tab
              class="mx-4 font-weight-bold"
              value="two"
              @click="moveFindBank"
              >Find Bank</v-tab
            >
            <v-tab
              class="mx-4 font-weight-bold"
              value="three"
              @click="moveExchange"
              >Exchange</v-tab
            >
            <v-tab
              class="ms-4 me-8 font-weight-bold"
              value="four"
              @click="moveRecommend"
              >Recommend</v-tab
            >
            <v-menu class="mx-4" v-if="more.length">
              <template v-slot:activator="{ props }">
                <v-btn
                  class="align-self-center font-weight-bold"
                  height="100%"
                  rounded="0"
                  variant="plain"
                  v-bind="props"
                >
                  more
                  <v-icon icon="mdi-menu-down" end></v-icon>
                </v-btn>
              </template>
              <v-list class="bg-grey-lighten-3">
                <v-list-item
                  v-for="item in more"
                  :key="item"
                  :title="item"
                  @click="handleMoreClick(item)"
                ></v-list-item>
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
          <v-img
            class="cursor"
            @click="mainMove"
            :src="logo"
            width="200"
          ></v-img>
        </v-col>
      </v-row>
      <v-container class="mx-auto under-bar"></v-container>
      <RouterView />
    </v-main>

    <!-- 챗봇 -->
    <Transition name="bounce">
      <v-card
        v-show="expand"
        style="position: fixed; bottom: 130px; right: 50px; z-index: 1000"
        class="mx-auto bg-secondary expand-component"
        height="600"
        width="400"
      >
        <ChatbotComponent /> </v-card
    ></Transition>
    <p class="chatbot-info ibm-plex-sans-kr-regular">AI챗봇에게 물어보세요!</p>
    <v-avatar
      @click="expand = !expand"
      class="chatbot-btn"
      size="90"
      color="transparent"
    >
      <v-img :src="chatbot"></v-img>
    </v-avatar>
  </v-app>
</template>

<script setup>
import { useUserStore } from "./stores/user";
import { useRouter, useRoute, RouterLink, RouterView } from "vue-router";
import { ref, computed } from "vue";
import swal from "sweetalert";
import ChatbotComponent from "@/components/ChatbotComponent.vue";
import chatbot from "@/assets/chatbot3.png";

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
  router.push({ name: "ProductsPreView" });
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
  return isLoggedIn.value
    ? ["COMMUNITY", "PROFILE", "LOGOUT"]
    : ["LOGIN", "SIGNUP"];
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
      swal({
        title: "오늘도 달달한 하루가 되었나요?",
        text: "꿀단지는 오늘도 숙성중입니다.",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((willDelete) => {
        if (willDelete) {
          swal("다음에 또 봐요!", {
            icon: "success",
          });
          userStore.logoutUser();
        } else {
          swal("더 둘러보다 가세요!");
        }
      });

      break;
    case "PROFILE":
      router.push({ name: "UserProfileView" });
      break;
    case "COMMUNITY":
      router.push({ name: "CommunityView" });
      break;
  }
};
const expand = ref(false);
</script>

<style>
.navbar-text {
  text-decoration: none;
  color: black;
  font-weight: bold;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}
.app-background {
  background-color: rgba(253, 248, 222, 0.658);
  height: 100%;
  height: inherit;
}

.font {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}

.under-bar {
  border-bottom: 1.5px solid rgba(148, 111, 94, 0.531);
}
.cursor {
  cursor: pointer;
}

.expand-container {
  text-align: right;
  position: fixed;
  bottom: 20px; /* 원하는 위치로 조절하세요 */
  right: 20px; /* 원하는 위치로 조절하세요 */
  z-index: 1000; /* 다른 요소 위로 배치되도록 설정 */
}
.expand-component {
  position: fixed;
  bottom: 20px; /* 원하는 위치로 조절하세요 */
  right: 20px; /* 원하는 위치로 조절하세요 */
  z-index: 1000; /* 다른 요소 위로 배치되도록 설정 */
}
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0.5);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

.chatbot-btn {
  /* background-color: rgba(253, 248, 222, 0.658); */
  position: fixed;
  bottom: 50px;
  right: 100px;
  z-index: 1000;
  padding: 10px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.chatbot-btn:hover {
  transform: translateY(-5px);
}

.chatbot-info {
  color: grey;
  font-size: 14px;
  position: fixed;
  bottom: 35px;
  right: 75px;
  z-index: 1000;
}
</style>
