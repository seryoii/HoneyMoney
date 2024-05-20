<template>
  <v-container>
    <v-autocomplete variant="solo" v-model="bank" :items="bankList" label="은행"></v-autocomplete>
    <v-container>
      <v-data-table :items="depositData" class="elevation-1" item-class="hoverable-row" :height="400" fixed-header>
        <!-- <template v-slot:item.은행="{ item }">
          <a class="custom-link" @click="showDetails(item[은행])">{{ item.은행 }}</a>
        </template> -->
        <template v-slot:item.상품명="{ item }">
          <v-btn class="mx-auto" @click="showDetails(item.상품명)">{{ item.상품명 }}</v-btn>
        </template>
      </v-data-table>
    </v-container>

    <v-dialog v-model="dialog" width="1000">
      <v-card class="mx-auto" prepend-icon="$vuetify" :subtitle="`${depositStore.getDepositDetail.kor_co_nm}`" width="1000">
        <template v-slot:title>
          <v-row>
            <v-col class="pb-0" cols="10">
              <span class="font-weight-black">{{ depositStore.getDepositDetail.fin_prdt_nm }}</span>
            </v-col>
            <v-col class="pb-0">
              <v-card-actions>
                <v-btn class="btn-style">save</v-btn>
              </v-card-actions>
            </v-col>
          </v-row>
        </template>

        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">관심도 ★</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.interest_user?.length }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">공시 제출일</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.dcls_month }}</v-card-text>
          </v-col>
        </v-row>
        <hr />

        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">금융 상품명</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.fin_prdt_nm }}</v-card-text>
          </v-col>
        </v-row>
        <hr />

        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">가입 방법</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.join_way }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.mtrt_int }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">우대 조건</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.spcl_cnd }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">가입 대상</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.join_member }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">가입 제한</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ join_limit }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">최고 한도</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ join_member }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center">기타 유의사항</v-card-text>
          </v-col>
          <v-col>
            <v-card-text class="">{{ depositStore.getDepositDetail.etc_note }}</v-card-text>
          </v-col>
        </v-row>
        <v-card-actions>
          <v-btn @click="dialog = false">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { useDepositStore } from "@/stores/deposit";
import { onMounted, watch, ref, watchEffect, computed } from "vue";

const depositStore = useDepositStore();
const depositData = ref([]);
const dialog = ref(false);

onMounted(() => {
  bank.value = "모든은행";
  depositStore.getAllDeposit();
});

const loaddata = function () {
  if (depositStore.allDeposit && depositStore.allDeposit.length > 0) {
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
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    });
  }
};

watch(
  () => depositStore.allDeposit,
  () => {
    loaddata();
  },
  { immediate: true }
);

const bankList = ref(["모든은행"]);
const bank = ref("");

watchEffect(() => {
  if (depositStore.bankList && depositStore.bankList.length > 0) {
    depositStore.bankList.forEach((item) => {
      bankList.value.push(item);
    });
  }
});

watch(bank, () => {
  loaddata();
  if (bank.value !== "모든은행") {
    depositData.value = depositData.value.filter((item) => {
      return item.은행 === bank.value;
    });
  }
});

const showDetails = (productName) => {
  findDetail(productName);
  // 로딩 데이터 확인 후 출력될 다이얼로그 데이터에 삽입
  dialog.value = true;
};

const findDetail = function (productName) {
  depositStore.getDepositData(productName);
};

// 한도 단위 변환
const formatCurrency = (amount) => {
  if (amount === null || amount === undefined) return "한도 없음";
  return new Intl.NumberFormat("ko-KR", { style: "currency", currency: "KRW" }).format(amount);
};

const join_member = computed(() => {
  return formatCurrency(depositStore.getDepositDetail.max_limit);
});

const join_limit = computed(() => {
  if (depositStore.getDepositDetail.join_deny === 1) {
    return `가입 제한 없음`;
  } else if (depositStore.getDepositDetail.join_deny === 2) {
    return `서민 전용`;
  } else if (depositStore.getDepositDetail.join_deny === 3) {
    return `일부 제한`;
  }
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
</style>
