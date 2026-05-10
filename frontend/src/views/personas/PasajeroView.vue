<template>
  <div class="relative">

    <!-- TOAST -->
    <div 
      v-if="toast"
      class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm z-50"
      :class="toastType === 'success' ? 'bg-green-500' : 'bg-red-500'"
    >
      {{ toast }}
    </div>

    <h2 class="text-lg font-bold mb-4">
      Perfil pasajero
    </h2>

    <div class="flex flex-col gap-3">

      <input
        v-model="form.documento"
        placeholder="Documento"
        class="border p-2 rounded"
      />

      <input
        v-model="form.nombre"
        placeholder="Nombre"
        class="border p-2 rounded"
      />

      <input
        v-model="form.correo"
        placeholder="Correo"
        class="border p-2 rounded"
      />

      <input
        v-model="form.telefono"
        placeholder="Teléfono"
        class="border p-2 rounded"
      />

      <button
        @click="guardar"
        class="bg-blue-500 text-white p-2 rounded"
      >
        Guardar
      </button>

    </div>

  </div>
</template>

<script setup>
import { reactive, onMounted, ref } from "vue";

const form = reactive({
  documento: "",
  nombre: "",
  correo: "",
  telefono: ""
});

const toast = ref(null);
const toastType = ref("success");

const showToast = (msg, type = "success") => {

  toast.value = msg;
  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const obtener = async () => {

  try {

    const res = await fetch("http://localhost:8000/pasajeros");

    if (!res.ok) return;

    const data = await res.json();

    Object.assign(form, data);

  } catch (error) {

    showToast("Error consultando pasajero", "error");
  }
};

const guardar = async () => {

  try {

    const res = await fetch("http://localhost:8000/pasajeros", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    if (!res.ok) {
      showToast("Error guardando pasajero", "error");
      return;
    }

    showToast("Pasajero guardado correctamente");

  } catch (error) {

    showToast("Error de conexión", "error");
  }
};

onMounted(() => {
  obtener();
});
</script>