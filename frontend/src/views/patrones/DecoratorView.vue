<template>
  <div class="relative">

    <!-- TOAST -->
    <div 
      v-if="toast"
      class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm"
      :class="toastType === 'success' ? 'bg-green-500' : 'bg-red-500'"
    >
      {{ toast }}
    </div>

    <h2 class="text-lg font-bold mb-3">Calcular tarifa</h2>

    <!-- Costo base -->
    <label class="text-sm">Costo base</label>
    <input 
      v-model="costoBase"
      type="number"
      class="w-full border p-2 rounded mb-3"
    />

    <!-- Extras -->
    <label class="text-sm">Extras</label>

    <div class="flex flex-col gap-2 mb-3">

      <label class="flex items-center gap-2">
        <input type="checkbox" value="peaje" v-model="extras" />
        Peaje (+3000)
      </label>

      <label class="flex items-center gap-2">
        <input type="checkbox" value="nocturno" v-model="extras" />
        Nocturno (+2000)
      </label>

      <label class="flex items-center gap-2">
        <input type="checkbox" value="seguro" v-model="extras" />
        Seguro (+1500)
      </label>

    </div>

    <!-- Botón -->
    <button 
      @click="calcular"
      class="w-full bg-blue-500 text-white p-2 rounded"
    >
      Calcular
    </button>

  </div>
</template>

<script setup>
import { ref } from "vue";

const costoBase = ref(10000);
const extras = ref([]);

const toast = ref(null);
const toastType = ref("success");

const showToast = (msg, type = "success") => {
  toast.value = msg;
  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const calcular = async () => {
  try {
    const res = await fetch("http://localhost:8000/tarifa/calcular", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        costo_base: Number(costoBase.value),
        extras: extras.value
      })
    });

    const data = await res.json();

    showToast(`Total: $${data.total}`, "success");

  } catch (error) {
    showToast("Error al calcular tarifa", "error");
  }
};
</script>