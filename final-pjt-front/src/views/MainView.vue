<script setup>
import { ref } from "vue";
import mapPhoto from "@/assets/map.jpeg";
import recommendPhoto from "@/assets/recommend.jpeg";
import savingPhoto from "@/assets/saving.jpeg";
import exchagePhoto from "@/assets/exchange.jpeg";

const tab = ref(1);
</script>

<style>
.text-center {
  text-align: center;
}
</style>

<template>
  <v-card>
    <v-tabs v-model="tab" color="#424242" align-tabs="center">
      <v-tab value="one">Product</v-tab>
      <v-tab value="two">Find Bank</v-tab>
      <v-tab value="three">Exchange</v-tab>
      <v-tab value="four">Recommend</v-tab>
    </v-tabs>

    <v-card-text>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="one">
          One
          <v-img max-width="448" :src="savingPhoto"></v-img>
        </v-tabs-window-item>

        <v-tabs-window-item value="two">
          Two
          <v-img max-width="448" :src="mapPhoto"></v-img>
        </v-tabs-window-item>

        <v-tabs-window-item value="three">
          Three
          <v-img max-width="448" :src="exchagePhoto"></v-img>
        </v-tabs-window-item>

        <v-tabs-window-item value="four">
          Four
          <v-img max-width="448" :src="recommendPhoto"></v-img>
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-text>
  </v-card>
</template>
