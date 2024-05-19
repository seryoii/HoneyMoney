<template>
  <v-container class="comment-section">
    <v-row v-if="commentList.length">
      <v-col v-for="comment in commentList" :key="comment.id" cols="12">
        <v-card class="comment">
          <v-row>
            <v-col>
              <v-card-text class="comment-content">{{ comment.content }}</v-card-text>
            </v-col>
            <v-card-actions>
              <v-btn @click="editComment(comment)" class="edit-button" color="primary">
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn @click="removeComment" :value="comment.id" class="remove-button" color="error">X</v-btn>
            </v-card-actions>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="12" class="no-comments">첫 댓글을 달아보세요!</v-col>
    </v-row>
    <v-form @submit.prevent="newComment" class="comment-form">
      <v-row justify="center" align="center">
        <v-col cols="9" class="mt-6">
          <v-text-field hint="다른 사람에게 상처받는 말은 하지 않는 것이 좋아요" label="댓글을 입력하세요" v-model="comment" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="3">
          <v-btn type="submit" color="primary" class="submit-button">댓글 생성하기!</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useCommentStore } from "@/stores/comment";
import { useRoute } from "vue-router";
import swal from "sweetalert";

const route = useRoute();
const comment = ref("");
const commentStore = useCommentStore();
const commentList = ref([]);
const editingCommentId = ref(null); // 수정 모드에 필요한 상태 변수

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

const editComment = function (comment) {
  editingCommentId.value = comment.id; // 수정 모드 활성화
  swal({
    text: "댓글을 수정하세요:",
    content: {
      element: "input",
      attributes: {
        value: comment.content,
      },
    },
    buttons: {
      cancel: {
        text: "Cancel",
        visible: true,
        closeModal: true,
      },
      confirm: {
        text: "OK",
        closeModal: false,
      },
    },
  }).then((value) => {
    if (value !== null) {
      commentStore.updateComment(route.params.id, editingCommentId.value, value);
      editingCommentId.value = null; // 수정 모드 해제
      swal("수정 완료!", "댓글이 성공적으로 수정되었습니다.", "success");
    } else {
      swal("수정 취소", "댓글 수정이 취소되었습니다.", "info");
    }
  });
};

const removeComment = function (event) {
  commentStore.deleteComment(route.params.id, event.target.value);
};
</script>

<style scoped>
.comment-section {
  max-width: 600px;
  margin: 0 auto;
}

.comment {
  margin-bottom: 10px;
}

.no-comments {
  text-align: center;
  color: #aaa;
}

.comment-form {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.comment-input {
  flex: 1;
}

.edit-button {
  margin-right: 10px;
}
</style>
