<template>
    <div>
<h1>추천페이지</h1>
    </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend';
import { onMounted } from 'vue'
const store = useRecommendStore()
onMounted(() => {
    store.getRecommendFirst()
})
console.log(store.recommendFirst)
</script>

<style scoped>

</style>