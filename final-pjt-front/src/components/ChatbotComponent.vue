<template>
  <div>
    <v-list style="width: 400px; height: 600px">
      <v-list-item v-for="(message, index) in messages" :key="index">
        <v-list-item-content
          class="ibm-plex-sans-kr-regular"
          :class="{
            'user-message': message.role === 'user',
            'assistant-message': message.role === 'assistant',
            'system-message': message.role === 'system',
          }"
        >
          <div>
            {{ message.content }}
          </div>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <div class="message-input">
      <v-progress-linear
        v-if="loading"
        color="grey-lighten-1"
        indeterminate
      ></v-progress-linear>
      <div class="d-flex">
        <v-text-field
          class="ms-5 me-3 mt-5"
          v-model="inputMessage"
          label="메시지를 입력하세요"
          @keydown.enter="getChatbot"
          rows="1"
          outlined
        ></v-text-field>

        <v-btn
          icon="mdi-arrow-up"
          class="custom-btn mt-6"
          @click="getChatbot()"
        ></v-btn>
        <v-btn
          icon="mdi-cached"
          class="custom-btn mt-6 mr-4 ms-3"
          @click="resetChat()"
        ></v-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";

const AI_API_KEY = import.meta.env.VITE_AI_API_KEY;
const loading = ref(false);
// 컴포넌트 상태로 messages 정의
const messages = ref([
  {
    role: "system",
    content: "챗봇에게 물어보세요!",
  },
  { role: "assistant", content: "어서오세요!" },
]);
const inputMessage = ref("");
const chatbotResponse = ref("");

// 챗봇 API 호출 함수
const getChatbot = () => {
  if (inputMessage.value.trim() === "") {
    return;
  }
  // 메시지 받는 동안 loading 실행
  loading.value = true;
  // 사용자 메시지를 messages 배열에 추가
  messages.value.push({ role: "user", content: inputMessage.value });
  inputMessage.value = "";

  axios({
    method: "post",
    url: "https://api.openai.com/v1/chat/completions",
    headers: {
      Authorization: `Bearer ${AI_API_KEY}`,
      "Content-Type": "application/json",
    },
    data: {
      model: "gpt-4",
      messages: messages.value,
    },
  })
    .then((response) => {
      const botMessage = response.data.choices[0].message.content;
      // 챗봇 응답을 messages 배열에 추가
      messages.value.push({ role: "assistant", content: botMessage });
      // 응답을 화면에 표시하기 위해 상태 업데이트
      chatbotResponse.value = botMessage;
      // 로딩 끝
      loading.value = false;
    })
    .catch((error) => {
      console.log(error);
      chatbotResponse.value = "Error: Unable to fetch response.";
    });
};

const resetChat = () => {
  messages.value = [
    {
      role: "system",
      content: "챗봇에게 물어보세요!",
    },
    { role: "assistant", content: "어서오세요!" },
  ];
};
</script>

<style scoped>
.assistant-message {
  text-align: left;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 20px;
  display: inline-block;
  padding: 10px 15px;
  margin: 5px;
  max-width: 800px;
}

.user-message {
  text-align: right;
  float: right;
  background-color: #fff6ce;
  border: 1px solid #fff6ce;
  border-radius: 20px;
  padding: 10px 15px;
  margin: 5px;
  max-width: 800px;
}

.system-message {
  text-align: center;
  font-weight: 700;
  background-color: #fff6ce;
}

.chat-box {
  border: lightgrey 1px solid;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}

.custom-btn {
  box-shadow: none;
  background-color: rgb(237, 235, 235);
  height: 48px;
}

.message-input {
  background-color: white;
  color: black;
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>
