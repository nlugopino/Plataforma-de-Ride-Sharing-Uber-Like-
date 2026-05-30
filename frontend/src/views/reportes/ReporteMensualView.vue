<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Reporte mensual de ingresos</h2>

    <div class="flex flex-col gap-3">
      <div>
        <label class="block text-sm mb-1"> Mes </label>

        <select v-model="mes" class="w-full border p-3 rounded">
          <option v-for="m in 12" :key="m" :value="m">
            {{ m }}
          </option>
        </select>
      </div>

      <div>
        <label class="block text-sm mb-1"> Año </label>

        <input v-model="anio" type="number" class="w-full border p-3 rounded" />
      </div>

      <button
        @click="generar"
        class="w-full bg-blue-500 text-white p-3 rounded font-semibold"
      >
        📄 Generar PDF
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const mes = ref(new Date().getMonth() + 1);

const anio = ref(new Date().getFullYear());

const generar = () => {
  window.open(
    `http://localhost:8000/reportes/mensual/${mes.value}/${anio.value}`,
    "_blank"
  );
};
</script>