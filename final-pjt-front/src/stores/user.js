import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import swal from "sweetalert";
import { lightFormatters } from "date-fns";

export const useUserStore = defineStore(
  "user",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();
    const token = ref(null);
    const userDesirePeriod = ref(null);
    const userInfo = ref(null);
    const userProfile = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    // 회원가입 부분
    const createUser = function (payload) {
      const {
        username,
        nickname,
        password1,
        password2,
        age,
        salary,
        wealth,
        tendency,
        desirePeriod,
      } = payload;
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
          console.log(res);
          const password = password1;
          const payload = {
            username,
            password,
          };
          loginUser(payload);
        })
        .catch((err) => {
          swal("Oops", "아이디가 중복되었어요!", "error");
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
          userDesirePeriod.value = res.data.user.desirePeriod;
          router.push({ name: "MainView" });
          swal(
            `${res.data.user.nickname}님 HoneyMoney에 오신 것을 환영합니다!`,
            {
              buttons: false,
              timer: 1000,
            }
          ).then((res) => {
            getProfile();
          });
        })
        .catch((err) => {
          swal("Oops", "아이디 혹은 비밀번호가 다릅니다", "error");
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
          userDesirePeriod.value = null;
          userInfo.value = null;
          userProfile.value = null;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };
    // UserProfile 부분
    const getProfile = function () {
      console.log(userInfo.value.username);
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${userInfo.value.username}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      }).then((res) => {
        console.log(res.data);
        userProfile.value = res.data;
      });
    };
    return {
      createUser,
      loginUser,
      logoutUser,
      getProfile,
      token,
      isLogin,
      userInfo,
      userProfile,
      userDesirePeriod,
    };
  },
  { persist: true }
);
