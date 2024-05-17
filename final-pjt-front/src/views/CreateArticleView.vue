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
const articleStore = useArticleStore();
const newtitle = ref("");
const newcontent = ref("");
const newArticle = function () {
  const databox = {
    title: newtitle.value,
    content: newcontent.value,
  };
  articleStore.createArticle(databox);
};
</script>

<style scoped></style>
