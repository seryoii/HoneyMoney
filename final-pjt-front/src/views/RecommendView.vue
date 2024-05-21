<template>
  <div>
<h1>추천페이지</h1>
  <v-tabs class="mb-3" v-model="type" variant="outlined" divided>
      <v-tab class="ibm-plex-sans-kr-regular" @click="Financial"><h3>금융 정보랑 비슷한거</h3></v-tab>
      <v-tab class="ibm-plex-sans-kr-regular" @click="Age"><h3>나이대</h3></v-tab>
  </v-tabs>
  <v-data-table-virtual v-if="state==='financial'" height="600" :items="recommendFirst" class="elevation-2" item-class="hoverable-row" fixed-header>
    <template v-slot:item.상품명="{ item }">
      <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{ item.상품명 }}</v-btn>
    </template>
  </v-data-table-virtual>
  <v-data-table-virtual v-if="state==='age'" height="600" :items="recommendSecond" class="elevation-2" item-class="hoverable-row" fixed-header>
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
const state = ref('financial')

const Financial = () => {
state.value = 'financial';
};
const Age = () => {
state.value = 'age';
};

onMounted(() => {
  store.getRecommendFirst()
  store.getRecommendSecond()
})

const recommendFirst = ref([])
const recommend1 = function () {
  recommendFirst.value = store.recommendFirst.map((element) => {
      console.log('element', element)
      if (element.fin_prdt_nm.includes('예금')) {
          const type = '예금'
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
    const intrRate6 = option6 ? option6.intr_rate : null;
    const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
    const intrRate12 = option12 ? option12.intr_rate : null;
    const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
    const intrRate24 = option24 ? option24.intr_rate : null;
    const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
    const intrRate36 = option36 ? option36.intr_rate : null;
    return {
      "상품 유형": type,
      공시제출일: element.dcls_month,
      은행: element.kor_co_nm,
      상품명: element.fin_prdt_nm,
      "6개월": intrRate6,
      "12개월": intrRate12,
      "24개월": intrRate24,
      "36개월": intrRate36,
    };
      } else if (element.fin_prdt_nm.includes('적금')) {
          const type = '적금'
      const option6 = element.savingoption_set.find((option) => option.save_trm === 6 && option.rsrv_type_nm === "자유적립식");
    const intrRate6 = option6 ? option6.intr_rate : null;
    const option12 = element.savingoption_set.find((option) => option.save_trm === 12);
    const intrRate12 = option12 ? option12.intr_rate : null;
    const option24 = element.savingoption_set.find((option) => option.save_trm === 24);
    const intrRate24 = option24 ? option24.intr_rate : null;
    const option36 = element.savingoption_set.find((option) => option.save_trm === 36);
    const intrRate36 = option36 ? option36.intr_rate : null;
    return {
        "상품 유형": type,
        공시제출일: element.dcls_month,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      }
    };
  });
}
const recommendSecond = ref([])
const recommend2 = function () {
  recommendSecond.value = store.recommendSecond.map((element) => {
      console.log('element', element)
      if (element.fin_prdt_nm.includes('예금')) {
          const type = '예금'
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
    const intrRate6 = option6 ? option6.intr_rate : null;
    const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
    const intrRate12 = option12 ? option12.intr_rate : null;
    const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
    const intrRate24 = option24 ? option24.intr_rate : null;
    const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
    const intrRate36 = option36 ? option36.intr_rate : null;
    return {
      유형: type,
      공시제출일: element.dcls_month,
      은행: element.kor_co_nm,
      상품명: element.fin_prdt_nm,
      "6개월": intrRate6,
      "12개월": intrRate12,
      "24개월": intrRate24,
      "36개월": intrRate36,
    };
      } else if (element.fin_prdt_nm.includes('적금')) {
          const type = '적금'
      const option6 = element.savingoption_set.find((option) => option.save_trm === 6 && option.rsrv_type_nm === "자유적립식");
    const intrRate6 = option6 ? option6.intr_rate : null;
    const option12 = element.savingoption_set.find((option) => option.save_trm === 12);
    const intrRate12 = option12 ? option12.intr_rate : null;
    const option24 = element.savingoption_set.find((option) => option.save_trm === 24);
    const intrRate24 = option24 ? option24.intr_rate : null;
    const option36 = element.savingoption_set.find((option) => option.save_trm === 36);
    const intrRate36 = option36 ? option36.intr_rate : null;
    return {
        유형: type,
        공시제출일: element.dcls_month,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      }
    };
  });
}
onMounted(() => {
  recommend1()
  recommend2()
});
</script>

<style scoped>
.custom-btn {
  background-color: #F5F5F5;
  box-shadow: none
}

.custom-btn:hover {
  background-color: #f0f0f0; /* 마우스를 올렸을 때 연한 회색 배경색으로 변경 */
}
</style>