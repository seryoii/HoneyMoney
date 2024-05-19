<template>
  <!-- 최초 로딩
    <v-btn @click="saveDepositData">최초 1회 클릭?</v-btn>
    <p v-if="depositStore.depositProductsData">{{ depositStore.depositProductsData }}</p> -->
  <v-container>
    <v-data-table :items="depositData"></v-data-table>
  </v-container>
</template>

<script setup>
import { useDepositStore } from "@/stores/deposit";
import { computed, onMounted, watch, ref } from "vue";
const depositStore = useDepositStore();

const depositData = ref([]);

// 테이블 헤더 정의
const headers = [
  { text: "Declaration Month", value: "dcls_month" },
  { text: "Bank Name", value: "kor_co_nm" },
  { text: "Product Name", value: "fin_prdt_nm" },
];

onMounted(() => {
  depositStore.getAllDeposit();
});

const loaddata = function () {
  depositData.value = depositStore.allDeposit.map((element) => ({
    공시제출일: element.dcls_month,
    은행: element.kor_co_nm,
    상품명: element.fin_prdt_nm,
  }));
};

watch(
  () => depositStore.allDeposit,
  () => {
    loaddata();
  },
  { immediate: true } // immediate를 사용하여 초기값을 바로 적용
);
</script>
