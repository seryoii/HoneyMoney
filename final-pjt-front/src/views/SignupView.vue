<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="username">Username</label>
      <input v-model="state.username" @blur="v$.username.$touch" />
      <span v-if="v$.username.$error">Username is required and must be at least 10 characters long</span>
    </div>
    <div>
      <label for="nickname">Nickname</label>
      <input v-model="state.nickname" @blur="v$.nickname.$touch" />
      <span v-if="v$.nickname.$error">Nickname is required and must be at least 20 characters long</span>
    </div>
    <div>
      <label for="password1">Password</label>
      <input type="password" v-model="state.password1" @blur="v$.password1.$touch" />
      <span v-if="v$.password1.$error">Password is required and must be at least 10 characters long</span>
    </div>
    <div>
      <label for="password2">Check Password</label>
      <input type="password" v-model="state.password2" @blur="v$.password2.$touch" />
      <span v-if="v$.password2.$error">Password confirmation is required and must be at least 10 characters long</span>
    </div>
    <div>
      <label for="age">Age</label>
      <input type="number" v-model="state.age" @blur="v$.age.$touch" />
      <span v-if="v$.age.$error">Age is required</span>
    </div>
    <div>
      <label for="salary">Salary</label>
      <input type="number" v-model="state.salary" @blur="v$.salary.$touch" />
      <span v-if="v$.salary.$error">Salary is required</span>
    </div>
    <div>
      <label for="wealth">Wealth</label>
      <input type="number" v-model="state.wealth" @blur="v$.wealth.$touch" />
      <span v-if="v$.wealth.$error">Wealth is required</span>
    </div>
    <div>
      <label for="tendency">Tendency</label>
      <input type="number" v-model="state.tendency" @blur="v$.tendency.$touch" />
      <span v-if="v$.tendency.$error">Tendency is required</span>
    </div>
    <div>
      <label for="desirePeriod">Desire Period</label>
      <input type="number" v-model="state.desirePeriod" @blur="v$.desirePeriod.$touch" />
      <span v-if="v$.desirePeriod.$error">Desire period is required</span>
    </div>
    <div>
      <label for="saving">Saving</label>
      <input type="number" v-model="state.saving" @blur="v$.saving.$touch" />
      <span v-if="v$.saving.$error">Saving is required</span>
    </div>
    <div>
      <label for="deposit">Deposit</label>
      <input type="number" v-model="state.deposit" @blur="v$.deposit.$touch" />
      <span v-if="v$.deposit.$error">Deposit is required</span>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import useVuelidate from "@vuelidate/core";
import { required, minLength } from "@vuelidate/validators";

// 상태 정의
const state = ref({
  username: "",
  nickname: "",
  password1: "",
  password2: "",
  age: 0,
  salary: 0,
  wealth: 0,
  tendency: 0,
  desirePeriod: 0,
  saving: 0,
  deposit: 0,
});

// 유효성 검사 규칙 정의
const rules = {
  username: { required, minLength: minLength(10) },
  nickname: { required, minLength: minLength(20) },
  password1: { required, minLength: minLength(10) },
  password2: { required, minLength: minLength(10) },
  age: { required },
  salary: { required },
  wealth: { required },
  tendency: { required },
  desirePeriod: { required },
  saving: { required },
  deposit: { required },
};

// Vuelidate 훅 사용
const v$ = useVuelidate(rules, state);

function submitForm() {
  v$.value.$validate();
  if (!v$.value.$error) {
    // 유효성 검사를 통과한 경우 처리 로직
    console.log("Form is valid", state.value);
  } else {
    // 유효성 검사를 통과하지 못한 경우 처리 로직
    console.log("Form is invalid");
  }
}
</script>
