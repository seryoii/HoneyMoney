<template>
  <v-container v-if="articleStore.articleDetail && userStore.userInfo">
    <v-btn class="returnBtn" @click="returnArticleList"><- Back</v-btn>
    <v-card class="mx-auto px-4 pt-4" width="80%">
      <template v-slot:title class="mt-2">
        <v-container class="pt-2 pb-0 px-0 ms-0 my-0 ibm-plex-sans-kr-regular">
          <h3>{{ articleStore.articleDetail.title }}</h3>
        </v-container>
      </template>
      <template v-slot:subtitle>
        <v-row justify="center ms-0">
          <v-col class="ps-0">
            <v-avatar :image="profileImg" size="20" class="mr-2"></v-avatar>
            <span class="font-weight-black ibm-plex-sans-kr-regular">{{ userNickname }}</span>
          </v-col>
          <v-col v-if="userStore.userInfo.username === articleStore.articleDetail.user.username" cols="4" class="text-right">
            <v-btn class="update-btn" @click="articleUpdate">Update</v-btn>
            <v-btn class="delete-btn" @click="articleDelete">Delete</v-btn>
          </v-col>
        </v-row>
      </template>
      <hr />
      <v-card-text class="main-content mx-4 pt-4 ibm-plex-sans-kr-regular" style="white-space: pre-line">
        {{ articleStore.articleDetail.content }}
      </v-card-text>
      <v-container class="py-1 font-style ibm-plex-sans-kr-regular text-right">
        Created Date:
        <span class="font-style ibm-plex-sans-kr-regular" v-if="articleStore.articleDetail.created_at">
          {{ formatDate(articleStore.articleDetail.created_at) }}
          {{ formatTime(articleStore.articleDetail.created_at) }}
        </span>
      </v-container>
      <v-container class="py-1 font-style ibm-plex-sans-kr-regular text-right">
        Updated Date:
        <span class="font-style ibm-plex-sans-kr-regular" v-if="articleStore.articleDetail.updated_at">
          {{ formatDate(articleStore.articleDetail.updated_at) }}
          {{ formatTime(articleStore.articleDetail.updated_at) }}
        </span>
      </v-container>
      <hr />
      <CommentsComponent v-if="articleStore.articleDetail && userStore.userInfo" :Username="userStore.userInfo.username" :articleUser="articleStore.articleDetail.user.username" />
    </v-card>
  </v-container>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { ref, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import CommentsComponent from "@/components/CommentsComponent.vue";
import { format, parseISO } from "date-fns";
import { useUserStore } from "@/stores/user";

const articleStore = useArticleStore();
const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
onMounted(() => {
  console.log(userStore.userInfo);
  userStore.getProfile();
});
const profileImg = computed(() => {
  return `http://localhost:8000${articleStore.articleDetail.user.profile_img}`;
});

const articleUpdate = () => {
  router.push({
    name: "UpdateArticleView",
    params: { id: articleStore.articleDetail.id },
  });
};

const returnArticleList = () => {
  router.push({
    name: "CommunityView",
  });
};

const articleDelete = () => {
  swal({
    title: "정말 삭제하실건가요?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      articleStore.deleteArticle(articleStore.articleDetail.id);
      swal("성공적으로 삭제 되었습니다!", {
        icon: "success",
      });
    } else {
      swal("취소되었습니다!");
    }
  });
};

onMounted(() => {
  articleStore.getArticleDetail(route.params.id);
});

const userNickname = computed(() => articleStore.articleDetail.user?.nickname || "");

const formatDate = (dateString) => {
  return format(parseISO(dateString), "yyyy-MM-dd");
};

const formatTime = (dateString) => {
  return format(parseISO(dateString), "HH:mm:ss");
};
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
  margin: 10px auto; /* 상하 여백 및 가운데 정렬 */
}
.font-style {
  font-size: small;
  color: gray;
}
.main-content {
  font-size: medium;
}
</style>
