<template>
  <div>
    <div
      v-if="toast"
      class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm transition-all duration-300"
      :class="[toastType === 'success' ? 'bg-green-500' : 'bg-red-500']"
    >
      {{ toast }}
    </div>
    <h2 class="text-lg font-bold mb-3">Enviar Notificación</h2>

    <!-- Tipo -->
    <label class="text-sm">Tipo de notificación</label>
    <select v-model="tipo" class="w-full border p-2 rounded mb-3">
      <option value="viaje">Viaje</option>
      <option value="emergencia">Emergencia</option>
    </select>

    <!-- Canal -->
    <label class="text-sm">Canal</label>
    <select v-model="canal" class="w-full border p-2 rounded mb-3">
      <option value="email">Email</option>
      <option value="sms">SMS</option>
    </select>

    <!-- Botón -->
    <button
      @click="enviarNotificacion"
      class="w-full bg-blue-500 text-white p-2 rounded"
    >
      Enviar
    </button>

    <!-- Resultado -->
    <div v-if="resultado" class="mt-4 p-3 bg-gray-100 rounded text-sm">
      {{ resultado }}
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const toast = ref(null);
const toastType = ref("success");

const showToast = (message, type = "success") => {
  toast.value = message;
  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const tipo = ref("viaje");
const canal = ref("email");
const resultado = ref(null);

const enviarNotificacion = async () => {
  try {
    const res = await fetch("http://localhost:8000/notificacion/enviar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        tipo: tipo.value,
        canal: canal.value,
      }),
    });

    const data = await res.json();

    if (data.error) {
      showToast(data.error, "error");
    } else {
      showToast(data.mensaje, "success");
    }
  } catch (error) {
    showToast("Error conectando con el backend", "error");
  }
};
</script>