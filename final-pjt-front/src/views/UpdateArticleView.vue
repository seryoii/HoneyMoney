<template>
  <div>
    <h1>게시글 수정 페이지</h1>
    <form @submit.prevent="updateArticle">
      <input type="text" v-model="updatetitle" />
      <input type="text" v-model="updatecontent" />
      <button type="submit">게시글 수정</button>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { useArticleStore } from "@/stores/article.js";
import { useRoute } from "vue-router";

const articleStore = useArticleStore();
const updatetitle = ref("");
const updatecontent = ref("");
const route = useRoute();

watch(
  () => articleStore.articleDetail,
  (pastData) => {
    updatetitle.value = pastData.title;
    updatecontent.value = pastData.content;
  }
);

// 입장 시 데이터 불러오기
onMounted(() => {
  articleStore.getArticleDetail(route.params.id);
});

// 제출 시 데이터 수정

const updateArticle = function () {
  const databox = {
    title: updatetitle.value,
    content: updatecontent.value,
    articleId: route.params.id,
  };
  articleStore.updateArticle(databox);
};
</script>

<style scoped></style>
