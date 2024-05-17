<template>
  <div>
    <h1>디테일 페이지</h1>
    <div>
      {{ articleStore.articleDetail }}
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { onMounted } from "vue";
import { useRoute } from "vue-router";

const articleStore = useArticleStore();
const route = useRoute();
onMounted(() => {
  articleStore.getArticleDetail(route.params.id);
});
</script>

<style scoped></style>
