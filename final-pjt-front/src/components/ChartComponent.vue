<template>
  <div>
    <Bar
      class="mx-auto"
      style="width: 100%"
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@//stores/saving";
import colors from "vuetify/util/colors";
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  Colors,
} from "chart.js";

const userStore = useUserStore();

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

const props = defineProps({
  options: Object,
  // savingOptions: String,
  //   averageIntrRate: Array,
  //   intrRate: Array,
  //   intrRate2: Array,
});
console.log(props.options.rsrv_type);

const chartDataS = {
  labels: ["6개월 금리", "12개월 금리", "24개월 금리", "36개월 금리"],
  datasets: [
    {
      label: "저축 금리",
      data: props.options.intrRate,
      backgroundColor: "#1089FF",
      stack: "Stack 1",
    },
    {
      label: "최고 우대 금리",
      data: props.options.intrRate2,
      backgroundColor: colors.red.accent2,
      stack: "Stack 2",
    },
  ],
};

const chartDataF = {
  labels: ["6개월 금리", "12개월 금리", "24개월 금리", "36개월 금리"],
  datasets: [
    {
      label: "저축 금리",
      data: props.options.intrRate,
      backgroundColor: "#1089FF",
      stack: "Stack 1",
    },
    {
      label: "최고 우대 금리",
      data: props.options.intrRate2,
      backgroundColor: colors.red.accent2,
      stack: "Stack 2",
    },
  ],
};
let chartData;

if (props.options.rsrv_type === "S") {
  chartData = chartDataS;
} else if (props.options.rsrv_type === "F") {
  chartData = chartDataF;
}
const chartOptions = ref({
  plugins: {
    title: {
      display: true,
      text: `<${props.title}> 상품의 저축 금리`,
    },
  },
  responsive: true,
  scales: {
    x: {
      stacked: true,
      ticks: {
        maxRotation: 0,
        minRotation: 0,
        font: {
          size: 10,
        },
      },
    },
  },
});
</script>

<style scoped></style>
