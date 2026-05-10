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

    <h2 class="text-lg font-bold mb-3">Paquete de servicios</h2>

    <!-- Nombre paquete -->
    <input 
      v-model="nombre"
      placeholder="Nombre del paquete"
      class="w-full border p-2 rounded mb-3"
    />

    <!-- Servicios -->
    <div class="mb-3">
      <label class="text-sm">Servicios</label>

      <div class="flex gap-2 mt-2">
        <input v-model="nuevoNombre" placeholder="Nombre" class="border p-2 rounded w-1/2"/>
        <input v-model="nuevoCosto" type="number" placeholder="Costo" class="border p-2 rounded w-1/2"/>
      </div>

      <button 
        @click="agregarServicio"
        class="mt-2 bg-gray-200 p-2 rounded w-full"
      >
        Agregar servicio
      </button>
    </div>

    <!-- Lista -->
    <ul class="mb-3 text-sm">
      <li v-for="(s, i) in servicios" :key="i">
        {{ s.nombre }} - ${{ s.costo }}
      </li>
    </ul>

    <!-- Botón -->
    <button 
      @click="calcular"
      class="w-full bg-blue-500 text-white p-2 rounded"
    >
      Calcular total
    </button>

  </div>
</template>

<script setup>
import { ref } from "vue";

const nombre = ref("Paquete completo");

const servicios = ref([]);

const nuevoNombre = ref("");
const nuevoCosto = ref("");

const toast = ref(null);
const toastType = ref("success");

const showToast = (msg, type = "success") => {
  toast.value = msg;
  toastType.value = type;
  setTimeout(() => toast.value = null, 2500);
};

const agregarServicio = () => {
  if (!nuevoNombre.value || !nuevoCosto.value) return;

  servicios.value.push({
    nombre: nuevoNombre.value,
    costo: Number(nuevoCosto.value)
  });

  nuevoNombre.value = "";
  nuevoCosto.value = "";
};

const calcular = async () => {
  try {
    const res = await fetch("http://localhost:8000/paquete/calcular", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        nombre: nombre.value,
        servicios: servicios.value
      })
    });

    const data = await res.json();

    showToast(`Total: $${data.total}`, "success");

  } catch (error) {
    showToast("Error al calcular paquete", "error");
  }
};
</script>