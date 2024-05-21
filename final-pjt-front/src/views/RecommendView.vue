<template>
    <div>
<h1>추천페이지</h1>
<v-data-table-virtual height="600" :items="depositData" class="elevation-2" item-class="hoverable-row" fixed-header>
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{ item.상품명 }}</v-btn>
      </template>
    </v-data-table-virtual>
    </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend';
import { onMounted, ref } from 'vue'
const store = useRecommendStore()
const depositData = ref([])

onMounted(() => {
    store.getRecommendFirst()
})
// console.log('갸', store.recommendFirst)

const loaddata = function () {
  let i = 1
    depositData.value = store.recommendFirst.map((element) => {
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        NO: i++,
        공시제출일: element.dcls_month,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    });
  }
const savingData = ref([])

onMounted(() => {
    loaddata()
});
</script>

<style scoped>

</style>