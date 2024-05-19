<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="auto">
        <v-tabs v-model="tab" color="#424242">
          <v-tab class="mx-4 font-weight-bold" value="one">Products</v-tab>
          <v-tab class="mx-4 font-weight-bold" value="two">Find Bank</v-tab>
          <v-tab class="mx-4 font-weight-bold" value="three">Exchange</v-tab>
          <v-tab class="ms-4 me-8 font-weight-bold" value="four">Recommend</v-tab>
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
        </v-tabs>
      </v-col>
    </v-row>
    <v-card-text>
      <v-carousel v-model="tab" hide-delimiters>
        <template v-slot:prev="{ props }">
          <v-btn class="invisible" color="" variant="elevated" @click="props.onClick"><</v-btn>
        </template>
        <template v-slot:next="{ props }">
          <v-btn class="invisible" color="" variant="elevated" @click="props.onClick">></v-btn>
        </template>
        <v-carousel-item value="one">
          <v-sheet class="ps-10 py-10 sheet-background-color-1 full-screen">
            <h1 class="text-white">세상엔 어떤 상품이 있을까?</h1>
            <h1 class="text-white">예금 적금 상품 알아보기</h1>
            <v-row justify="end">
              <v-col cols="4">
                <v-img class="click-event" @click="moveProducts" max-width="200" :src="savingPhoto"></v-img>
              </v-col>
            </v-row>
            <v-btn class="btn-1" @click="moveProducts" variant="tonal">상품 검색하러 가기</v-btn>
          </v-sheet>
        </v-carousel-item>
        <v-carousel-item value="two">
          <v-sheet class="ps-10 py-10 sheet-background-color-2 full-screen">
            <v-row justify="end">
              <v-col cols="6">
                <h1 class="text-white">퇴근하면 6시...</h1>
                <h1 class="text-white">내 주변 은행은 어디에?</h1>
              </v-col>
            </v-row>
            <v-img class="click-event" @click="moveFindBank" max-width="200" :src="mapPhoto"></v-img>
            <v-row justify="end">
              <v-col cols="3">
                <v-btn class="btn-2" @click="moveFindBank" variant="tonal">주변 은행 찾기</v-btn>
              </v-col>
            </v-row>
          </v-sheet>
        </v-carousel-item>
        <v-carousel-item value="three">
          <v-sheet class="ps-10 py-10 sheet-background-color-3 full-screen">
            <h1 class="text-white">환율이 싸다고?</h1>
            <h1 class="text-white">당장 여행 계획을 세워보자</h1>
            <v-row justify="end">
              <v-col cols="8">
                <v-img class="click-event" @click="moveExchange" max-width="200" :src="exchangePhoto"></v-img>
              </v-col>
            </v-row>
            <v-btn class="btn-3" @click="moveExchange" variant="tonal">환율 알아 보기</v-btn>
          </v-sheet>
        </v-carousel-item>
        <v-carousel-item value="four">
          <v-sheet class="ps-10 py-10 sheet-background-color-4 full-screen">
            <h1 class="text-white">어떤 상품을 가입해야하는지 모르겠다고?</h1>
            <h1 class="text-white">내 성향과 비슷한 금융 상품 추천!</h1>
            <v-img class="click-event" @click="moveRecommend" max-width="200" :src="recommendPhoto"></v-img>
            <v-btn class="btn-4" @click="moveRecommend" variant="tonal">금융 상품 추천 받기</v-btn>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </v-card-text>
  </v-container>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import mapPhoto from "@/assets/map.png";
import recommendPhoto from "@/assets/recommend.png";
import savingPhoto from "@/assets/saving.png";
import exchangePhoto from "@/assets/exchange.png";

const userStore = useUserStore();
const isLoggedIn = computed(() => userStore.isLogin);

const tab = ref("one");
const router = useRouter();

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
.text-center {
  text-align: center;
}
.sheet-background-color-1 {
  background-color: rgba(178, 115, 37, 0.452) !important;
  border-radius: 8px !important;
  width: 100% !important;
  padding: 20px;
  height: 100% !important;
}
.btn-1 {
  border-radius: 50px !important;
  color: rgb(77, 50, 17) !important;
  font-weight: bold !important;
  margin-bottom: 10px !important;
}
.sheet-background-color-2 {
  background-color: #8757219c !important;
  border-radius: 8px !important;
  padding: 20px;
  width: 100% !important;
  height: 100% !important;
}
.btn-2 {
  border-radius: 50px !important;
  color: #4a3012 !important;
  font-weight: bold !important;
}

.sheet-background-color-3 {
  background-color: #b97b359b !important;
  border-radius: 8px !important;
  padding: 20px;
  width: 100% !important;
  height: 100% !important;
}
.btn-3 {
  border-radius: 50px !important;
  color: #6d4921 !important;
  font-weight: bold !important;
}
.sheet-background-color-4 {
  background-color: #8d602e97 !important;
  border-radius: 8px !important;
  padding: 20px;
  width: 100% !important;
  height: 100% !important;
}
.btn-4 {
  border-radius: 50px !important;
  color: #553a1b !important;
  font-weight: bold !important;
}
.full-screen {
  width: 100%;
  height: 50vh;
  margin: 0;
}
.click-event {
  cursor: pointer;
}
.invisible {
  background-color: rgba(0, 0, 0, 0); /* 완전히 투명 */
  box-shadow: none;
  width: 70px !important;
  height: 70px !important;
  border-radius: 100%;
  color: rgba(0, 0, 0, 0.154); /* 버튼 텍스트 색상 */
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
