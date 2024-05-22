<template>
  <v-container class="comment-section pt-0">
    <v-container v-if="commentList.length" class="py-0 my-1">
      <v-row>
        <v-col v-for="comment in commentList" :key="comment.id" cols="12" class="py-2 my-0">
          <v-card v-if="comment.user.username === articleUser" class="mx-auto" elevation="0">
            <template v-slot:subtitle>
              <span class="font-weight-black ibm-plex-sans-kr-regular">{{ comment.content }}</span>
            </template>
            <template v-slot:title>
              <v-row>
                <v-col cols="10">
                  <v-avatar :image="`http://localhost:8000${comment.user.profile_img}`" size="25" class="me-1"></v-avatar>
                  <span class="ibm-plex-sans-kr-regular comment-user-font">{{ comment.user.nickname }}</span>
                </v-col>
                <v-col v-if="userStore.userInfo.username === articleUser" cols="2">
                  <v-card-actions>
                    <v-btn @click="editComment(comment)" class="edit-button" color="primary">
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn @click="removeComment" :value="comment.id" class="delete-button" color="error">X</v-btn>
                  </v-card-actions>
                </v-col>
              </v-row>
            </template>
          </v-card>
          <v-card v-else class="mx-auto" elevation="0">
            <template v-slot:subtitle>
              <span class="font-weight-black ibm-plex-sans-kr-regular">{{ comment.content }}</span>
            </template>
            <template v-slot:title>
              <v-row>
                <v-col cols="10">
                  <v-avatar :image="`http://localhost:8000${comment.user.profile_img}`" size="25" class="me-1"></v-avatar>
                  <span class="ibm-plex-sans-kr-regular comment-nick-font">{{ comment.user.nickname }}</span>
                </v-col>
                <v-col v-if="userStore.userInfo.username === comment.user.username" cols="2">
                  <v-card-actions>
                    <v-btn @click="editComment(comment)" class="edit-button" color="primary">
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn @click="removeComment" :value="comment.id" class="delete-button" color="error">X</v-btn>
                  </v-card-actions>
                </v-col>
              </v-row>
            </template>
          </v-card>
          <hr />
        </v-col>
      </v-row>
    </v-container>
    <v-container v-else class="py-0 my-3">
      <v-row>
        <v-col cols="12" class="no-comments ibm-plex-sans-kr-regular">가장 먼저 댓글을 달아보세요 !</v-col>
        <hr />
      </v-row>
    </v-container>
    <v-form @submit.prevent="newComment" class="comment-form">
      <v-row>
        <v-col cols="10">
          <v-text-field class="ibm-plex-sans-kr-regular" hint="다른 사람에게 상처받는 말은 하지 않는 것이 좋아요" label="댓글을 입력하세요" v-model="comment" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="2">
          <v-btn type="submit" color="primary" class="submit-button ibm-plex-sans-kr-regular">댓글 생성하기!</v-btn>
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
import { useUserStore } from "@/stores/user";

defineProps({
  Username: String,
  articleUser: String,
});

const route = useRoute();
const comment = ref("");
const commentStore = useCommentStore();
const commentList = ref([]);
const editingCommentId = ref(null); // 수정 모드
const userStore = useUserStore();

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

  console.log(userStore.userInfo.username);
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
  max-width: 100%;
  margin: 0;
}

.comment {
  margin-bottom: 10px;
}

.no-comments {
  text-align: center;
  color: #aaa;
}

.comment-form {
  margin-top: 20px;
}

.edit-button {
  min-width: 10px; /* 최소 너비 */
  min-height: 10px; /* 최소 높이 */
  font-size: 12px; /* 글자 크기 */
}
.delete-button {
  min-width: 10px; /* 최소 너비 */
  min-height: 10px; /* 최소 높이 */
  font-size: 12px; /* 글자 크기 */
}

.comment-nick-font {
  font-size: medium;
}
.comment-user-font {
  color: rgb(233, 166, 22);
  font-size: medium;
  font-weight: bold;
}

hr {
  border: 0; /* 기본 테두리 제거 */
  height: 0.5px; /* 두께 설정 */
  background-color: #dedede; /* 배경색 (수평선의 색상) 설정 */
  width: 100%; /* 너비 설정 */
}
</style>
