<template>
<v-container class="px-16">
  <v-row justify="center" align="center">
    <v-col cols="6" align="center" class="custom-border custom-border-right">
      <v-container class="cursor" @click="intoDeposits">
        <v-img :src="depositsPic" height="400px" width="200px"></v-img>
        <h1 class="ibm-plex-sans-kr-bold">예금</h1>
      </v-container>
    </v-col>
    <v-col cols="6" align="center" class="custom-border custom-border-left">
      <v-container class="cursor" @click="intoSavings">
        <v-img :src="savingsPic" height="400px" width="200px"></v-img>
        <h1 class="ibm-plex-sans-kr-bold">적금</h1>
      </v-container>
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
.custom-border {
  position: relative;
}

.custom-border-right::after {
  content: '';
  position: absolute;
  right: 0;
  top: 10%; /* adjust as needed */
  bottom: 10%; /* adjust as needed */
  width: 1px; /* adjust thickness as needed */
  background-color: lightgrey; /* adjust color as needed */
}

.custom-border-left::before {
  content: '';
  position: absolute;
  left: 0;
  top: 10%; /* adjust as needed */
  bottom: 10%; /* adjust as needed */
  width: 1px; /* adjust thickness as needed */
  background-color: lightgrey; /* adjust color as needed */
}
</style>
