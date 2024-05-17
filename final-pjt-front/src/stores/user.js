import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export const useUserStore = defineStore(
  "user",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();
    const token = ref(null);
    const userInfo = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    // 회원가입 부분
    const createUser = function (payload) {
      const { username, nickname, password1, password2, age, salary, wealth, tendency, desirePeriod } = payload;
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/registration/`,
        data: {
          username,
          nickname,
          password1,
          password2,
          age,
          salary,
          wealth,
          tendency,
          desirePeriod,
        },
      })
        .then((res) => {
          const password = password1;
          const payload = {
            username,
            password,
          };
          loginUser(payload);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 로그인
    const loginUser = function (payload) {
      const { username, password } = payload;
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          userInfo.value = res.data.user;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 로그아웃
    const logoutUser = function () {
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/logout/`,
      })
        .then((res) => {
          console.log(res);
          token.value = null;
          userInfo.value = null;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };
    return { createUser, loginUser, logoutUser, token, isLogin, userInfo };
  },
  { persist: true }
);
