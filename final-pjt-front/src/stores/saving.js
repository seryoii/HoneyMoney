import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "./user";

export const useSavingStore = defineStore("saving", () => {
  const userStore = useUserStore();
  const API_URL = "http://127.0.0.1:8000/products";
  const savingProductsData = ref([]);
  const getSavingDetail = ref({});
  const getSavingDetailOption = ref([]);
  const loadSavingData = function () {
    axios({
      method: "get",
      url: `${API_URL}/get_saving_products/`,
    })
      .then((res) => {
        console.log(res.data);
        savingProductsData.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const allSaving = ref([]);
  const bankList = ref([]);

  const getAllSaving = function () {
    axios({
      method: "get",
      url: `${API_URL}/saving/`,
    })
      .then((res) => {
        console.log(res.data);
        allSaving.value = res.data;
        allSaving.value.forEach((item) => {
          if (!bankList.value.includes(item.kor_co_nm)) {
            bankList.value.push(item.kor_co_nm);
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // Saving Data 데이터 GET
  const getSavingData = function (productName) {
    axios({
      method: "get",
      url: `${API_URL}/saving/${productName}/`,
    })
      .then((res) => {
        console.log(res.data);
        getSavingDetail.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getSavingOptionData = function (productName) {
    axios({
      method: "get",
      url: `${API_URL}/saving/${productName}/option/`,
    })
      .then((res) => {
        getSavingDetailOption.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getHoney = function (productCode) {
    axios({
      method: "post",
      url: `${API_URL}/like/saving/${productCode}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    }).then((res) => {
      console.log(res);
    });
  };
  const profileSavingData = ref([]);
  const getProfileSaving = function (userSaving) {
    axios({
      method: "get",
      url: `${API_URL}/saving/`,
    })
      .then((res) => {
        allSaving.value = res.data;
        profileSavingData.value = [];
        const interestSaving = userSaving.map((info) => {
          return info.id;
        });
        allSaving.value.forEach((item) => {
          if (interestSaving.includes(item.id)) {
            profileSavingData.value.push(item);
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return { savingProductsData, loadSavingData, allSaving, getAllSaving, bankList, getSavingData, getSavingDetail, getSavingOptionData, getSavingDetailOption, getHoney, getProfileSaving, profileSavingData };
});
