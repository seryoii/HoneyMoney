<template>
  <v-container>
    <v-container class="text-center main-title pb-5">
      <h1>New Post</h1>
    </v-container>
    <v-row>
      <v-col align="center">
        <v-card class="py-8" width="80%">
          <v-form @submit.prevent="newArticle" ref="form">
            <v-text-field width="90%" v-model="newtitle" :counter="40" :rules="nameRules" label="Title" required></v-text-field>
            <v-textarea width="90%" label="Content" v-model="newcontent" name="input-7-1" variant="filled" auto-grow required></v-textarea>
            <v-btn color="yellow-darken-3" size="large" variant="tonal" width="90%" type="submit">SAVE</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useArticleStore } from "@/stores/article.js";
import swal from "sweetalert";
const articleStore = useArticleStore();
const newtitle = ref("");
const newcontent = ref("");
const newArticle = function () {
  swal({
    title: "게시글을 생성할까요?",
    text: "꿀팁을 나누면 더 달달해져요!",
    icon: "info",
    buttons: [true, "생성하기!"],
  }).then((willCreate) => {
    if (willCreate) {
      const databox = {
        title: newtitle.value,
        content: newcontent.value,
      };
      articleStore.createArticle(databox);
      swal("성공적으로 생성되었어요!", {
        icon: "success",
      });
    }
  });
};
</script>

<style scoped>
.main-title {
  color: #9b7026;
}
</style>
