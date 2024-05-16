<template>
  <div>
    <h1>내 주변 은행 찾기</h1>
    <!-- select - option을 통해 검색 -->
    <select v-model="province" @change="updateCities">
      <option value="">도/시</option>
      <option v-for="info in infos" :key="info.id">
        {{ info.prov }}
      </option>
    </select>
    <select v-model="city">
      <option value="">시/군/구</option>
      <option v-for="c in cities" :key="c">{{ c }}</option>
    </select>
    <select v-model="bank">
      <option value="">은행</option>
      <option v-for="b in banks" :key="b">{{ b }}</option>
    </select>
    <!-- 지도 출력 Component 연결, 선택된 데이터 전달 -->
    <MapSearchComponent :province="province" :city="city" :bank="bank" />
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import MapSearchComponent from "@/components/MapSearchComponent.vue";
import { useMapStore } from "@/stores/map";

const store = useMapStore();

const infos = store.infos;
const banks = store.banks;
const cities = ref([]);

// 도
const province = ref("");
// 시
const city = ref("");
// 은행
const bank = ref("");

// 조건에 맞는 데이터 호출 -> cities에 할당
const updateCities = () => {
  const selectedInfo = infos.find((info) => info.prov === province.value);
  cities.value = selectedInfo ? selectedInfo.city : [];
};

// province 선택 시 함수 실행
watch(province, () => {
  updateCities();
});
</script>

<style scoped></style>
