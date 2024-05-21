import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import swal from "sweetalert";
import { useUserStore } from "./user";
import { lightFormatters } from "date-fns";

export const useRecommendStore = defineStore('recommend', () => {
    const API_URL = "http://127.0.0.1:8000/products";
    const recommendFirst = ref([])
    const recommendSecond = ref([])
    const userStore = useUserStore()
    console.log(userStore.userInfo)
    const getRecommendFirst = function () {
        axios({
        method: 'get',
        url: `${API_URL}/recommend/deposit/${userStore.userInfo.username}/`,
        headers: {
            Authorization: userStore.token
        }
        })
        .then((response) => {
            recommendFirst.value = []
            response.data.forEach((item) => {
                // console.log(item)
                recommendFirst.value.push(item)
            })
        })
        .catch((error) => {
            console.log(error)
        })
        axios({
        method: 'get',
        url: `${API_URL}/recommend/deposit/${userStore.userInfo.username}/`,
        headers: {
            Authorization: userStore.token
        }
        })
        .then((response) => {
            recommendFirst.value = []
            response.data.forEach((item) => {
                // console.log(item)
                recommendFirst.value.push(item)
            })
        })
        .catch((error) => {
            console.log(error)
        })
    }
    return { getRecommendFirst, recommendFirst }
}, { persist: true }
);