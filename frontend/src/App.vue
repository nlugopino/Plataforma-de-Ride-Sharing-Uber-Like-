<script setup>
import { ref } from "vue";

const isOpen = ref(false);

const personasOpen = ref(false);
const patronesOpen = ref(false);
const serviciosOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};
</script>

<template>

  <div class="min-h-screen bg-gray-100 flex items-center justify-center">

    <!-- CELULAR -->
    <div
      class="w-[360px] h-[640px] bg-white rounded-2xl shadow overflow-hidden relative"
    >

      <!-- HEADER -->
      <div class="flex items-center justify-between p-3 border-b">

        <button
          @click="toggleMenu"
          class="text-xl"
        >
          ☰
        </button>

        <span class="font-bold">
          Ride Sharing
        </span>

        <div></div>

      </div>

      <!-- CONTENIDO -->
      <div class="h-[calc(100%-56px)] overflow-auto p-4">
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
        class="absolute top-0 left-0 h-full w-64 bg-white shadow transition-transform duration-300 z-50"
        :class="isOpen ? 'translate-x-0' : '-translate-x-full'"
      >

        <!-- TITLE -->
        <div class="p-4 border-b">

          <h2 class="font-bold text-lg">
            🚖 Menú
          </h2>

        </div>

        <!-- NAV -->
        <div class="p-2 text-sm">

          <!-- HOME -->
          <button
            @click="$router.push('/'); toggleMenu()"
            class="w-full text-left p-3 rounded hover:bg-gray-100"
          >
            🏠 Inicio
          </button>

          <!-- PERSONAS -->
          <div>

            <button
              @click="personasOpen = !personasOpen"
              class="w-full text-left p-3 rounded hover:bg-gray-100 flex justify-between"
            >
              <span>👥 Personas</span>
              <span>{{ personasOpen ? '−' : '+' }}</span>
            </button>

            <div
              v-if="personasOpen"
              class="ml-4 flex flex-col"
            >

              <button
                @click="$router.push('/pasajero'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Pasajero
              </button>

              <button
                @click="$router.push('/conductor'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Conductor
              </button>

            </div>

          </div>

          <!-- SERVICIOS -->
          <div>

            <button
              @click="serviciosOpen = !serviciosOpen"
              class="w-full text-left p-3 rounded hover:bg-gray-100 flex justify-between"
            >
              <span>🚖 Servicios</span>
              <span>{{ serviciosOpen ? '−' : '+' }}</span>
            </button>

            <div
              v-if="serviciosOpen"
              class="ml-4 flex flex-col"
            >

              <button
                @click="$router.push('/servicio-pasajero'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Pasajero
              </button>

              <button
                @click="$router.push('/servicio-conductor'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Conductor
              </button>

              <button
                @click="$router.push('/historial-viajes'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Historial Viajes
              </button>

            </div>

          </div>

          <!-- PATRONES -->
          <div>

            <button
              @click="patronesOpen = !patronesOpen"
              class="w-full text-left p-3 rounded hover:bg-gray-100 flex justify-between"
            >
              <span>🧠 Patrones</span>
              <span>{{ patronesOpen ? '−' : '+' }}</span>
            </button>

            <div
              v-if="patronesOpen"
              class="ml-4 flex flex-col"
            >

              <button
                @click="$router.push('/bridge'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Bridge
              </button>

              <button
                @click="$router.push('/decorator'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Decorator
              </button>

              <button
                @click="$router.push('/facade'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Facade
              </button>

              <button
                @click="$router.push('/composite'); toggleMenu()"
                class="text-left p-2 hover:bg-gray-100 rounded"
              >
                Composite
              </button>

            </div>

          </div>

        </div>

      </div>

    </div>

  </div>

</template>