import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export const useUserStore = defineStore("user", () => {
  const router = useRouter();
  const createUser = function (payload) {
    const { username, nickname, password1, password2, age, salary, wealth, tendency, desirePeriod } = payload;
    axios({
      method: "post",
      url: `http://127.0.0.1:8000/dj-rest-auth/registration/`,
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
        router.push({ name: "MainView" });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return { createUser };
});
