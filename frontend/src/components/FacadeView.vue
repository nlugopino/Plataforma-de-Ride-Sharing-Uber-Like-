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

    <h2 class="text-lg font-bold mb-3">Finalizar viaje</h2>

    <!-- ID -->
    <label class="text-sm">ID del viaje</label>
    <input 
      v-model="id"
      type="number"
      class="w-full border p-2 rounded mb-3"
    />

    <!-- Total -->
    <label class="text-sm">Total</label>
    <input 
      v-model="total"
      type="number"
      class="w-full border p-2 rounded mb-3"
    />

    <!-- Botón -->
    <button 
      @click="finalizar"
      class="w-full bg-blue-500 text-white p-2 rounded"
    >
      Finalizar viaje
    </button>

  </div>
</template>

<script setup>
import { ref } from "vue";

const id = ref(1);
const total = ref(20000);

const toast = ref(null);
const toastType = ref("success");

const showToast = (msg, type = "success") => {
  toast.value = msg;
  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const finalizar = async () => {
  try {
    const res = await fetch("http://localhost:8000/viaje/finalizar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        id: Number(id.value),
        total: Number(total.value)
      })
    });

    const data = await res.json();

    showToast(data.mensaje, "success");

  } catch (error) {
    showToast("Error al finalizar viaje", "error");
  }
};
</script>