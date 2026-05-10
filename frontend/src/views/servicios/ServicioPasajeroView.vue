<template>

<div class="relative">

  <div
    v-if="toast"
    class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm z-50"
    :class="toastType === 'success' ? 'bg-green-500' : 'bg-red-500'"
  >
    {{ toast }}
  </div>

  <div v-if="servicioActivo">

    <h2 class="font-bold text-lg mb-4">
      Servicio activo
    </h2>

    <div class="border rounded p-3">

      <MapaViaje
        v-if="servicioActivo.estado === 'aceptado'"
        class="mt-4"
      />

      <p>
        Estado:
        <strong>{{ servicioActivo.estado }}</strong>
      </p>

      <p>
        Origen:
        {{ servicioActivo.direccion_origen }}
      </p>

      <p>
        Destino:
        {{ servicioActivo.direccion_destino }}
      </p>

      <div class="mt-3 bg-gray-100 p-2 rounded">

        <div class="flex justify-between">
          <span>Distancia</span>
          <strong>{{ servicioActivo.distancia_km }} km</strong>
        </div>

      </div>

      <button
        v-if="servicioActivo.estado === 'pendiente'"
        @click="cancelar"
        class="bg-red-500 text-white px-4 py-2 rounded mt-4"
      >
        Cancelar
      </button>

    </div>

  </div>

  <div v-else>

    <h2 class="font-bold text-lg mb-4">
      Solicitar servicio
    </h2>

    <div class="flex flex-col gap-3">

      <input
        v-model="form.direccion_origen"
        placeholder="Dirección origen"
        class="border p-2 rounded"
      />

      <input
        v-model="form.direccion_destino"
        placeholder="Dirección destino"
        class="border p-2 rounded"
      />

      <select
        v-model="form.tipo_servicio"
        class="border p-2 rounded"
      >
        <option value="viaje">Viaje</option>
        <option value="pedido">Pedido</option>
        <option value="mensajeria">Mensajería</option>
      </select>

      <input
        v-model="form.valor_oferta"
        type="number"
        placeholder="Valor oferta"
        class="border p-2 rounded"
      />

      <button
        @click="calcularDistancia"
        class="bg-gray-500 text-white p-2 rounded"
      >
        Calcular distancia
      </button>

      <div v-if="form.distancia_km">
        Distancia:
        {{ form.distancia_km }} km
      </div>

      <button
        @click="solicitar"
        class="bg-blue-500 text-white p-2 rounded"
      >
        Solicitar
      </button>

    </div>

  </div>

</div>

</template>

<script setup>
import MapaViaje from "../../components/MapaViaje.vue";
import { reactive, ref, onMounted } from "vue";

const toast = ref(null);
const toastType = ref("success");

const servicioActivo = ref(null);

const form = reactive({

  direccion_origen: "",

  direccion_destino: "",

  tipo_servicio: "viaje",

  distancia_km: 0,

  valor_oferta: 0
});

const showToast = (msg, type = "success") => {

  toast.value = msg;

  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const calcularDistancia = () => {

  form.distancia_km =
    Math.floor(Math.random() * 16) + 5;
};

const obtenerServicio = async () => {

  const res = await fetch(
    "http://localhost:8000/servicios/pasajero"
  );

  if (!res.ok) return;

  const data = await res.json();

  if (data) {
    servicioActivo.value = data;
  }
};

const solicitar = async () => {

  const res = await fetch(
    "http://localhost:8000/servicios",
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify(form)
    }
  );

  if (!res.ok) {

    showToast("Error", "error");

    return;
  }

  const data = await res.json();

  servicioActivo.value = data;

  showToast("Servicio solicitado");
};

const cancelar = async () => {

  const res = await fetch(
    `http://localhost:8000/servicios/cancelar/${servicioActivo.value.uuid_servicio}`,
    {
      method: "PUT"
    }
  );

  if (!res.ok) {

    showToast("Error", "error");

    return;
  }

  servicioActivo.value = null;

  form.direccion_origen = "";
  form.direccion_destino = "";

  showToast("Servicio cancelado");
};

onMounted(() => {
  obtenerServicio();
});
</script>