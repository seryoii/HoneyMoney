<template>
  <div>
    <h1>디테일 페이지</h1>
    <div>
      {{ articleStore.articleDetail }}
      <button @click="articleUpdate">수정하기</button>
      <button @click="articleDelete">삭제하기</button>
    </div>
    <div>
      <CommentsComponent v-if="articleStore.articleDetail" />
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { ref, onMounted, computed } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";
import CommentsComponent from "@/components/CommentsComponent.vue";

const articleStore = useArticleStore();
const route = useRoute();
const router = useRouter();

const articleUpdate = function () {
  router.push({
    name: "UpdateArticleView",
    params: { id: articleStore.articleDetail.id },
  });
};

const articleDelete = function () {
  articleStore.deleteArticle(articleStore.articleDetail.id);
};

onMounted(() => {
  articleStore.getArticleDetail(route.params.id);
});
</script>

<style scoped></style>
