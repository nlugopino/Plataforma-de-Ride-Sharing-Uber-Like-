<script setup>
import { ref } from "vue";

const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};
</script>

<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    
    <div id="mobile-container" class="w-[360px] h-[640px] bg-white rounded-2xl shadow overflow-hidden relative">

      <!-- HEADER -->
      <div class="flex items-center justify-between p-3 border-b">
        <button @click="toggleMenu" class="text-xl">
          ☰
        </button>
        <span class="font-bold">App Ride Sharing</span>
        <div></div>
      </div>

      <!-- CONTENIDO -->
      <div class="p-4 overflow-auto h-[calc(100%-48px)]">
        <router-view />
      </div>

      <!-- OVERLAY -->
      <div 
        v-if="isOpen"
        @click="toggleMenu"
        class="absolute inset-0 bg-black bg-opacity-30"
      ></div>

      <!-- DRAWER -->
      <div 
        class="absolute top-0 left-0 h-full w-56 bg-white shadow transform transition-transform"
        :class="isOpen ? 'translate-x-0' : '-translate-x-full'"
      >
        <div class="p-4 font-bold border-b">
          Menú
        </div>

        <nav class="flex flex-col text-sm">
          
          <button 
            @click="$router.push('/matching'); toggleMenu()" 
            class="p-3 text-left hover:bg-gray-100"
          >
            Matching
          </button>

          <button 
            @click="$router.push('/bridge'); toggleMenu()" 
            class="p-3 text-left hover:bg-gray-100"
          >
            Bridge
          </button>

          <!-- Agrega más patrones aquí -->
          <!--
          <button @click="$router.push('/observer')">Observer</button>
          -->

        </nav>
      </div>

    </div>

  </div>
</template>