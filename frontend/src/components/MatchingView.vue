<template>
  <div>
    <h2 class="text-lg font-bold mb-3">Solicitar viaje</h2>

    <select 
      v-model="serviceType" 
      class="w-full border border-gray-300 p-2 rounded mb-3"
    >
      <option value="standard">Standard</option>
      <option value="premium">Premium</option>
    </select>

    <button 
      @click="requestRide"
      class="w-full bg-blue-500 hover:bg-blue-600 text-white p-2 rounded"
    >
      Solicitar
    </button>

    <div 
      v-if="result" 
      class="mt-4 p-3 bg-gray-100 rounded text-sm"
    >
      {{ result }}
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const serviceType = ref("standard");
const result = ref(null);

const requestRide = async () => {
  try {
    const res = await fetch("http://localhost:8000/match-driver", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_id: 1,
        location: "7.1,-73.1",
        service_type: serviceType.value
      })
    });

    const data = await res.json();
    result.value = JSON.stringify(data, null, 2);
  } catch (error) {
    result.value = "Error conectando con el backend";
  }
};
</script>