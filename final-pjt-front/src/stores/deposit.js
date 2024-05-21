import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "./user";

export const useDepositStore = defineStore("deposit", () => {
  const userStore = useUserStore();
  const API_URL = "http://127.0.0.1:8000/products";
  const depositProductsData = ref([]);
  const getDepositDetail = ref({});
  const loadDepositData = function () {
    axios({
      method: "get",
      url: `${API_URL}/get_deposit_products/`,
    })
      .then((res) => {
        console.log(res.data);
        depositProductsData.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const allDeposit = ref([]);
  const bankList = ref([]);
  // Deposit List
  const getAllDeposit = function () {
    axios({
      method: "get",
      url: `${API_URL}/deposit/`,
    })
      .then((res) => {
        console.log(res.data);
        allDeposit.value = res.data;
        allDeposit.value.forEach((item) => {
          if (!bankList.value.includes(item.kor_co_nm)) {
            bankList.value.push(item.kor_co_nm);
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // Deposit Data 데이터 GET
  const getDepositData = function (productName) {
    axios({
      method: "get",
      url: `${API_URL}/deposit/${productName}/`,
    })
      .then((res) => {
        console.log(res);
        getDepositDetail.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getDepositDetailOption = ref([]);
  const getDepositOptionData = function (productName) {
    axios({
      method: "get",
      url: `${API_URL}/deposit/${productName}/option/`,
    })
      .then((res) => {
        getDepositDetailOption.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const depositHoney = ref("");
  // 꿀바르기 확인
  const getHoney = function (productCode) {
    axios({
      method: "post",
      url: `${API_URL}/like/deposit/${productCode}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    }).then((res) => {
      console.log(res);
      depositHoney.value = res.data;
    });
  };
  const profileDepositData = ref([]);
  const getProfileDeposit = function (userDeposit) {
    axios({
      method: "get",
      url: `${API_URL}/deposit/`,
    })
      .then((res) => {
        allDeposit.value = res.data;
        profileDepositData.value = [];
        const interestDeposit = userDeposit.map((info) => {
          return info.id;
        });
        allDeposit.value.forEach((item) => {
          if (interestDeposit.includes(item.id)) {
            profileDepositData.value.push(item);
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return { depositProductsData, loadDepositData, allDeposit, getAllDeposit, bankList, getDepositData, getDepositDetail, getDepositOptionData, getDepositDetailOption, getHoney, getProfileDeposit, profileDepositData, depositHoney };
});
