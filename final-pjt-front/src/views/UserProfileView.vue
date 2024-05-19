<template>
  <v-container>
    <v-avatar :src="userStore.userProfile.profile_img" size="150"></v-avatar>
    <!-- <v-avatar :image="usersPicture" size="150"></v-avatar> -->
    <h1>유저 프로필 페이지</h1>
      <div v-if="userStore.userProfile">
        <p>유저 등록 ID : {{ userStore.userProfile.id }}</p>
        <p>유저 아이디 : {{ userStore.userProfile.username }}</p>
        <p>유저 닉네임 : {{ userStore.userProfile.nickname }}</p>
        <p>유저 최근 로그인 : {{ userStore.userProfile.last_login }}</p>
        <p>유저 이미지 링크 : {{ userStore.userProfile.profile_img }}</p>
        <p>유저 나이 : {{ userStore.userProfile.age }}</p>
        <p>유저 연봉 : {{ userStore.userProfile.salary }}</p>
        <p>유저 자산 : {{ userStore.userProfile.wealth }}</p>
        <p>유저 성향 : {{ userStore.userProfile.tendency }}</p>
        <p>유저 희망 기간 : {{ userStore.userProfile.desirePeriod }}</p>
      </div>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import usersPicture from "@/assets/users.jpg";
const userStore = useUserStore();
onMounted(() => {
  userStore.getProfile();
});
</script>

<style scoped></style>
