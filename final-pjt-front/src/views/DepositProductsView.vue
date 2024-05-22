<template>
  <v-container>
    <v-container class="d-flex justify-end">
      <v-col class="my-0 py-0" cols="5">
        <v-select
          class="ibm-plex-sans-kr-regular"
          v-model="bank"
          :items="bankList"
          label="은행"
          variant="outlined"
        ></v-select>
      </v-col>
    </v-container>
    <v-data-table-virtual
      height="600"
      :items="depositData"
      class="elevation-2"
      item-class="hoverable-row"
      fixed-header
    >
      <!-- userPeriod에 따라 다른 기간을 선택하여 표시 -->
      <template
        v-if="userPeriod && userPeriod === 6"
        v-slot:item.6개월="{ value }"
      >
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template
        v-else-if="userPeriod && userPeriod === 12"
        v-slot:item.12개월="{ value }"
      >
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template
        v-else-if="userPeriod && userPeriod === 24"
        v-slot:item.24개월="{ value }"
      >
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template
        v-else-if="userPeriod && userPeriod === 36"
        v-slot:item.36개월="{ value }"
      >
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{
          item.상품명
        }}</v-btn>
      </template>
    </v-data-table-virtual>

    <v-dialog v-model="dialog" width="1000">
      <v-card class="mx-auto" width="1000">
        <!-- 디테일 페이지 헤더 -->
        <template v-slot:title>
          <v-row class="mb-0">
            <v-img
              :src="bankIcon"
              class="mt-10 ms-3"
              style="height: 40px; width: 30px"
            ></v-img>
            <v-col class="pb-0 mt-6" cols="10">
              <span class="font-weight-black text-h5">
                {{ depositStore.getDepositDetail.fin_prdt_nm }}
              </span>
              <v-card-subtitle>{{
                depositStore.getDepositDetail.kor_co_nm
              }}</v-card-subtitle>
            </v-col>
            <!-- 꿀바르기 버튼 시작-->
            <v-col>
              <v-card-actions class="mt-3">
                <v-img
                  v-if="
                    depositStore.getDepositDetail.interest_user &&
                    !depositStore.getDepositDetail.interest_user.includes(
                      userStore.userInfo.id
                    )
                  "
                  @click="
                    saveEvent(
                      depositStore.getDepositDetail.fin_prdt_cd,
                      depositStore.getDepositDetail.fin_prdt_nm
                    )
                  "
                  :src="cancel"
                  class="button-image hover-effect"
                  style="width: 40px"
                />
                <v-img
                  v-else
                  @click="
                    deleteEvent(
                      depositStore.getDepositDetail.fin_prdt_cd,
                      depositStore.getDepositDetail.fin_prdt_nm
                    )
                  "
                  :src="save"
                  class="button-image hover-effect"
                  style="width: 40px"
                />
              </v-card-actions>
            </v-col>
            <!-- 꿀 바르기 버튼 끝 -->
          </v-row>
        </template>
        <!-- 디테일 페이지 내용 -->
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >관심도 ★</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.interest_user?.length
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >공시 제출일</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.dcls_month
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />

        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >금융 상품명</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.fin_prdt_nm
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />

        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >가입 방법</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.join_way
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >만기 후 이자율</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.mtrt_int
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >우대 조건</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.spcl_cnd
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >가입 대상</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.join_member
            }}</v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >가입 제한</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">
              {{
                depositStore.getDepositDetail.join_deny == 1
                  ? "제한없음"
                  : depositStore.getDepositDetail.join_deny == 2
                  ? "서민전용"
                  : depositStore.getDepositDetail.join_deny == 3
                  ? "일부제한"
                  : "기타"
              }}
            </v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >최고 한도</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">
              {{
                depositStore.getDepositDetail.max_limit === null
                  ? "한도 없음"
                  : `${new Intl.NumberFormat("ko-KR", {
                      style: "currency",
                      currency: "KRW",
                    }).format(depositStore.getDepositDetail.max_limit)}`
              }}
            </v-card-text>
          </v-col>
        </v-row>
        <hr />
        <v-row justify="center" align="center">
          <v-col cols="3" class="d-flex justify-center">
            <v-card-text class="text-style" align="center"
              >기타 유의사항</v-card-text
            >
          </v-col>
          <v-col>
            <v-card-text class="">{{
              depositStore.getDepositDetail.etc_note
            }}</v-card-text>
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
import { useSavingStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import cancel from "@/assets/cancel.png";
import save from "@/assets/save.png";
import bankIcon from "@/assets/bank-icon.png";

const userStore = useUserStore();
const savingStore = useSavingStore();

const depositStore = useDepositStore();
const depositData = ref([]);
const dialog = ref(false);

onMounted(() => {
  bank.value = "모든은행";
  depositStore.getAllDeposit();
});

const loaddata = function () {
  let i = 1;
  if (depositStore.allDeposit && depositStore.allDeposit.length > 0) {
    depositData.value = depositStore.allDeposit.map((element) => {
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

const saveEvent = function (productCode, productName) {
  console.log(productCode);
  console.log(`꿀바르기!`);
  if (productName.includes("예금")) {
    // 예금 쪽 확인
    depositStore.getHoney(productCode);
  } else if (productName.includes("적금")) {
    // 적금 쪽 확인
    savingStore.getHoney(productCode);
  }
};
const deleteEvent = function (productCode, productName) {
  console.log(productCode);
  console.log(`꿀버리기...`);
  if (productName.includes("예금")) {
    // 예금 쪽 확인
    depositStore.getHoney(productCode);
  } else if (productName.includes("적금")) {
    // 적금 쪽 확인
    savingStore.getHoney(productCode);
  }
};

// getColor 함수 정의
const getColor = (value) => {
  if (value >= 3) {
    return "green";
  } else if (value >= 2) {
    return "orange";
  } else {
    return "white";
  }
};
const userPeriod = userStore.userProfile.desirePeriod;
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

.button-image {
  transition: transform 0.3s ease-in-out;
}

.hover-effect:hover {
  transform: translateY(-10px);
}
</style>
