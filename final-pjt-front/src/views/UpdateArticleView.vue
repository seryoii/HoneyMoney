<template>
  <v-container class="py-0">
    <v-container class="text-center main-title pb-5">
      <h1>Update Post</h1>
    </v-container>
    <v-row>
      <v-col align="center">
        <v-card class="py-8" width="80%">
          <v-form @submit.prevent="updateArticle" ref="form">
            <v-text-field width="90%" v-model="updatetitle" :counter="40" :rules="nameRules" label="Title" required></v-text-field>
            <v-textarea width="90%" label="Content" v-model="updatecontent" name="input-7-1" variant="filled" auto-grow required></v-textarea>
            <v-btn color="yellow-darken-3" size="large" variant="tonal" width="90%" type="submit">SAVE</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
