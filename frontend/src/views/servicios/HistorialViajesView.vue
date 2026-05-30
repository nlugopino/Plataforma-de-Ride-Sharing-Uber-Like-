<template>
  <div class="max-w-md mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Historial de Viajes</h1>

    <!-- TOAST -->
    <div
      v-if="toast"
      class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm z-50"
      :class="toastType === 'success' ? 'bg-green-500' : 'bg-red-500'"
    >
      {{ toast }}
    </div>

    <div v-if="viajes.length === 0" class="bg-white p-4 rounded shadow">
      No hay viajes finalizados
    </div>

    <div
      v-for="viaje in viajes"
      :key="viaje.id"
      class="bg-white text-black p-4 rounded shadow mb-4"
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

      <p v-if="viaje.calificacion" class="text-green-600 mt-2 text-sm">
        Viaje calificado
      </p>

      <p class="text-sm text-yellow-600">
        ⭐ +{{ Math.floor(viaje.total_final / 1000) }} puntos
      </p>

      <div v-if="!viaje.propina" class="mt-3">
        <p class="text-sm font-semibold mb-2">💰 Propina para el conductor</p>

        <div class="flex gap-2">
          <button
            @click="agregarPropina(viaje.id, 1000)"
            class="bg-green-500 text-white px-3 py-1 rounded"
          >
            $1.000
          </button>

          <button
            @click="agregarPropina(viaje.id, 3000)"
            class="bg-green-500 text-white px-3 py-1 rounded"
          >
            $3.000
          </button>

          <button
            @click="agregarPropina(viaje.id, 5000)"
            class="bg-green-500 text-white px-3 py-1 rounded"
          >
            $5.000
          </button>
        </div>
      </div>

      <div v-else class="mt-3 text-green-600">
        💰 Propina otorgada: $ {{ viaje.propina }}
      </div>

      <button
        v-if="!viaje.tiene_objeto_perdido"
        @click="reportarObjeto(viaje)"
        class="bg-orange-500 text-white px-3 py-2 rounded mt-2"
      >
        🧳 Reportar objeto perdido
      </button>
    </div>

    <div
      v-if="mostrarModalObjeto"
      class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50"
    >
      <div class="bg-white p-4 rounded w-80 shadow-lg">
        <div class="flex justify-between items-center mb-3">
          <h3 class="font-bold">🧳 Objeto perdido</h3>

          <button
            @click="mostrarModalObjeto = false"
            class="text-gray-500 hover:text-red-500 text-xl font-bold"
          >
            ✕
          </button>
        </div>

        <select
          v-model="objetoPerdido.tipo"
          class="border p-2 w-full mb-2 rounded"
        >
          <option value="celular">Celular</option>

          <option value="llaves">Llaves</option>

          <option value="billetera">Billetera</option>
        </select>

        <textarea
          v-model="objetoPerdido.descripcion"
          class="border p-2 w-full rounded"
          rows="4"
          placeholder="Describe el objeto perdido"
        />

        <div class="flex gap-2 mt-3">
          <button
            @click="guardarObjeto"
            class="flex-1 bg-blue-500 text-white p-2 rounded"
          >
            Guardar
          </button>

          <button
            @click="mostrarModalObjeto = false"
            class="flex-1 bg-gray-400 text-white p-2 rounded"
          >
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from "vue";
import axios from "axios";

const viajes = ref([]);

const toast = ref("");
const toastType = ref("success");

const mostrarModalObjeto = ref(false);

const viajeSeleccionado = ref(null);

const objetoPerdido = reactive({
  tipo: "celular",

  descripcion: "",
});

const showToast = (msg, type = "success") => {
  toast.value = msg;

  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

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
    mostrarToast("Error cargando historial", "error");
  }
};

const calificar = async (servicioId, estrellas) => {
  try {
    await axios.post(
      `http://localhost:8000/servicios/${servicioId}/calificar`,
      {
        calificacion: estrellas,
        comentario: "",
      }
    );

    mostrarToast("Viaje calificado");

    cargarHistorial();
  } catch (error) {
    mostrarToast(error.response.data.detail, "error");
  }
};

const agregarPropina = async (servicioId, valor) => {
  const res = await fetch(
    `http://localhost:8000/servicios/${servicioId}/propina`,
    {
      method: "PUT",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        propina: valor,
      }),
    }
  );

  if (!res.ok) {
    const error = await res.json();

    showToast(error.detail, "error");

    return;
  }

  showToast("Propina registrada");

  // Esperar que se actualice el historial
  await cargarHistorial();
};

const reportarObjeto = async (viaje) => {
  viajeSeleccionado.value = viaje;

  mostrarModalObjeto.value = true;
};

const guardarObjeto = async () => {
  const res = await fetch(
    `http://localhost:8000/objetos-perdidos/${viajeSeleccionado.value.id}`,

    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(objetoPerdido),
    }
  );

  if (!res.ok) {
    const error = await res.json();

    showToast(error.detail, "error");

    return;
  }

  showToast("Objeto reportado");

  mostrarModalObjeto.value = false;

  await obtenerHistorial();
};

onMounted(() => {
  cargarHistorial();
});
</script>