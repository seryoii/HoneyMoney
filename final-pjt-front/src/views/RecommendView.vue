<template>
  <div>
    <v-tabs class="mb-8 mt-10 custom-bg" variant="outlined" divided>
      <v-tab
        class="ibm-plex-sans-kr-regular"
        style="width: 50%"
        @click="Financial"
        ><h3>나와 비슷한 금융 정보를 가진 사용자들이 가입한 상품</h3></v-tab
      >
      <v-tab class="ibm-plex-sans-kr-regular" style="width: 50%" @click="Age"
        ><h3>{{ age }}대가 가장 많이 가입한 상품</h3></v-tab
      >
    </v-tabs>
    <v-data-table-virtual
      v-if="state === 'financial'"
      height="600"
      :items="recommendFirst"
      class="elevation-2"
      item-class="hoverable-row"
      fixed-header
    >
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{
          item.상품명
        }}</v-btn>
      </template>
    </v-data-table-virtual>
    <v-data-table-virtual
      v-if="state === 'age'"
      height="600"
      :items="recommendSecond"
      class="elevation-2"
      item-class="hoverable-row"
      fixed-header
    >
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{
          item.상품명
        }}</v-btn>
      </template>
    </v-data-table-virtual>
  </div>
</template>

<script setup>
import { useRecommendStore } from "@/stores/recommend";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import { onMounted, ref, computed } from "vue";

const store = useRecommendStore();
const state = ref("financial");
const depositStore = useDepositStore();
const savingStore = useSavingStore();
const userStore = useUserStore();
const dialog = ref(false);
const age = ref(Math.floor(userStore.userProfile.age / 10) * 10);
const Financial = () => {
  state.value = "financial";
};
const Age = () => {
  state.value = "age";
};

onMounted(() => {
  store.getRecommendFirst();
  store.getRecommendSecond();
});

const join_member = ref(null);
const join_limit = ref(null);

const recommendFirst = ref([]);
const recommend1 = function () {
  recommendFirst.value = store.recommendFirst.map((element) => {
    console.log("element", element);
    if (element.fin_prdt_nm.includes("예금")) {
      const type = "예금";
      const option6 = element.depositoption_set.find(
        (option) => option.save_trm === 6
      );
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find(
        (option) => option.save_trm === 12
      );
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find(
        (option) => option.save_trm === 24
      );
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find(
        (option) => option.save_trm === 36
      );
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
    } else if (element.fin_prdt_nm.includes("적금")) {
      const type = "적금";
      const option6 = element.savingoption_set.find(
        (option) => option.save_trm === 6
      );
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.savingoption_set.find(
        (option) => option.save_trm === 12
      );
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.savingoption_set.find(
        (option) => option.save_trm === 24
      );
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.savingoption_set.find(
        (option) => option.save_trm === 36
      );
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
    }
  });
};
const recommendSecond = ref([]);
const recommend2 = function () {
  recommendSecond.value = store.recommendSecond.map((element) => {
    console.log("element", element);
    if (element.fin_prdt_nm.includes("예금")) {
      const type = "예금";
      const option6 = element.depositoption_set.find(
        (option) => option.save_trm === 6
      );
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find(
        (option) => option.save_trm === 12
      );
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find(
        (option) => option.save_trm === 24
      );
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find(
        (option) => option.save_trm === 36
      );
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
    } else if (element.fin_prdt_nm.includes("적금")) {
      const type = "적금";
      const option6 = element.savingoption_set.find(
        (option) => option.save_trm === 6
      );
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.savingoption_set.find(
        (option) => option.save_trm === 12
      );
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.savingoption_set.find(
        (option) => option.save_trm === 24
      );
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.savingoption_set.find(
        (option) => option.save_trm === 36
      );
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
    }
  });
};

onMounted(() => {
  recommend1();
  recommend2();
});
</script>

<style scoped>
.hoverable-row {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hoverable-row:hover {
  background-color: #f5f5f5;
}

.custom-link {
  color: black;
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
}

.custom-link:hover {
  color: darkblue;
}
hr {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 40px;
  margin-right: 40px;
  box-shadow: 1px 1px 1px rgba(193, 193, 193, 0.435);
  border: 1px solid rgba(255, 255, 255, 0);
}
.text-style {
  font-weight: bolder;
  font-size: medium;
}
.btn-style {
  font-size: large;
  background-color: rgba(255, 174, 0, 0.661);
  border-radius: 5%px;
}

.custom-btn {
  background-color: #f5f5f5;
  box-shadow: none;
}

.custom-btn:hover {
  background-color: #f0f0f0; /* 마우스를 올렸을 때 연한 회색 배경색으로 변경 */
}

.custom-bg {
  background-color: #f7ecd3;
}
</style>
