import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import swal from 'sweetalert';

export const useArticleStore = defineStore("article", () => {
  // 유저 토큰 확보용
  const userStore = useUserStore();
  const API_URL = "http://127.0.0.1:8000";
  const articlesList = ref([]);
  const articleDetail = ref({});
  const router = useRouter();
  // 게시글 리스트 GET
  const getArticleList = function () {
    axios({
      method: "get",
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((res) => {
        console.log(res);
        articlesList.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // 게시글 디테일 GET
  const getArticleDetail = function (articleId) {
    axios({
      method: "get",
      url: `${API_URL}/articles/${articleId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((res) => {
        console.log(res.data.user);
        articleDetail.value = res.data.user;
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // 게시글 생성 POST
  const createArticle = function (databox) {
    const { title, content } = databox;
    axios({
      method: "post",
      url: `${API_URL}/articles/`,
      data: {
        title,
        content,
      },
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((res) => {
        swal({
          title: `게시글이 생성되었습니다.`,
          icon: "success",
          button: "확인!",
        });
        router.push({ name: "ArticleDetailView", params: { id: res.data.id } });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // 게시글 수정 PUT
  const updateArticle = function (databox) {
    const { title, content, articleId } = databox;
    axios({
      method: "put",
      url: `${API_URL}/articles/${articleId}/`,
      data: {
        title,
        content,
      },
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((res) => {
        console.log(res);
        window.alert("게시글이 수정되었습니다.");
        router.push({ name: "ArticleDetailView", params: { id: res.data.id } });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // 게시글 삭제 DELETE
  const deleteArticle = function (articleId) {
    axios({
      method: "delete",
      url: `${API_URL}/articles/${articleId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((res) => {
        console.log(res);
        window.alert("삭제가 완료되었습니다.");
        router.push({ name: "CommunityView" });
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // 게시글 수정 PUT
  const putArticle = function (databox, articleId) {
    const { title, content } = databox;
    axios({
      method: "delete",
      url: `${API_URL}/articles/${articleId}/`,
      data: {
        title,
        content,
      },
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    }).then((res) => {
      console.log(res);
      window.alert("수정이 완료되었습니다.");
      router.push({ name: "ArticleDetailView", params: { id: articleId } });
    });
  };
  return { articlesList, articleDetail, getArticleList, getArticleDetail, createArticle, updateArticle, deleteArticle, putArticle };
});
