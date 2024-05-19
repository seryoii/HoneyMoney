<template>
    <div>
        <h1>환율 정보 페이지</h1>
        <v-form>
            <v-select v-model="state" :items="states" label="기준"></v-select>
            <v-select v-model="country" :items="store.curName" label="통화 선택"></v-select>

            <v-text-field v-model="exchangeBefore" :label=exchangeDetail.cur_unit></v-text-field>
            <v-text-field v-model="exchangeAfter" label="KRW"></v-text-field>
        </v-form>
    </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchange';
const store = useExchangeStore()

const states = ['송금 받을 때', '송금 보낼 때', '매매 기준율']
const state = ref('')
const country = ref('')
const exchangeDetail = ref({})
const exchangeBefore = ref('')
const exchangeAfter = ref('')
// console.log(store.exchangeInfo)
onMounted(() => {
    store.getExchangeInfo()
})

const updateExchangeDetail = () => {
    exchangeDetail.value = store.exchangeInfo.find((item) => item.cur_nm === country.value) || {}
    calculateExchange()

}

const calculateExchange = function () {
        if (state.value == '송금 받을 때' && exchangeDetail.value.ttb) {
            exchangeDetail.value.ttb = exchangeDetail.value.ttb.replace(",", "");
            exchangeAfter.value = Number(exchangeBefore.value) * Number(exchangeDetail.value.ttb)
        } else if (state.value == '송금 보낼 때' && exchangeDetail.value.tts) {
            exchangeDetail.value.tts = exchangeDetail.value.tts.replace(",", "");
            exchangeAfter.value = Number(exchangeBefore.value) * Number(exchangeDetail.value.tts)
        } else if (state.value == '매매 기준율' && exchangeDetail.value.deal_bas_r) {
            exchangeDetail.value.deal_bas_r = exchangeDetail.value.deal_bas_r.replace(",", "");
            exchangeAfter.value = Number(exchangeBefore.value) * Number(exchangeDetail.value.deal_bas_r)
        } else {
            exchangeAfter.value = '기준을 선택해주세요.'
        }
    
}

watch([state, country], () => {
    updateExchangeDetail()
})

watch(exchangeBefore, calculateExchange)
</script>

<style scoped>

</style>