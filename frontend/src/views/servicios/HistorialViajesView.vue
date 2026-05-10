<template>

<div class="max-w-md mx-auto p-4">

  <h1 class="text-2xl font-bold mb-4">
    Historial de Viajes
  </h1>

  <!-- TOAST -->
  <div
    v-if="toast"
    class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm z-50"
    :class="toastType === 'success'
      ? 'bg-green-500'
      : 'bg-red-500'"
  >
    {{ toast }}
  </div>

  <div
    v-if="viajes.length === 0"
    class="bg-white p-4 rounded shadow"
  >
    No hay viajes finalizados
  </div>

  <div
    v-for="viaje in viajes"
    :key="viaje.id"
    class="bg-white p-4 rounded shadow mb-4"
  >

    <p>
      <strong>Origen:</strong>
      {{ viaje.direccion_origen }}
    </p>

    <p>
      <strong>Destino:</strong>
      {{ viaje.direccion_destino }}
    </p>

    <p>
      <strong>Distancia:</strong>
      {{ viaje.distancia_km }} km
    </p>

    <p>
      <strong>Valor:</strong>
      $ {{ viaje.valor_oferta }}
    </p>

    <div class="flex gap-1 mt-3">

      <button
        v-for="estrella in 5"
        :key="estrella"
        @click="calificar(viaje.id, estrella)"
        :disabled="viaje.calificacion"
        class="text-2xl"
      >

        <span
          :class="
            estrella <= (viaje.calificacion || 0)
            ? 'text-yellow-400'
            : 'text-gray-300'
          "
        >
          ★
        </span>

      </button>

    </div>

    <p
      v-if="viaje.calificacion"
      class="text-green-600 mt-2 text-sm"
    >
      Viaje calificado
    </p>

  </div>

</div>

</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const viajes = ref([]);

const toast = ref("");
const toastType = ref("success");

const mostrarToast = (mensaje, tipo = "success") => {

  toast.value = mensaje;
  toastType.value = tipo;

  setTimeout(() => {
    toast.value = "";
  }, 3000);
};

const cargarHistorial = async () => {

  try {

    const response = await axios.get(
      "http://localhost:8000/servicios/historial/1"
    );

    viajes.value = response.data;

  } catch (error) {

    mostrarToast(
      "Error cargando historial",
      "error"
    );
  }
};

const calificar = async (servicioId, estrellas) => {

  try {

    await axios.post(
      `http://localhost:8000/servicios/${servicioId}/calificar`,
      {
        calificacion: estrellas,
        comentario: ""
      }
    );

    mostrarToast("Viaje calificado");

    cargarHistorial();

  } catch (error) {

    mostrarToast(
      error.response.data.detail,
      "error"
    );
  }
};

onMounted(() => {
  cargarHistorial();
});
</script>