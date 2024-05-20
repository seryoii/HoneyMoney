<template>
  <v-container>
    <v-container v-if="userStore.userProfile">
      <v-container class="pa-4 text-center">
        <v-dialog v-model="dialog" max-width="600">
          <template v-slot:activator="{ props: activatorProps }">
            <v-btn class="text-none font-weight-regular" prepend-icon="mdi-account" text="Edit Profile" variant="tonal" v-bind="activatorProps"></v-btn>
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
      <v-avatar :image="profileImg" size="150" alt="User Profile Image"></v-avatar>
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
