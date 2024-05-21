import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";
import { useUserStore } from "@/stores/user";

export const useCommentStore = defineStore(
  "comment",
  () => {
    // 댓글 리스트 확인
    const userStore = useUserStore();
    const comments = ref([]);
    const API_URL = `http://127.0.0.1:8000/articles`;

    const getCommentList = function (articleId) {
      axios({
        method: "get",
        url: `${API_URL}/${articleId}/comments/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          comments.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 댓글 생성
    const createComment = function (databox) {
      const { articleId, content } = databox;
      axios({
        method: "post",
        url: `${API_URL}/${articleId}/comments/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
        data: {
          content,
        },
      })
        .then((res) => {
          console.log(`댓글 생성 완료`);
          comments.value.push(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 댓글 삭제
    const deleteComment = function (articleId, commentId) {
      axios({
        method: "delete",
        url: `${API_URL}/${articleId}/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          getCommentList(articleId);
        })
        .catch((err) => {
          console.log(err);
        });
    };
    // 댓글 수정
    const updateComment = function (articleId, commentId, content) {
      axios({
        method: "put",
        url: `${API_URL}/${articleId}/comments/${commentId}/`,
        data: {
          content,
        },
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          getCommentList(articleId);
        })
        .catch((err) => {
          console.log(err);
        });
    };
    return { comments, getCommentList, createComment, deleteComment, updateComment };
  },
  { persist: true }
);
