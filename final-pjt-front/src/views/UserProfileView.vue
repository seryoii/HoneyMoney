<template>
  <div v-if="isLoading" class="loading-screen">
    <v-container fill-height align="center" justify="center">
      <v-progress-circular :model-value="value" :rotate="360" :size="100" :width="15" color="amber">
        <template v-slot:default>{{ value }} %</template>
      </v-progress-circular>
    </v-container>
  </div>
  <v-container v-else v-if="userStore.userProfile">
    <v-card class="mx-auto py-5">
      <v-row>
        <v-col cols="6">
          <v-container class="mt-3" align="center">
            <v-avatar :image="profileImg" size="200" alt="User Profile Image" cover></v-avatar>
            <v-card-title class="mt-3 ibm-plex-sans-kr-bold">
              <h2>{{ userStore.userProfile.nickname }} 님</h2>
            </v-card-title>
            <v-card-text class="ibm-plex-sans-kr-bold">
              <h3>{{ userStore.userProfile.username }} (만 {{ userStore.userProfile.age }}세)</h3>
            </v-card-text>
          </v-container>
          <v-col class="text-center">
            <v-container>
              <v-card-title class="ibm-plex-sans-kr-bold"><h4>나의 금융 정보</h4></v-card-title>
              <div class="px-4 mb-2">
                <v-chip class="chip-style mx-1 my-1">나의 연봉 : {{ new Intl.NumberFormat("ko-KR", { style: "currency", currency: "KRW" }).format(userStore.userProfile.salary) }}</v-chip>
                <v-chip class="chip-style mx-1 my-1">나의 자산 : {{ new Intl.NumberFormat("ko-KR", { style: "currency", currency: "KRW" }).format(userStore.userProfile.wealth) }}</v-chip>
                <v-chip class="chip-style mx-1 my-1">나의 저축 성향 : {{ userStore.userProfile.tendency }}</v-chip>
                <v-chip class="chip-style mx-1 my-1">나의 저축 희망 기간 : {{ userStore.userProfile.desirePeriod }}개월</v-chip>
              </div>
            </v-container>
          </v-col>
          <v-card-actions>
            <v-container class="pa-4 text-center">
              <v-dialog v-model="dialog" max-width="600">
                <template v-slot:activator="{ props: activatorProps }">
                  <v-btn v-bind="activatorProps" color="yellow-darken-3" prepend-icon="mdi-account" variant="tonal" text="Edit Profile" block border></v-btn>
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
                          <v-select :items="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" label="Tendency*" v-model="form.tendency" required></v-select>
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
        </v-col>
        <v-col class="px-0 mx-0" cols="6">
          <v-row class="px-0 mx-0">
            <v-col class="d-flex align-center justify-center px-0 mx-0 mb-0">
              <v-container v-if="depositStore.profileDepositData.length" class="py-0 mb-0">
                <v-row justify="end">
                  <v-col class="ms-4" cols="2">
                    <v-badge color="yellow" :content="depositStore.profileDepositData.length"></v-badge>
                    <v-img :src="jar" max-width="50"></v-img>
                  </v-col>
                  <v-row class="py-0 my-0" align="end">
                    <v-col class="mx-0 py-0 my-2 px-0" cols="7">
                      <h2 class="font-weight-black ibm-plex-sans-kr-regular">꿀바른 예금</h2>
                    </v-col>
                  </v-row>
                </v-row>
                <v-carousel height="300" show-arrows="hover" hide-delimiters>
                  <v-carousel-item v-for="(honeyDeposit, index) in depositStore.profileDepositData" :key="`carousel1-${index}`" class="no-padding">
                    <v-card class="mx-16 fill-height d-flex align-center justify-center" elevation="0">
                      <v-card class="card-design mb-2 density-compact" prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg" variant="text">
                        <template v-slot:subtitle>
                          <span class="ibm-plex-sans-kr-regular">{{ honeyDeposit.kor_co_nm }}</span>
                        </template>
                        <template v-slot:title>
                          <span class="font-weight-black ibm-plex-sans-kr-regular">
                            <h4>{{ honeyDeposit.fin_prdt_nm }}</h4>
                          </span>
                        </template>
                        <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular">가입 방법 : {{ honeyDeposit.join_way }}</v-card-text>
                        <v-card-text class="ibm-plex-sans-kr-regular">만기 후 이자율 : {{ honeyDeposit.mtrt_int }}</v-card-text>
                        <v-container align="center">
                          <v-btn color="yellow-darken-3" variant="tonal">Details</v-btn>
                        </v-container>
                      </v-card>
                    </v-card>
                  </v-carousel-item>
                </v-carousel>
              </v-container>
              <v-container v-else class="px-0 mx-0">
                <p>꿀발라보세요~</p>
              </v-container>
            </v-col>
          </v-row>
          <v-row class="py-0 my-0">
            <v-col class="d-flex align-center justify-center py-0 my-0">
              <v-container class="py-0 mb-0" v-if="savingStore.profileSavingData.length">
                <v-row justify="end">
                  <v-col class="ms-4" cols="2">
                    <v-badge color="yellow" :content="savingStore.profileSavingData.length"></v-badge>
                    <v-img :src="jar" max-width="50"></v-img>
                  </v-col>
                  <v-row class="py-0 my-0" align="end">
                    <v-col class="mx-0 py-0 my-2 px-0" cols="7">
                      <h2 class="font-weight-black ibm-plex-sans-kr-regular">꿀바른 적금</h2>
                    </v-col>
                  </v-row>
                </v-row>
                <v-carousel height="300" show-arrows="hover" hide-delimiters>
                  <v-carousel-item v-for="(honeySaving, index) in savingStore.profileSavingData" :key="`carousel2-${index}`" class="no-padding">
                    <v-card class="mx-16 fill-height d-flex align-center justify-center" elevation="0">
                      <v-card class="card-design mb-2 density-compact" prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg" variant="text">
                        <template v-slot:subtitle>
                          <span class="ibm-plex-sans-kr-regular">{{ honeySaving.kor_co_nm }}</span>
                        </template>
                        <template v-slot:title>
                          <span class="font-weight-black ibm-plex-sans-kr-regular">
                            <h4>{{ honeySaving.fin_prdt_nm }}</h4>
                          </span>
                        </template>
                        <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular">가입 방법 : {{ honeySaving.join_way }}</v-card-text>
                        <v-card-text class="ibm-plex-sans-kr-regular">만기 후 이자율 : {{ honeySaving.mtrt_int }}</v-card-text>
                        <v-container align="center">
                          <v-btn color="yellow-darken-3" variant="tonal">Details</v-btn>
                        </v-container>
                      </v-card>
                    </v-card>
                  </v-carousel-item>
                </v-carousel>
              </v-container>
              <v-container v-else class="px-0 mx-0">
                <p>꿀발라보세요~</p>
              </v-container>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import jar from "@/assets/jar.png";
const depositStore = useDepositStore();
const savingStore = useSavingStore();
const userStore = useUserStore();

const isLoading = ref(true);
const value = ref(0);
const interval = ref(-1);

onMounted(() => {
  userStore.getProfile();
  checkDeposit();
  checkSaving();
  // 프로그레스 서클 업데이트
  interval.value = setInterval(() => {
    if (value.value === 100) {
      value.value = 100;
    } else {
      value.value += 10;
    }
  }, 200);

  // 3-5초 후에 로딩을 false로 설정합니다.
  setTimeout(() => {
    isLoading.value = false;
    clearInterval(interval.value);
  }, 3000); // 여기서는 3초로 설정
});

// 꿀바른 상품 확인 함수
const checkDeposit = function () {
  depositStore.getProfileDeposit(userStore.userProfile.interest_deposit);
  console.log(userStore.userProfile.interest_deposit);
};

const checkSaving = function () {
  savingStore.getProfileSaving(userStore.userProfile.interest_saving);
  console.log(userStore.userProfile.interest_saving);
};

const dialog = ref(false);
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

// 여기서 axios로 불러와서 연결해보자. 아니면 로그인 했을 때, 배열을 미리 받아두면 되지 않을까?
</script>

<style scoped>
.loading-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 24px;
}

.chip-style {
  cursor: pointer;
}
.chip-style:hover {
  background-color: rgba(255, 162, 0, 0.199);
}

.card-design {
  border-radius: 8px;
  background-color: rgba(255, 234, 0, 0.171);
}
</style>
