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
import eventBus from "@/eventBus"; // 이벤트 버스 임포트

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
  },
  {
    path: "/article",
    name: "CreateArticleView",
    component: CreateArticleView,
  },
  {
    path: "/article/:id",
    name: "ArticleDetailView",
    component: ArticleDetailView,
  },
  {
    path: "/updateArticle/:id",
    name: "UpdateArticleView",
    component: UpdateArticleView,
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
    beforeEnter: (to, from, next) => {
      next().then(window.location.reload());
    },
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
  },
  {
    path: "/preView",
    name: "ProductsPreView",
    component: ProductsPreView,
  },
  {
    path: "/savings",
    name: "SavingProductsView",
    component: SavingProductsView,
  },
  {
    path: "/deposits",
    name: "DepositProductsView",
    component: DepositProductsView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
