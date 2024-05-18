<template>
  <div>
    
    <v-card class="mx-auto pa-8 pt-2 pb-4" elevation="8" max-width="448" rounded="lg">
      <v-img class="mx-auto my-6" max-width="228" :src="logo"></v-img>
      <v-form @submit.prevent="submitForm">
        <div class="text-subtitle-1 text-medium-emphasis">Username</div>

        <v-text-field v-model="state.username" @blur="v$.username.$touch" density="compact" placeholder="아이디" prepend-inner-icon="mdi-information" variant="outlined"></v-text-field>

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          Password

          <a class="text-caption text-decoration-none text-yellow-darken-3" href="#" rel="noopener noreferrer" target="_blank">비밀번호를 잊으셨나요?</a>
        </div>

        <v-text-field
          v-model="state.password"
          @blur="v$.password.$touch"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="비밀번호"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          @click:append-inner="visible = !visible"
        ></v-text-field>

        <v-btn type="submit" class="mb-8" color="yellow-darken-3" size="large" variant="tonal" block>Log In</v-btn>
      </v-form>
      <v-card-text class="text-center">
        <a class="text-yellow-darken-3 text-decoration-none" href="http://localhost:5173/signup" rel="noopener noreferrer">
          회원가입
          <v-icon icon="mdi-menu-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import useVuelidate from "@vuelidate/core";
import { required, minLength, maxLength, minValue } from "@vuelidate/validators";
import { useUserStore } from "@/stores/user";
import logo from "@/assets/logo_dev.png"
const visible = ref(false);

const userStore = useUserStore();
// 상태 정의
const state = ref({
  username: "",
  password: "",
});

// 유효성 검사 규칙 정의
const rules = {
  username: { required, maxLength: maxLength(20) },
  password: { required, maxLength: maxLength(128) },
};

// Vuelidate 훅 사용
const v$ = useVuelidate(rules, state);

function submitForm() {
  v$.value.$validate();
  if (!v$.value.$error) {
    // 유효성 검사를 통과한 경우 처리 로직
    const payload = {
      username: state.value.username,
      password: state.value.password,
    };
    userStore.loginUser(payload);
  } else {
    // 유효성 검사를 통과하지 못한 경우 처리 로직
    console.log("Form is invalid");
  }
}
</script>


