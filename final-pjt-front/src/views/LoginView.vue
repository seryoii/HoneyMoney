<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="username">Username</label>
      <input id="username" v-model="state.username" @blur="v$.username.$touch" />
      <span v-if="v$.username.$error">Username is required and must be at least 20 characters long</span>
    </div>
    <div>
      <label for="password">Password</label>
      <input id="password" type="password" v-model="state.password" @blur="v$.password.$touch" />
      <span v-if="v$.password.$error">Password is required and must be at least 10 characters long</span>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import useVuelidate from "@vuelidate/core";
import { required, minLength, maxLength, minValue } from "@vuelidate/validators";
import { useUserStore } from "@/stores/user";

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
    console.log("Form is valid", state.value);
    const payload = {
      username: state.value.username,
      password: state.value.password,
    };
    console.log(payload);
    userStore.loginUser(payload);
  } else {
    // 유효성 검사를 통과하지 못한 경우 처리 로직
    console.log("Form is invalid");
  }
}
</script>
