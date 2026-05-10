<template>

<div
  class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
>

  <div class="bg-white w-11/12 max-w-md rounded p-4">

    <h2 class="text-xl font-bold mb-4">
      Reportar incidente
    </h2>

    <select
      v-model="tipo"
      class="w-full border rounded p-2 mb-3"
    >
      <option value="">
        Seleccione tipo
      </option>

      <option>
        Conducción peligrosa
      </option>

      <option>
        Mala atención
      </option>

      <option>
        Inseguridad
      </option>

      <option>
        Vehículo en mal estado
      </option>

      <option>
        Cobro incorrecto
      </option>

      <option>
        Otro
      </option>

    </select>

    <textarea
      v-model="descripcion"
      placeholder="Descripción"
      class="w-full border rounded p-2 mb-4"
    />

    <div class="flex justify-end gap-2">

      <button
        @click="$emit('cerrar')"
        class="px-4 py-2 bg-gray-300 rounded"
      >
        Cancelar
      </button>

      <button
        @click="enviarReporte"
        class="px-4 py-2 bg-red-500 text-white rounded"
      >
        Enviar
      </button>

    </div>

  </div>

</div>

</template>

<script setup>
import { ref } from "vue";

import axios from "axios";

const props = defineProps({
  servicioId: Number
});

const emit = defineEmits([
  "cerrar",
  "guardado"
]);

const tipo = ref("");

const descripcion = ref("");

const enviarReporte = async () => {

  try {

    await axios.post(
      `http://localhost:8000/servicios/${props.servicioId}/reportar`,
      {
        tipo_incidente: tipo.value,
        descripcion: descripcion.value
      }
    );

    emit("guardado");

  } catch (error) {

    alert(
      error.response.data.detail
    );
  }
};
</script>