<template>
  <div>
    <h1>적금 페이지</h1>
    <!-- 최초 로딩
    <v-btn @click="saveSavingData">최초 1회 클릭?</v-btn>
    <p v-if="savingStore.savingProductsData">{{ savingStore.savingProductsData }}</p> -->
  </div>
</template>

<script setup>
import { useSavingStore } from "@/stores/saving";
const savingStore = useSavingStore();
// const saveSavingData = function () {
//   savingStore.loadSavingData();
// };
</script>

<style scoped></style>
