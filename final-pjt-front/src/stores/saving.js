import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";

export const useSavingStore = defineStore("saving", () => {
  const API_URL = "http://127.0.0.1:8000/products";
  const savingProductsData = ref([]);
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
  return { savingProductsData, loadSavingData };
});
