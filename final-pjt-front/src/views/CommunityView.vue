<template>
  <RouterLink :to="{ name: 'CreateArticleView' }">게시글 생성하기</RouterLink>
  <v-card class="mx-auto" max-width="300">
    <v-list>
      <v-list-item v-for="(item, index) in paginatedItems" :key="index">
        <v-list-item-content>
          <RouterLink :to="{ name: 'ArticleDetailView', params: { id: item.id } }">
            {{ item.id }}번 게시글 | {{ item.user.nickname }} |
            {{ item.title }}
          </RouterLink>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-pagination v-model="currentPage" :length="totalPages" @input="updatePagination"></v-pagination>
  </v-card>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useArticleStore } from "@/stores/article";
import { RouterLink } from "vue-router";
const articleStore = useArticleStore();

onMounted(() => {
  articleStore.getArticleList();
});

watch(
  () => articleStore.articlesList,
  (newArticlesList) => {
    items.value = newArticlesList;
  }
);
const itemsPerPage = 5;
const items = ref([]);

const reversedItems = computed(() => {
  return [...items.value].reverse();
});
const currentPage = ref(1);

const totalPages = computed(() => {
  return Math.ceil(reversedItems.value.length / itemsPerPage);
});

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return reversedItems.value.slice(start, end);
});

const updatePagination = (page) => {
  currentPage.value = page;
};
</script>

<style></style>
