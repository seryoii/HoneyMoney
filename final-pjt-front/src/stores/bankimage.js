import { defineStore } from "pinia";
import { ref } from "vue";
import { useSavingStore } from "./saving";
import { useDepositStore } from "./deposit";
import Kyungnam from "@/assets/bank/Kyungnam.jpg";
import Gwangju from "@/assets/bank/Gwangju.jpg";
import Kookmin from "@/assets/bank/Kookmin.jpg";
import Nonghyup from "@/assets/bank/Nonghyup.jpg";
import Daegu from "@/assets/bank/Daegu.jpg";
import Busan from "@/assets/bank/Busan.jpg";
import Suhyup from "@/assets/bank/Suhyup.jpg";
import StandardChartered from "@/assets/bank/StandardChartered.jpg";
import Shinhan from "@/assets/bank/Shinhan.jpg";
import Woori from "@/assets/bank/Woori.jpg";
import Jeonbuk from "@/assets/bank/Jeonbuk.jpg";
import Jeju from "@/assets/bank/Jeju.jpg";
import IBK from "@/assets/bank/IBK.jpg";
import Kakao from "@/assets/bank/Kakao.jpg";
import Kbank from "@/assets/bank/Kbank.jpg";
import Toss from "@/assets/bank/Toss.jpg";
import Hana from "@/assets/bank/Hana.jpg";
import KDB from "@/assets/bank/KDB.jpg";

export const useBankImageStore = defineStore("bankimage", () => {
  const savingStore = useSavingStore();
  const depositStore = useDepositStore();
  
  return {};
});
