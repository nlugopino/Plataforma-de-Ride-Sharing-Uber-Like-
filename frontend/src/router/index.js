import { createRouter, createWebHistory } from "vue-router";

import MatchingView from "../components/MatchingView.vue";
import BridgeView from "../components/BridgeView.vue";
import DecoratorView from "../components/DecoratorView.vue";
import FacadeView from "../components/FacadeView.vue";

const routes = [
  {
    path: "/",
    redirect: "/matching"
  },
  {
    path: "/matching",
    component: MatchingView
  },
  {
    path: "/bridge",
    component: BridgeView
  },
  {
    path: "/decorator",
    component: DecoratorView
  },
  {
    path: "/facade",
    component: FacadeView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;