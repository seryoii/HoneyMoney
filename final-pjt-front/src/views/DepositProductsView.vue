<template>
  <!-- 최초 로딩
    <v-btn @click="saveDepositData">최초 1회 클릭?</v-btn>
    <p v-if="depositStore.depositProductsData">{{ depositStore.depositProductsData }}</p> -->
    <v-container>
      <v-select v-model="bank" :items="bankList" label="은행"></v-select>
        <v-container>
          <v-data-table :items="depositData"></v-data-table>
        </v-container>
    </v-container>

</template>

<script setup>
import { useDepositStore } from "@/stores/deposit";
import { onMounted, watch, ref, watchEffect } from "vue";
const depositStore = useDepositStore();

const depositData = ref([]);

onMounted(() => {
  depositStore.getAllDeposit();
});

const loaddata = function () {
  depositData.value = depositStore.allDeposit.map((element) => {
    const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
    const intrRate6 = option6 ? option6.intr_rate : null;
    const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
    const intrRate12 = option12 ? option12.intr_rate : null;
    const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
    const intrRate24 = option24 ? option24.intr_rate : null;
    const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
    const intrRate36 = option36 ? option36.intr_rate : null;
    return {
      공시제출일: element.dcls_month,
      은행: element.kor_co_nm,
      상품명: element.fin_prdt_nm,
      '6개월': intrRate6,
      '12개월': intrRate12,
      '24개월': intrRate24,
      '36개월': intrRate36,
    }});
};

watch(
  () => depositStore.allDeposit,
  () => {
    loaddata();
  },
  { immediate: true } // immediate를 사용하여 초기값을 바로 적용
);

const bankList = ref(['전체보기'])
const bank = ref('')

watchEffect(() => {
  depositStore.bankList.forEach((item) => {
    bankList.value.push(item)
  })
})
watch(bank, () => {
  loaddata()
  if (bank.value !== '전체보기') {
  depositData.value = depositData.value.filter((item) => {
    return item.은행 === bank.value
  })
  } else {depositData.value = depositData.value}
})


</script>
