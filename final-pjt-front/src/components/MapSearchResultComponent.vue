<template>
  <v-container>
    <v-row>
      <!-- {{ results }} -->
      <v-col v-for="result in results" :key="result" cols="6">
        <v-card class="mx-auto pb-2" @click="intoDetail">
          <v-card-title>{{ result.fin_prdt_nm }}</v-card-title>
          <v-card-subtitle>{{ result.kor_co_nm }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";

const results = ref([]);
const intoDetail = function () {};
const props = defineProps({
  searchKeyword: String,
});

watch(
  () => props.searchKeyword,
  (newKeyword, oldKeyword) => {
    console.log(newKeyword);
    searchDeposit(newKeyword);
  }
);

const searchDeposit = function (keyword) {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/bank/deposit/${keyword}`,
  })
    .then((res) => {
      console.log(res);
      results.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
