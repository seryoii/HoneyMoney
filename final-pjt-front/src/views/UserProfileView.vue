<template>
  <v-container>
    <v-container v-if="userStore.userProfile">
      <v-card :disabled="loading" :loading="loading" class="mx-auto my-12" max-width="374">
        <template v-slot:loader="{ isActive }">
          <v-progress-linear :active="isActive" color="deep-purple" height="4" indeterminate></v-progress-linear>
        </template>
        <v-container class="mt-3" align="center">
          <v-avatar :image="profileImg" size="200" alt="User Profile Image" cover></v-avatar>
          <v-card-title class="mt-3 ibm-plex-sans-kr-bold"><h2>{{ userStore.userProfile.nickname }} 님</h2></v-card-title>
          <v-card-text class="ibm-plex-sans-kr-bold"><h3>{{ userStore.userProfile.username }} (만 {{ userStore.userProfile.age }}세)</h3></v-card-text>
        </v-container>

        <v-divider class="mx-4 mb-1"></v-divider>

        <!-- <v-container>
          <v-card-title class="ibm-plex-sans-kr-bold"><h4>내 정보</h4></v-card-title>
          <v-card-text>아이디 : {{ userStore.userProfile.username }}</v-card-text>
          <v-card-text>나이 : {{ userStore.userProfile.age }}</v-card-text>
        </v-container> -->

        
        <v-container>
          <v-card-title class="ibm-plex-sans-kr-bold"><h4>나의 금융 정보</h4></v-card-title>

          <div class="px-4 mb-2">
              <v-chip>나의 연봉 : {{ userStore.userProfile.salary }}</v-chip>

              <v-chip>나의 자산 : {{ userStore.userProfile.wealth }}</v-chip>

              <v-chip>나의 저축 성향 : {{ userStore.userProfile.tendency }}</v-chip>

              <v-chip>나의 저축 희망 기간 : {{ userStore.userProfile.desirePeriod }}</v-chip>
          </div>
        </v-container>

        <v-card-actions>
      <v-container class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
          <template v-slot:activator="{ props: activatorProps }">
            <v-btn v-bind="activatorProps" color="yellow-darken-3" prepend-icon="mdi-account" variant="tonal" text="Edit Profile" block border @click="reserve"></v-btn>
          </template>
          <v-card prepend-icon="mdi-account" title="User Profile">
            <v-card-text>
              <v-form @submit.prevent="submitForm">
                <v-row dense>
                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Nickname*" v-model="form.nickname" required></v-text-field>
                  </v-col>

                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Age*" type="number" v-model="form.age" required></v-text-field>
                  </v-col>

                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Salary*" type="number" v-model="form.salary" required></v-text-field>
                  </v-col>

                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Wealth*" type="number" v-model="form.wealth" required></v-text-field>
                  </v-col>

                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Password*" type="password" v-model="form.password1" required></v-text-field>
                  </v-col>

                  <v-col cols="12" md="4" sm="6">
                    <v-text-field label="Confirm Password*" type="password" v-model="form.password2" required></v-text-field>
                  </v-col>

                  <v-col cols="12" sm="6">
                    <v-select :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" label="Tendency*" v-model="form.tendency" required></v-select>
                  </v-col>

                  <v-col cols="12" sm="6">
                    <v-select :items="[6, 12, 24, 36]" label="Desire Period*" v-model="form.desirePeriod" required></v-select>
                  </v-col>

                  <v-col cols="12">
                    <v-file-input prepend-icon="mdi-camera" label="Profile Image" accept="image/" v-model="form.profile_img"></v-file-input>
                  </v-col>
                </v-row>
                <small class="text-caption text-medium-emphasis">*indicates required field</small>
              </v-form>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

              <v-btn color="primary" text="Save" variant="tonal" @click="submitForm"></v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-card-actions>
  </v-card>
      <!-- <v-avatar :image="profileImg" size="150" alt="User Profile Image"></v-avatar>
      <p>유저 등록 ID : {{ userStore.userProfile.id }}</p>
      <p>유저 아이디 : {{ userStore.userProfile.username }}</p>
      <p>유저 닉네임 : {{ userStore.userProfile.nickname }}</p>
      <p>유저 최근 로그인 : {{ userStore.userProfile.last_login }}</p>
      <p>유저 이미지 링크 : {{ userStore.userProfile.profile_img }}</p>
      <p>유저 나이 : {{ userStore.userProfile.age }}</p>
      <p>유저 연봉 : {{ userStore.userProfile.salary }}</p>
      <p>유저 자산 : {{ userStore.userProfile.wealth }}</p>
      <p>유저 성향 : {{ userStore.userProfile.tendency }}</p>
      <p>유저 희망 기간 : {{ userStore.userProfile.desirePeriod }}</p> -->
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const dialog = ref(false);
const userStore = useUserStore();
const form = ref({
  nickname: `${userStore.userProfile.nickname}`,
  age: `${userStore.userProfile.age}`,
  salary: `${userStore.userProfile.salary}`,
  wealth: `${userStore.userProfile.wealth}`,
  password1: `${userStore.userProfile.password1}`,
  password2: `${userStore.userProfile.password2}`,
  tendency: `${userStore.userProfile.tendency}`,
  desirePeriod: `${userStore.userProfile.desirePeriod}`,
  profile_img: null, // 프로필 이미지
});

const profileImg = computed(() => {
  return `http://localhost:8000${userStore.userProfile.profile_img}`;
});

const submitForm = async () => {
  const formData = new FormData();
  formData.append("nickname", form.value.nickname);
  formData.append("age", form.value.age);
  formData.append("salary", form.value.salary);
  formData.append("wealth", form.value.wealth);
  formData.append("password1", form.value.password1);
  formData.append("password2", form.value.password2);
  formData.append("tendency", form.value.tendency);
  formData.append("desirePeriod", form.value.desirePeriod);
  if (form.value.profile_img) {
    formData.append("profile_img", form.value.profile_img);
  }
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${userStore.userProfile.username}/`,
    data: formData,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      dialog.value = false;
      userStore.getProfile(); // 업데이트된 프로필을 다시 가져옵니다.
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>


</style>
