import { createRouter, createWebHistory } from "vue-router";

import MatchingView from "../components/MatchingView.vue";
import BridgeView from "../components/BridgeView.vue";

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;