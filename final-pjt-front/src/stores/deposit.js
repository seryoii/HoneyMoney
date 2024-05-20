import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";

export const useDepositStore = defineStore("deposit", () => {
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
  // db 호출
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
  return { depositProductsData, loadDepositData, allDeposit, getAllDeposit, bankList, getDepositData, getDepositDetail };
});
