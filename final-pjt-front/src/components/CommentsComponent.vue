<template>
  <div>
    <h1>여기는 댓글 Component</h1>
    <div v-if="commentList.length">
      <p v-for="comment in commentList" :key="comment.id">
        {{ comment.id }}
        {{ comment.content }}
        <button @click="removeComment" :value="comment.id">X</button>
      </p>
    </div>
    <div v-else>
      <p>첫 댓글을 달아보세요!</p>
    </div>
    <form @submit.prevent="newComment">
      <input type="text" v-model="comment" />
      <button type="submit">댓글 생성하기!</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useCommentStore } from "@/stores/comment";
import { useRoute } from "vue-router";

const route = useRoute();
const comment = ref("");
const commentStore = useCommentStore();
const commentList = ref([]);
const checkCommentList = function () {
  commentStore.getCommentList(route.params.id);
};
watch(
  () => commentStore.comments,
  (newComments) => {
    commentList.value = newComments;
  }
);
onMounted(() => {
  checkCommentList();
});
const newComment = function () {
  const databox = {
    articleId: route.params.id,
    content: comment.value,
  };
  commentStore.createComment(databox);
  comment.value = ""; // 댓글 입력 필드 초기화
};

const removeComment = function (event) {
  commentStore.deleteComment(route.params.id, event.target.value);
};
</script>

<style scoped></style>
