<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="newArticle">
      <input type="text" v-model="newtitle" />
      <input type="text" v-model="newcontent" />
      <button type="submit">게시글 생성</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useArticleStore } from "@/stores/article.js";
import swal from "sweetalert";
const articleStore = useArticleStore();
const newtitle = ref("");
const newcontent = ref("");
const newArticle = function () {
  if (window.confirm("게시글을 생성하시겠습니까?")) {
    const databox = {
      title: newtitle.value,
      content: newcontent.value,
    };
    articleStore.createArticle(databox);
  } else {
    window.alert("취소되었습니다.");
    swal("Hello world!");
  }
};
</script>

<style scoped></style>
