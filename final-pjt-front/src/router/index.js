import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import MapView from "@/views/MapView.vue";
import SignupView from "@/views/SignupView.vue";
import LoginView from "@/views/LoginView.vue";
import CommunityView from "@/views/CommunityView.vue";
import ExchangeView from "@/views/ExchangeView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import ProductsView from "@/views/ProductsView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import CreateArticleView from "@/views/CreateArticleView.vue";
import UpdateArticleView from "@/views/UpdateArticleView.vue";
import RecommendView from "@/views/RecommendView.vue";

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
  },
  {
    path: "/products",
    name: "ProductsView",
    component: ProductsView,
  },
  {
    path: "/recommend",
    name: "RecommendView",
    component: RecommendView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
