<template>
  <v-container class="mt-10">
    <v-row justify="center">
      <v-col cols="6" align="center">
        <v-img class="cursor" @click="intoDeposits" :src="depositsPic" width="50%"></v-img>
        <p>Deposits</p>
      </v-col>
      <v-col cols="6" align="center">
        <v-img class="cursor" @click="intoSavings" :src="savingsPic" width="50%"></v-img>
        <p>Savings</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import savingsPic from "@/assets/savings.png";
import depositsPic from "@/assets/deposits.png";

import { useRouter } from "vue-router";
const router = useRouter();

// 예금
const intoDeposits = function () {
  router.push({ name: "DepositProductsView" });
};
// 적금
const intoSavings = function () {
  router.push({ name: "SavingProductsView" });
};
</script>

<style scoped>
.cursor {
  cursor: pointer;
}
</style>
