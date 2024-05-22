// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import MapView from "@/views/MapView.vue";
import SignupView from "@/views/SignupView.vue";
import LoginView from "@/views/LoginView.vue";
import CommunityView from "@/views/CommunityView.vue";
import ExchangeView from "@/views/ExchangeView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import ProductsPreView from "@/views/ProductsPreView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import CreateArticleView from "@/views/CreateArticleView.vue";
import UpdateArticleView from "@/views/UpdateArticleView.vue";
import RecommendView from "@/views/RecommendView.vue";
import SavingProductsView from "@/views/SavingProductsView.vue";
import DepositProductsView from "@/views/DepositProductsView.vue";
import Swal from "sweetalert";
import { useUserStore } from "@/stores/user";

const routes = [
  {
    path: "/",
    name: "MainView",
    component: MainView,
  },
  {
    path: "/map",
    name: "MapView",
    component: MapView,
  },
  {
    path: "/signup",
    name: "SignupView",
    component: SignupView,
  },
  {
    path: "/login",
    name: "LoginView",
    component: LoginView,
  },
  {
    path: "/community",
    name: "CommunityView",
    component: CommunityView,
    meta: { requiresAuth: true },
  },
  {
    path: "/article",
    name: "CreateArticleView",
    component: CreateArticleView,
    meta: { requiresAuth: true },
  },
  {
    path: "/article/:id",
    name: "ArticleDetailView",
    component: ArticleDetailView,
    meta: { requiresAuth: true },
  },
  {
    path: "/updateArticle/:id",
    name: "UpdateArticleView",
    component: UpdateArticleView,
    meta: { requiresAuth: true },
  },
  {
    path: "/exchange",
    name: "ExchangeView",
    component: ExchangeView,
  },
  {
    path: "/profile",
    name: "UserProfileView",
    component: UserProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: "/products",
    name: "ProductsPreView",
    component: ProductsPreView,
  },
  {
    path: "/recommend",
    name: "RecommendView",
    component: RecommendView,
    meta: { requiresAuth: true },
  },
  {
    path: "/preView",
    name: "ProductsPreView",
    component: ProductsPreView,
    meta: { requiresAuth: true },
  },
  {
    path: "/savings",
    name: "SavingProductsView",
    component: SavingProductsView,
    meta: { requiresAuth: true },
  },
  {
    path: "/deposits",
    name: "DepositProductsView",
    component: DepositProductsView,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (userStore.isLogin) {
      next();
    } else {
      Swal({
        title: "로그인이 필요합니다",
        text: "이 페이지에 접근하려면 로그인이 필요합니다.",
        icon: "warning",
        confirmButtonText: "로그인 페이지로 이동",
      }).then(() => {
        next({ name: "LoginView" });
      });
    }
  } else {
    next();
  }
});

export default router;
