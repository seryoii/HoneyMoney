<template>
  <v-container>
    <v-row>
      <v-col v-for="result in results" :key="result.id" cols="6">
        <v-card class="mx-auto pb-2 custom-bg" @click="openDialog(result)">
          <v-card-title class="ibm-plex-sans-kr-regular"
            ><h3>{{ result.fin_prdt_nm }}</h3></v-card-title
          >
          <v-card-subtitle class="ibm-plex-sans-kr-regular"
            ><h4>{{ result.kor_co_nm }}</h4></v-card-subtitle
          >
        </v-card>
        <v-dialog v-model="result.dialog" width="1000">
          <v-card class="mx-auto" width="1000">
            <template v-slot:title>
              <v-row class="mb-0 px-3">
                <v-img
                  :src="bankIcon"
                  class="mt-10 ms-3"
                  style="height: 40px; width: 30px"
                ></v-img>
                <v-col class="pb-0 mt-6" cols="10">
                  <span class="font-weight-black text-h5">{{
                    result.fin_prdt_nm
                  }}</span>
                  <v-card-subtitle>{{ result.kor_co_nm }}</v-card-subtitle>
                </v-col>
                <!-- 꿀바르기 버튼 시작-->
                <v-col>
                  <v-card-actions class="mt-3">
                    <v-img
                      v-if="
                        !result.interest_user.includes(userStore.userInfo.id)
                      "
                      @click="saveEvent(result.fin_prdt_cd, result.fin_prdt_nm)"
                      :src="cancel"
                      class="button-image hover-effect"
                      style="width: 40px"
                    />
                    <v-img
                      v-else
                      @click="
                        deleteEvent(result.fin_prdt_cd, result.fin_prdt_nm)
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
            <v-row justify="center" align="center" class="m-0">
              <v-col cols="3" class="d-flex justify-center">
                <v-card-text class="text-style" align="center"
                  >관심도 ★</v-card-text
                >
              </v-col>
              <v-col>
                <v-card-text class="">{{
                  result.interest_user?.length
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
                <v-card-text class="">{{ result.dcls_month }}</v-card-text>
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
                <v-card-text class="">{{ result.fin_prdt_nm }}</v-card-text>
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
                <v-card-text class="">{{ result.join_way }}</v-card-text>
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
                <v-card-text class="">{{ result.mtrt_int }}</v-card-text>
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
                <v-card-text class="">{{ result.spcl_cnd }}</v-card-text>
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
                <v-card-text class="">{{ result.join_member }}</v-card-text>
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
                    result.join_deny == 1
                      ? "제한없음"
                      : result.join_deny == 2
                      ? "서민전용"
                      : result.join_deny == 3
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
                <v-card-text class="">{{
                  result.max_limit === null
                    ? "한도 없음"
                    : `${new Intl.NumberFormat("ko-KR", {
                        style: "currency",
                        currency: "KRW",
                      }).format(result.max_limit)}`
                }}</v-card-text>
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
                <v-card-text class="">{{ result.etc_note }}</v-card-text>
              </v-col>
            </v-row>
            <v-card-actions>
              <v-btn @click="result.dialog = false">OK</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";
import cancel from "@/assets/cancel.png";
import save from "@/assets/save.png";
import { useUserStore } from "@/stores/user";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import swal from "sweetalert";
import { useRouter } from "vue-router";
import bankIcon from "@/assets/bank-icon.png";

const router = useRouter();
const depositStore = useDepositStore();
const savingStore = useSavingStore();
const userStore = useUserStore();
console.log(userStore.userInfo);
const results = ref([]);

const props = defineProps({
  searchKeyword: String,
});

watch(
  () => props.searchKeyword,
  (newKeyword) => {
    if (!userStore.isLogin) {
      swal({
        title: "더 많은 정보를 보실래요?",
        text: "로그인 하시면 상품도 볼 수 있어요!",
        icon: "info",
        buttons: {
          cancel: "아뇨 괜찮아요",
          catch: {
            text: "로그인 하러 가기!",
          },
        },
      }).then((willDelete) => {
        if (willDelete) {
          router.push({ name: "LoginView" });
        }
      });
    } else {
      console.log(newKeyword);
      results.value = [];
      searchDeposit(newKeyword);
      searchSaving(newKeyword);
    }
  }
);

const searchDeposit = function (keyword) {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/bank/deposit/${keyword}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      res.data.forEach((element) => {
        results.value.push({
          ...element,
          dialog: false,
          resultOption: element.resultOption || [],
        });
      });
    })
    .catch((err) => {
      console.log("예금은 없어용");
      console.log(err);
    });
};

const searchSaving = function (keyword) {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/bank/saving/${keyword}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      res.data.forEach((element) => {
        results.value.push({
          ...element,
          dialog: false,
          resultOption: element.resultOption || [],
        });
      });
    })
    .catch((err) => {
      console.log("적금은 없어용");
      console.log(err);
    });
};

const openDialog = (result) => {
  result.dialog = true;
};

const saveEvent = function (productCode, productName) {
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
  console.log(`꿀버리기...`);
  if (productName.includes("예금")) {
    // 예금 쪽 확인
    depositStore.getHoney(productCode);
  } else if (productName.includes("적금")) {
    // 적금 쪽 확인
    savingStore.getHoney(productCode);
  }
};
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
.button-image {
  transition: transform 0.3s ease-in-out;
}

.hover-effect:hover {
  transform: translateY(-10px);
}

.custom-bg {
  background-color: #f8f0de;
}
</style>
