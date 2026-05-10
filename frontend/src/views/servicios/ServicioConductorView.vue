<template>

<div>

  <div v-if="servicioActivo">

    <h2 class="font-bold text-lg mb-4">
      Servicio actual
    </h2>

    <div class="border rounded p-3">

      <p>
        {{ servicioActivo.direccion_origen }}
      </p>

      <p>
        {{ servicioActivo.direccion_destino }}
      </p>

      <p>
        {{ servicioActivo.tipo_servicio }}
      </p>

      <p>
        $ {{ servicioActivo.valor_oferta }}
      </p>

      <div class="mt-3 bg-gray-100 p-2 rounded">

        <div class="flex justify-between">
          <span>Distancia</span>
          <strong>{{ servicioActivo.distancia_km }} km</strong>
        </div>

      </div>

      <button
        @click="finalizar"
        class="bg-green-500 text-white px-4 py-2 rounded mt-4"
      >
        Finalizar
      </button>

      <MapaViaje class="mt-4" />

    </div>

  </div>

  <div v-else>

    <h2 class="font-bold text-lg mb-4">
      Servicios disponibles
    </h2>

    <div
      v-for="servicio in servicios"
      :key="servicio.id"
      class="border rounded p-3 mb-3"
    >

      <p>
        {{ servicio.direccion_origen }}
      </p>

      <p>
        {{ servicio.direccion_destino }}
      </p>

      <p>
        {{ servicio.distancia_km }} km
      </p>

      <p>
        $ {{ servicio.valor_oferta }}
      </p>

      <button
        @click="aceptar(servicio.id)"
        class="bg-blue-500 text-white px-4 py-2 rounded mt-3"
      >
        Aceptar
      </button>

    </div>

  </div>

</div>

</template>

<script setup>
import MapaViaje from "../../components/MapaViaje.vue";
import { ref, onMounted } from "vue";

const servicios = ref([]);

const servicioActivo = ref(null);

const obtenerDisponibles = async () => {

  const res = await fetch(
    "http://localhost:8000/servicios/disponibles"
  );

  servicios.value = await res.json();
};

const obtenerActivo = async () => {

  const res = await fetch(
    "http://localhost:8000/servicios/conductor"
  );

  const data = await res.json();

  if (data) {
    servicioActivo.value = data;
  }
};

const aceptar = async (id) => {

  await fetch(
    `http://localhost:8000/servicios/aceptar/${id}`,
    {
      method: "PUT"
    }
  );

  obtenerActivo();
};

const finalizar = async () => {

  await fetch(
    `http://localhost:8000/servicios/finalizar/${servicioActivo.value.id}`,
    {
      method: "PUT"
    }
  );

  servicioActivo.value = null;

  obtenerDisponibles();
};

onMounted(() => {

  obtenerActivo();

  obtenerDisponibles();
});
</script>