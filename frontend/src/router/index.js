import { createRouter, createWebHistory } from "vue-router";

/* HOME */
import HomeView from "../views/HomeView.vue";

/* PERSONAS */
import PasajeroView from "../views/personas/PasajeroView.vue";
import ConductorView from "../views/personas/ConductorView.vue";

/* SERVICIOS */
import ServicioPasajeroView from "../views/servicios/ServicioPasajeroView.vue";
import ServicioConductorView from "../views/servicios/ServicioConductorView.vue";
import HistorialViajesView from "../views/servicios/HistorialViajesView.vue";

/* PATRONES */
import BridgeView from "../views/patrones/BridgeView.vue";
import DecoratorView from "../views/patrones/DecoratorView.vue";
import FacadeView from "../views/patrones/FacadeView.vue";
import CompositeView from "../views/patrones/CompositeView.vue";

const routes = [
  {
    path: "/",
    component: HomeView
  },

  /* PERSONAS */
  {
    path: "/pasajero",
    component: PasajeroView
  },
  {
    path: "/conductor",
    component: ConductorView
  },

  /* SERVICIOS */
  {
    path: "/servicio-pasajero",
    component: ServicioPasajeroView
  },
  {
    path: "/servicio-conductor",
    component: ServicioConductorView
  },
  {
    path: "/historial-viajes",
    component: HistorialViajesView
  },

  /* PATRONES */
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
  },
  {
    path: "/composite",
    component: CompositeView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;