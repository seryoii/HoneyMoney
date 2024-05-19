<template>
  <v-container>
    <v-btn class="returnBtn" @click="returnArticleList"><- Back</v-btn>
    <v-card class="mx-auto" prepend-icon="$vuetify" :subtitle="`${articleStore.articleDetail.user}`" width="80%">
      <template v-slot:title>
        <v-row justify="center">
          <v-col>
            <span class="font-weight-black">{{ articleStore.articleDetail.title }}</span>
          </v-col>
          <v-col cols="4" class="text-right">
            <v-btn class="update-btn" @click="articleUpdate">Update</v-btn>
            <v-btn class="delete-btn" @click="articleDelete">Delete</v-btn>
          </v-col>
        </v-row>
      </template>
      <v-card-text class="pt-4">
        {{ articleStore.articleDetail.content }}
      </v-card-text>
      <hr />
      <CommentsComponent v-if="articleStore.articleDetail" />
    </v-card>
  </v-container>
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

const returnArticleList = function () {
  router.push({
    name: "CommunityView",
  });
};

const articleDelete = function () {
  articleStore.deleteArticle(articleStore.articleDetail.id);
};

onMounted(() => {
  articleStore.getArticleDetail(route.params.id);
});
</script>

<style scoped>
.update-btn {
  background-color: rgba(0, 0, 0, 0); /* 완전히 투명 */
  box-shadow: none;
  color: rgba(255, 196, 0, 0.986); /* 버튼 텍스트 색상 */
  font-weight: bolder;
  font-size: 12px;
  cursor: pointer;
  text-shadow: 0.5px 0.5px 0.5px rgba(255, 166, 0, 0.986);
}
.delete-btn {
  background-color: rgba(0, 0, 0, 0); /* 완전히 투명 */
  box-shadow: none;
  color: rgba(230, 54, 54, 0.688); /* 버튼 텍스트 색상 */
  font-size: 12px;
  font-weight: bolder;
  cursor: pointer;
  text-shadow: 0.5px 0.5px 0.5px rgba(230, 54, 54, 0.688);
}
.returnBtn {
  background-color: rgba(0, 0, 0, 0); /* 완전히 투명 */
  cursor: pointer;
  font-weight: bolder;
  box-shadow: none;
  color: rgba(0, 0, 0, 0.291); /* 버튼 텍스트 색상 */
}

hr {
  border: 0; /* 기본 테두리 제거 */
  height: 0.5px; /* 두께 설정 */
  background-color: #dedede; /* 배경색 (수평선의 색상) 설정 */
  width: 95%; /* 너비 설정 */
  margin: 20px auto; /* 상하 여백 및 가운데 정렬 */
}
</style>
