import { defineStore } from "pinia";
import { ref } from "vue";
import axios from 'axios'

export const useExchangeStore = defineStore("exchange", () => {
  const curName = ref([])
  const ttb = ref([])
  const tts = ref([])
  const exchangeInfo = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/exchange/'
    })
    .then((response) => {
      response.data.forEach(item => {
        curName.value.push(item.cur_nm);
      });
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return { exchangeInfo, curName, ttb, tts };
});
