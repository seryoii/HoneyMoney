<template>
  <v-container class="map-size">
    <v-row>
      <!-- 도/시 선택 -->
      <v-col cols="4">
        <v-select class="custom-select" v-model="province" :items="provinces" label="도/시" @change="updateCities"></v-select>
      </v-col>
      <!-- 시/군/구 선택 -->
      <v-col cols="4">
        <v-select class="custom-select" v-model="city" :items="cities" label="시/군/구"></v-select>
      </v-col>
      <!-- 은행 선택 -->
      <v-col cols="4">
        <v-select class="custom-select" v-model="bank" :items="banks" label="은행"></v-select>
      </v-col>
      <!-- 지도 출력 Component 연결, 선택된 데이터 전달 -->
    </v-row>
    <MapSearchComponent :province="province" :city="city" :bank="bank" class="py-0 map-component" />
  </v-container>
</template>

<script setup>
import { ref, watch, computed } from "vue";
import MapSearchComponent from "@/components/MapSearchComponent.vue";
import { useMapStore } from "@/stores/map";

const store = useMapStore();

const infos = store.infos;
const banks = store.banks;
const cities = ref([]);

// 도/시 목록
const provinces = computed(() => infos.map((info) => info.prov));

// 도/시
const province = ref("선택해주세요");
// 시/군/구
const city = ref("선택해주세요");
// 은행
const bank = ref("선택해주세요");

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

<style scoped>
.custom-select {
  background-color: #fef5e771; /* 원하는 배경 색상 */
  /* 테스트 색상 */
  color: #643a09;
  font-weight: bold;
  box-shadow: 2px 2px 1px rgba(0, 0, 0, 0.1); /* 그림자 */
  border-radius: 8px;
}
.map-size {
  width: 80%;
}
</style>
