<template>
    <div>
        <h1>환율 정보 페이지</h1>
        <v-form>
            <v-select v-model="city" :items="cities" label="시/군/구"></v-select>

        <v-text-field></v-text-field>
        <v-text-field></v-text-field>
        </v-form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchange';
const store = useExchangeStore()
onMounted(() => {
    store.exchangeInfo()
})
console.log(store.curName)
</script>

<style scoped>

</style>