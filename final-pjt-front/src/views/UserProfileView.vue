<template>
  <div v-if="isLoading" class="loading-screen">
    <v-container fill-height align="center" justify="center">
      <v-progress-circular :model-value="value" :rotate="360" :size="100" :width="15" color="amber">
        <template v-slot:default>{{ value }} %</template>
      </v-progress-circular>
    </v-container>
  </div>
  <v-container v-else v-if="userProfile">
    <v-card class="mx-auto py-5">
      <v-row>
        <v-col cols="6">
          <v-container class="mt-3" align="center">
            <v-avatar :image="profileImg" size="200" alt="User Profile Image" cover></v-avatar>
            <v-card-title class="mt-3 ibm-plex-sans-kr-bold">
              <h2>{{ userProfile.nickname }} 님</h2>
            </v-card-title>
            <v-card-text class="ibm-plex-sans-kr-bold">
              <h3>{{ userProfile.username }} (만 {{ userProfile.age }}세)</h3>
            </v-card-text>
          </v-container>
          <v-col class="text-center">
            <v-container>
              <v-card-title class="ibm-plex-sans-kr-bold"><h4>나의 금융 정보</h4></v-card-title>
              <div class="px-4 mb-2">
                <v-chip class="chip-style mx-1 my-1">
                  나의 연봉 :
                  {{
                    new Intl.NumberFormat("ko-KR", {
                      style: "currency",
                      currency: "KRW",
                    }).format(userProfile.salary)
                  }}
                </v-chip>
                <v-chip class="chip-style mx-1 my-1">
                  나의 자산 :
                  {{
                    new Intl.NumberFormat("ko-KR", {
                      style: "currency",
                      currency: "KRW",
                    }).format(userProfile.wealth)
                  }}
                </v-chip>
                <v-chip class="chip-style mx-1 my-1">나의 저축 성향 : {{ userProfile.tendency }}</v-chip>
                <v-chip class="chip-style mx-1 my-1">나의 저축 희망 기간 : {{ userProfile.desirePeriod }}개월</v-chip>
              </div>
            </v-container>
          </v-col>
          <v-card-actions>
            <v-container class="pa-4 text-center">
              <v-dialog v-model="dialog" max-width="600" @click:outside="preventClose" persistent>
                <template v-slot:activator="{ props: activatorProps }">
                  <v-btn v-bind="activatorProps" color="yellow-darken-3" prepend-icon="mdi-account" variant="tonal" text="Edit Profile" block border></v-btn>
                </template>
                <v-card prepend-icon="mdi-account" title="User Profile" :style="{ maxHeight: '1000px', overflowY: 'auto' }">
                  <v-card-text>
                    <v-form @submit.prevent="submitForm">
                      <v-row dense>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Nickname*" v-model="form.nickname" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Age*" type="number" v-model="form.age" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Salary*" type="number" v-model="form.salary" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Wealth*" type="number" v-model="form.wealth" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Password*" type="password" v-model="form.password1" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4" sm="6">
                          <v-text-field label="Confirm Password*" type="password" v-model="form.password2" required></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6">
                          <v-select :items="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" label="Tendency*" v-model="form.tendency" required></v-select>
                        </v-col>
                        <v-col cols="12" sm="6">
                          <v-select :items="[6, 12, 24, 36]" label="Desire Period*" v-model="form.desirePeriod" required></v-select>
                        </v-col>
                        <v-col cols="12">
                          <v-file-input prepend-icon="mdi-camera" label="Profile Image" accept="image/" v-model="form.profile_img"></v-file-input>
                        </v-col>
                      </v-row>
                      <small class="text-caption text-medium-emphasis">*indicates required field</small>
                    </v-form>
                  </v-card-text>
                  <v-divider></v-divider>
                  <v-card-actions>
                    <v-row justify="space-between" align="center" class="w-100">
                      <v-col cols="auto">
                        <v-btn color="red" text="Accounts Delete" variant="plain" @click="deleteAccount"></v-btn>
                      </v-col>
                      <v-col cols="auto">
                        <v-btn color="primary" text="Save" variant="tonal" @click="submitForm"></v-btn>
                      </v-col>
                    </v-row>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-container>
          </v-card-actions>
        </v-col>
        <v-col class="px-0 mx-0" cols="6">
          <v-row class="px-0 mx-0">
            <v-col class="d-flex align-center justify-center px-0 mx-0 mb-0">
              <v-container v-if="depositStore.profileDepositData.length" class="py-0 mb-0">
                <v-row justify="end">
                  <v-col class="ms-4" cols="2">
                    <v-badge color="yellow" :content="depositStore.profileDepositData.length"></v-badge>
                    <v-img :src="jar" max-width="50"></v-img>
                  </v-col>
                  <v-row class="py-0 my-0" align="end">
                    <v-col class="mx-0 py-0 my-2 px-0" cols="7">
                      <h2 class="font-weight-black ibm-plex-sans-kr-regular">꿀바른 예금</h2>
                    </v-col>
                  </v-row>
                </v-row>
                <v-carousel height="300" show-arrows="hover" hide-delimiters>
                  <v-carousel-item v-for="(honeyDeposit, index) in depositStore.profileDepositData" :key="`carousel1-${index}`" class="no-padding">
                    <v-card class="mx-16 fill-height d-flex align-center justify-center" elevation="0">
                      <v-card class="card-design mb-2 density-compact" prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg" variant="text">
                        <template v-slot:subtitle>
                          <span class="ibm-plex-sans-kr-regular">{{ honeyDeposit.kor_co_nm }}</span>
                        </template>
                        <template v-slot:title>
                          <span class="font-weight-black ibm-plex-sans-kr-regular">
                            <h4>{{ honeyDeposit.fin_prdt_nm }}</h4>
                          </span>
                        </template>
                        <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular">가입 방법 : {{ honeyDeposit.join_way }}</v-card-text>
                        <v-card-text class="ibm-plex-sans-kr-regular">만기 후 이자율 : {{ honeyDeposit.mtrt_int }}</v-card-text>
                        <v-container align="center">
                          <v-btn color="yellow-darken-3" variant="tonal" @click="viewDetailDeposit">Details</v-btn>
                          <v-dialog v-model="viewDetailDepositDialog" width="1000">
                            <v-card class="mx-auto" width="1000">
                              <template v-slot:subtitle>
                                <v-row>
                                  <v-col cols="4"></v-col>
                                  <v-col align="center" cols="4">
                                    <div class="custom-subtitle ibm-plex-sans-kr-regular">
                                      {{ honeyDeposit.kor_co_nm }}
                                    </div>
                                  </v-col>
                                  <v-col align="center" cols="4" class="mt-2 ibm-plex-sans-kr-regular">꿀바르기</v-col>
                                </v-row>
                              </template>
                              <template v-slot:title>
                                <v-row align="center" justify="space-between">
                                  <v-col align="center"></v-col>
                                  <v-col align="center" class="pb-0">
                                    <span class="font-weight-black ibm-plex-sans-kr-regular">
                                      <h2>{{ honeyDeposit.fin_prdt_nm }}</h2>
                                    </span>
                                  </v-col>
                                  <v-col align="center" class="pb-0 mt-2">
                                    <v-img
                                      v-if="honeyDeposit.interest_user && !honeyDeposit.interest_user.includes(userStore.userInfo.id)"
                                      @click="saveEvent(honeyDeposit.fin_prdt_cd, honeyDeposit.fin_prdt_nm)"
                                      :src="cancel"
                                      class="button-image hover-effect"
                                      max-width="60"
                                    />
                                    <v-img v-else @click="deleteEvent(honeyDeposit.fin_prdt_cd, honeyDeposit.fin_prdt_nm)" :src="save" class="button-image hover-effect" max-width="60" />
                                  </v-col>
                                </v-row>
                              </template>

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">관심도 ★</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.interest_user?.length }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">공시 제출일</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.dcls_month }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">금융 상품명</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.fin_prdt_nm }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 방법</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.join_way }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.mtrt_int }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">우대 조건</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.spcl_cnd }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 대상</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.join_member }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 제한</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">
                                    {{ honeyDeposit.join_deny == 1 ? "제한없음" : honeyDeposit.join_deny == 2 ? "서민전용" : honeyDeposit.join_deny == 3 ? "일부제한" : "기타" }}
                                  </v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">최고 한도</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">
                                    {{
                                      honeyDeposit.max_limit === null
                                        ? "한도 없음"
                                        : `${new Intl.NumberFormat("ko-KR", {
                                            style: "currency",
                                            currency: "KRW",
                                          }).format(honeyDeposit.max_limit)}`
                                    }}
                                  </v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">기타 유의사항</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeyDeposit.etc_note }}</v-card-text>
                                </v-col>
                              </v-row>
                              <v-card-actions>
                                <v-btn @click="viewDetailDepositDialog = false">OK</v-btn>
                              </v-card-actions>
                            </v-card>
                          </v-dialog>
                        </v-container>
                      </v-card>
                    </v-card>
                  </v-carousel-item>
                </v-carousel>
              </v-container>
              <v-container v-else>
                <v-container class="my-14 py-14 font-weight-black ibm-plex-sans-kr-regular" align="center" justify="center">
                  <p>예금 꿀통이 비어있어요...</p>
                  <v-btn @click="goDeposit" color="yellow-darken-2 mt-4" size="large" variant="tonal">
                    <p class="ibm-plex-sans-kr-regular">예금 꿀 바르러 가기!</p>
                  </v-btn>
                </v-container>
              </v-container>
            </v-col>
          </v-row>
          <v-row class="py-0 my-0">
            <v-col class="d-flex align-center justify-center py-0 my-0">
              <v-container class="py-0 mb-0" v-if="savingStore.profileSavingData.length">
                <v-row justify="end">
                  <v-col class="ms-4" cols="2">
                    <v-badge color="yellow" :content="savingStore.profileSavingData.length"></v-badge>
                    <v-img :src="jar" max-width="50"></v-img>
                  </v-col>
                  <v-row class="py-0 my-0" align="end">
                    <v-col class="mx-0 py-0 my-2 px-0" cols="7">
                      <h2 class="font-weight-black ibm-plex-sans-kr-regular">꿀바른 적금</h2>
                    </v-col>
                  </v-row>
                </v-row>
                <v-carousel height="300" show-arrows="hover" hide-delimiters>
                  <v-carousel-item v-for="(honeySaving, index) in savingStore.profileSavingData" :key="`carousel2-${index}`" class="no-padding">
                    <v-card class="mx-16 fill-height d-flex align-center justify-center" elevation="0">
                      <v-card class="card-design mb-2 density-compact" prepend-avatar="https://randomuser.me/api/portraits/women/10.jpg" variant="text">
                        <template v-slot:subtitle>
                          <span class="ibm-plex-sans-kr-regular">{{ honeySaving.kor_co_nm }}</span>
                        </template>
                        <template v-slot:title>
                          <span class="font-weight-black ibm-plex-sans-kr-regular">
                            <h4>{{ honeySaving.fin_prdt_nm }}</h4>
                          </span>
                        </template>
                        <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular">가입 방법 : {{ honeySaving.join_way }}</v-card-text>
                        <v-card-text class="ibm-plex-sans-kr-regular">만기 후 이자율 : {{ honeySaving.mtrt_int }}</v-card-text>
                        <v-container align="center">
                          <v-btn color="yellow-darken-3" variant="tonal" @click="viewDetailSaving">Details</v-btn>
                          <v-dialog v-model="viewDetailSavingDialog" width="1000">
                            <v-card class="mx-auto" width="1000">
                              <template v-slot:subtitle>
                                <v-row>
                                  <v-col cols="4"></v-col>
                                  <v-col align="center" cols="4">
                                    <div class="custom-subtitle ibm-plex-sans-kr-regular">
                                      {{ honeySaving.kor_co_nm }}
                                    </div>
                                  </v-col>
                                  <v-col align="center" cols="4" class="mt-2 ibm-plex-sans-kr-regular">꿀바르기</v-col>
                                </v-row>
                              </template>
                              <template v-slot:title>
                                <v-row align="center" justify="space-between">
                                  <v-col align="center"></v-col>
                                  <v-col align="center" class="pb-0">
                                    <span class="font-weight-black ibm-plex-sans-kr-regular">
                                      <h2>{{ honeySaving.fin_prdt_nm }}</h2>
                                    </span>
                                  </v-col>
                                  <v-col align="center" class="pb-0 mt-2">
                                    <v-img
                                      v-if="honeySaving.interest_user && !honeySaving.interest_user.includes(userStore.userInfo.id)"
                                      @click="saveEvent(honeySaving.fin_prdt_cd, honeySaving.fin_prdt_nm)"
                                      :src="cancel"
                                      class="button-image hover-effect"
                                      max-width="60"
                                    />
                                    <v-img v-else @click="deleteEvent(honeySaving.fin_prdt_cd, honeySaving.fin_prdt_nm)" :src="save" class="button-image hover-effect" max-width="60" />
                                  </v-col>
                                </v-row>
                              </template>

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">관심도 ★</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.interest_user?.length }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">공시 제출일</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.dcls_month }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">금융 상품명</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.fin_prdt_nm }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 방법</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.join_way }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />

                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">기간 별 이율</v-card-text>
                                </v-col>
                                <v-col>
                                  <!-- <v-card-text v-for="option in honeySavingOption">
                                    <p>적립 방법 : {{ option.rsrv_type_nm }}</p>
                                    <p>개월 수 : {{ option.save_trm }}</p>
                                    <p>이율 : {{ option.intr_rate }}</p>
                                    <p>최대 이율 : {{ option.intr_rate2 }}</p>
                                  </v-card-text> -->
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">만기 후 이자율</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.mtrt_int }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">우대 조건</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.spcl_cnd }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 대상</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.join_member }}</v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">가입 제한</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">
                                    {{ honeySaving.join_deny == 1 ? "제한없음" : honeySaving.join_deny == 2 ? "서민전용" : honeySaving.join_deny == 3 ? "일부제한" : "기타" }}
                                  </v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">최고 한도</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">
                                    {{
                                      honeySaving.max_limit === null
                                        ? "한도 없음"
                                        : `${new Intl.NumberFormat("ko-KR", {
                                            style: "currency",
                                            currency: "KRW",
                                          }).format(honeySaving.max_limit)}`
                                    }}
                                  </v-card-text>
                                </v-col>
                              </v-row>
                              <hr />
                              <v-row justify="center" align="center">
                                <v-col cols="3" class="d-flex justify-center">
                                  <v-card-text class="text-style" align="center">기타 유의사항</v-card-text>
                                </v-col>
                                <v-col>
                                  <v-card-text class="">{{ honeySaving.etc_note }}</v-card-text>
                                </v-col>
                              </v-row>
                              <v-card-actions>
                                <v-btn @click="viewDetailSavingDialog = false">OK</v-btn>
                              </v-card-actions>
                            </v-card>
                          </v-dialog>
                        </v-container>
                      </v-card>
                    </v-card>
                  </v-carousel-item>
                </v-carousel>
              </v-container>
              <v-container v-else>
                <v-container class="my-14 py-14 font-weight-black ibm-plex-sans-kr-regular" align="center" justify="center">
                  <p>적금 꿀통이 비어있어요...</p>
                  <v-btn @click="goSaving" color="yellow-darken-2 mt-4" size="large" variant="tonal">
                    <p class="ibm-plex-sans-kr-regular">적금 꿀 바르러 가기!</p>
                  </v-btn>
                </v-container>
              </v-container>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import jar from "@/assets/jar.png";
import cancel from "@/assets/cancel.png";
import save from "@/assets/save.png";
import { useRouter } from "vue-router";
import swal from "sweetalert";
const router = useRouter();

const depositStore = useDepositStore();
const savingStore = useSavingStore();
const userStore = useUserStore();

const { userProfile } = storeToRefs(userStore);

const isLoading = ref(true);
const value = ref(0);
const interval = ref(-1);

onMounted(() => {
  console.log("onMounted");
  userStore.getProfile();
  checkDeposit();
  checkSaving();
  // 프로그레스 서클 업데이트
  interval.value = setInterval(() => {
    if (value.value === 100) {
      value.value = 100;
    } else {
      value.value += 10;
    }
  }, 200);

  // 3-5초 후에 로딩을 false로 설정합니다.
  setTimeout(() => {
    isLoading.value = false;
    clearInterval(interval.value);
  }, 3000); // 여기서는 3초로 설정
});

// 꿀바른 상품 확인 함수
const checkDeposit = function () {
  depositStore.getProfileDeposit(userProfile.value.interest_deposit);
  console.log(userProfile.value.interest_deposit);
};

const checkSaving = function () {
  savingStore.getProfileSaving(userProfile.value.interest_saving);
  console.log(userProfile.value.interest_saving);
};

const dialog = ref(false);
const form = ref({
  nickname: `${userProfile.value.nickname}`,
  age: `${userProfile.value.age}`,
  salary: `${userProfile.value.salary}`,
  wealth: `${userProfile.value.wealth}`,
  password1: `${userProfile.value.password1}`,
  password2: `${userProfile.value.password2}`,
  tendency: `${userProfile.value.tendency}`,
  desirePeriod: `${userProfile.value.desirePeriod}`,
  profile_img: null, // 프로필 이미지
});

const profileImg = computed(() => {
  return `http://localhost:8000${userProfile.value.profile_img}`;
});

const submitForm = async () => {
  const formData = new FormData();
  formData.append("nickname", form.value.nickname);
  formData.append("age", form.value.age);
  formData.append("salary", form.value.salary);
  formData.append("wealth", form.value.wealth);
  formData.append("password1", form.value.password1);
  formData.append("password2", form.value.password2);
  formData.append("tendency", form.value.tendency);
  formData.append("desirePeriod", form.value.desirePeriod);
  if (form.value.profile_img) {
    formData.append("profile_img", form.value.profile_img);
  }
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${userProfile.value.username}/`,
    data: formData,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      swal("성공적으로 저장되었습니다!", "You clicked the button!", "success");
      dialog.value = false;
      userStore.getProfile(); // 업데이트된 프로필을 다시 가져옵니다.
    })
    .catch((err) => {
      console.log(err);
    });
};

const preventClose = function () {
  swal("Save 버튼을 눌러주세요!");
};

// 로고 사진도 가져오기

const viewDetailDepositDialog = ref(false);
const viewDetailDeposit = function () {
  console.log("위에꺼");
  viewDetailDepositDialog.value = true;
};
const viewDetailSavingDialog = ref(false);
const viewDetailSaving = function () {
  console.log(`아래꺼`);
  viewDetailSavingDialog.value = true;
};

const goSaving = function () {
  router.push({ name: "SavingProductsView" });
};
const goDeposit = function () {
  router.push({ name: "DepositProductsView" });
};

const deleteAccount = function () {
  swal({
    title: "정말 떠나실 건가요..?",
    text: "꿀은 숙성될 수록 비싸답니다",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("꿀통이 완전히 제거되었습니다", {
        icon: "success",
      });
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/accounts/user/delete/${userProfile.value.username}/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          console.log(`회원탈퇴 완료!`);
          userStore.logoutUser();
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      swal("꿀통을 지키셨어요!");
    }
  });
};

// 여기서 axios로 불러와서 연결해보자. 아니면 로그인 했을 때, 배열을 미리 받아두면 되지 않을까?
</script>

<style scoped>
.loading-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 24px;
}

.chip-style {
  cursor: pointer;
}
.chip-style:hover {
  background-color: rgba(255, 162, 0, 0.199);
}

.card-design {
  border-radius: 8px;
  background-color: rgba(255, 234, 0, 0.171);
}

.hoverable-row {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hoverable-row:hover {
  background-color: #f5f5f5;
}

.custom-link:hover {
  color: darkblue;
}
hr {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 40px;
  margin-right: 40px;
  box-shadow: 1px 1px 1px rgba(193, 193, 193, 0.435);
  border: 1px solid rgba(255, 255, 255, 0);
}
.text-style {
  font-weight: bolder;
  font-size: medium;
}
.button-image {
  transition: transform 0.3s ease-in-out;
}

.hover-effect:hover {
  transform: translateY(-10px);
}
</style>
