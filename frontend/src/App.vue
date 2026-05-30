<template>
  <div
    class="min-h-screen flex items-center justify-center transition-colors"
    :class="tema === 'oscuro' ? 'bg-gray-900' : 'bg-gray-100'"
  >
    <!-- CELULAR -->
    <div
      class="w-[360px] h-[640px] rounded-2xl shadow overflow-hidden relative transition-colors"
      :class="
        tema === 'oscuro' ? 'bg-gray-800 text-white' : 'bg-white text-black'
      "
    >
      <!-- HEADER -->
      <div
        class="flex items-center justify-between p-3 border-b"
        :class="tema === 'oscuro' ? 'border-gray-700' : 'border-gray-200'"
      >
        <button @click="toggleMenu" class="text-xl">☰</button>

        <span class="font-bold"> Ride Sharing </span>

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
        class="absolute top-0 left-0 h-full w-64 shadow transition-transform duration-300 z-50"
        :class="[
          tema === 'oscuro' ? 'bg-gray-800 text-white' : 'bg-white text-black',

          isOpen ? 'translate-x-0' : '-translate-x-full',
        ]"
      >
        <!-- TITLE -->
        <div class="p-4 border-b">
          <h2 class="font-bold text-lg">🚖 Menú</h2>
        </div>

        <!-- NAV -->
        <div class="p-2 text-sm">
          <button
            @click="
              cambiarTema();
              toggleMenu();
            "
            class="w-full text-left p-3 rounded hover:bg-gray-100"
            :class="menuClass"
          >
            {{ tema === "claro" ? "🌙 Modo nocturno" : "☀️ Modo claro" }}
          </button>

          <!-- HOME -->
          <button
            @click="
              $router.push('/');
              toggleMenu();
            "
            class="w-full text-left p-3 rounded hover:bg-gray-100"
            :class="menuClass"
          >
            🏠 Inicio
          </button>

          <!-- PERSONAS -->
          <div>
            <button
              @click="personasOpen = !personasOpen"
              class="w-full text-left p-3 rounded hover:bg-gray-100 flex justify-between"
              :class="menuClass"
            >
              <span>👥 Personas</span>
              <span>{{ personasOpen ? "−" : "+" }}</span>
            </button>

            <div v-if="personasOpen" class="ml-4 flex flex-col">
              <button
                @click="
                  $router.push('/pasajero');
                  toggleMenu();
                "
                class="text-left p-2 hover:bg-gray-100 rounded"
                :class="menuClass"
              >
                Pasajero
              </button>

              <button
                @click="
                  $router.push('/conductor');
                  toggleMenu();
                "
                class="text-left p-2 hover:bg-gray-100 rounded"
                :class="menuClass"
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
              :class="menuClass"
            >
              <span>🚖 Servicios</span>
              <span>{{ serviciosOpen ? "−" : "+" }}</span>
            </button>

            <div v-if="serviciosOpen" class="ml-4 flex flex-col">
              <button
                @click="
                  $router.push('/servicio-pasajero');
                  toggleMenu();
                "
                class="text-left p-2 hover:bg-gray-100 rounded"
                :class="menuClass"
              >
                Pasajero
              </button>

              <button
                @click="
                  $router.push('/servicio-conductor');
                  toggleMenu();
                "
                class="text-left p-2 hover:bg-gray-100 rounded"
                :class="menuClass"
              >
                Conductor
              </button>

              <button
                @click="
                  $router.push('/historial-viajes');
                  toggleMenu();
                "
                class="text-left p-2 hover:bg-gray-100 rounded"
                :class="menuClass"
              >
                Historial Viajes
              </button>
            </div>
          </div>

          <button
            @click="
              $router.push('/reportes/mensual');
              toggleMenu();
            "
            class="w-full text-left p-3 rounded hover:bg-gray-100"
            :class="menuClass"
          >
            📊 Reportes
          </button>

          <!-- PATRONES -->
          <!-- <div>

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

          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, computed } from "vue";

const isOpen = ref(false);

const personasOpen = ref(false);
const patronesOpen = ref(false);
const serviciosOpen = ref(false);
const tema = ref("claro");

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const cargarTema = async () => {
  const res = await fetch("http://localhost:8000/tema");

  if (!res.ok) return;

  const data = await res.json();

  tema.value = data.tema;
};

const cambiarTema = async () => {
  const nuevoTema = tema.value === "claro" ? "oscuro" : "claro";

  await fetch(
    `http://localhost:8000/tema/${nuevoTema}`,

    {
      method: "PUT",
    }
  );

  tema.value = nuevoTema;
};

const menuClass = computed(() =>
  tema.value === "oscuro" ? "hover:bg-gray-700" : "hover:bg-gray-100"
);

onMounted(() => {
  cargarTema();
});
</script>