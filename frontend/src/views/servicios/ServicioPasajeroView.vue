<template>
  <div class="relative">
    <div class="bg-yellow-100 border border-yellow-300 p-3 rounded mb-4">
      <div class="flex justify-between items-center">
        <div>
          <p class="font-bold">🏆 Nivel {{ nivel }}</p>

          <p class="text-sm">⭐ {{ puntos }} puntos acumulados</p>
        </div>
      </div>
    </div>

    <div
      v-if="notificacion"
      class="bg-blue-100 border border-blue-300 p-3 rounded mb-4"
    >
      <p class="text-sm">🔔 {{ notificacion }}</p>
    </div>

    <div
      v-if="toast"
      class="absolute top-3 right-3 px-4 py-2 rounded shadow text-white text-sm z-50"
      :class="toastType === 'success' ? 'bg-green-500' : 'bg-red-500'"
    >
      {{ toast }}
    </div>

    <div v-if="servicioActivo">
      <h2 class="font-bold text-lg mb-4">Servicio activo</h2>

      <div class="border rounded p-3">
        <MapaViaje v-if="servicioActivo.estado === 'aceptado'" class="mt-4" />

        <p>
          Estado:
          <strong>{{ servicioActivo.estado }}</strong>
        </p>

        <p>
          Origen:
          {{ servicioActivo.direccion_origen }}
        </p>

        <p>
          Destino:
          {{ servicioActivo.direccion_destino }}
        </p>

        <p>
          Método pago:
          <strong>
            {{ servicioActivo.metodo_pago }}
          </strong>
        </p>

        <div class="mt-3 bg-gray-100 p-2 rounded">
          <div class="flex justify-between">
            <span>Distancia</span>
            <strong>{{ servicioActivo.distancia_km }} km</strong>
          </div>
        </div>

        <div class="mt-3 bg-green-50 p-2 rounded">
          <div class="flex justify-between">
            <span>Oferta original</span>
            <strong> $ {{ servicioActivo.valor_oferta }} </strong>
          </div>

          <div class="flex justify-between">
            <span>Descuento</span>
            <strong class="text-green-600">
              - $ {{ servicioActivo.descuento_aplicado }}
            </strong>
          </div>

          <div class="flex justify-between mt-2">
            <span>Total final</span>

            <strong class="text-blue-600">
              $ {{ servicioActivo.total_final }}
            </strong>
          </div>
        </div>

        <button
          v-if="servicioActivo.estado === 'pendiente'"
          @click="cancelar"
          class="bg-red-500 text-white px-4 py-2 rounded mt-4"
        >
          Cancelar
        </button>

        <button
          v-if="
            !tieneReporte &&
            (servicioActivo.estado === 'aceptado' ||
              servicioActivo.estado === 'finalizado')
          "
          @click="mostrarModalReporte = true"
          class="bg-red-500 text-white px-4 py-2 rounded mt-4 w-full"
        >
          Reportar incidente
        </button>

        <div
          v-if="tieneReporte"
          class="mt-4 bg-green-100 text-green-700 p-2 rounded"
        >
          Reporte enviado
        </div>
      </div>

      <div
        v-if="servicioActivo.estado === 'aceptado'"
        class="grid grid-cols-1 gap-2 mt-4"
      >
        <button
          @click="ejecutarAccion('emergencia')"
          class="bg-red-500 text-white p-2 rounded"
        >
          🚨 Emergencia
        </button>

        <button
          @click="ejecutarAccion('ubicacion')"
          class="bg-blue-500 text-white p-2 rounded"
        >
          📍 Compartir
        </button>

        <button
          @click="ejecutarAccion('contacto')"
          class="bg-green-500 text-white p-2 rounded"
        >
          📞 Contactar
        </button>
      </div>
    </div>

    <div class="flex gap-2 mt-3" v-if="servicioActivo && !servicioActivo.tipo_comprobante">
      <button
        @click="generarComprobante(servicioActivo.id, 'estandar')"
        class="bg-gray-600 text-white px-3 py-1 rounded"
      >
        📄 Estándar
      </button>

      <button
        @click="generarComprobante(servicioActivo.id, 'premium')"
        class="bg-yellow-500 text-white px-3 py-1 rounded"
      >
        ⭐ Premium
      </button>

      <button
        @click="generarComprobante(servicioActivo.id, 'corporativo')"
        class="bg-blue-700 text-white px-3 py-1 rounded"
      >
        🏢 Corporativo
      </button>
    </div>

    <div v-if="servicioActivo" class="mt-3 text-sm text-green-600 font-semibold">
      Comprobante generado:
      {{ servicioActivo.tipo_comprobante }}
    </div>

    <div v-if="!servicioActivo">
      <h2 class="font-bold text-lg mb-4">Solicitar servicio</h2>

      <div class="flex flex-col gap-3">
        <input
          v-model="form.direccion_origen"
          placeholder="Dirección origen"
          class="border p-2 rounded"
        />

        <input
          v-model="form.direccion_destino"
          placeholder="Dirección destino"
          class="border p-2 rounded"
        />

        <select v-model="form.tipo_servicio" class="border p-2 rounded">
          <option value="viaje">Viaje</option>
          <option value="pedido">Pedido</option>
          <option value="mensajeria">Mensajería</option>
        </select>

        <input
          v-model="form.valor_oferta"
          type="number"
          placeholder="Valor oferta"
          class="border p-2 rounded"
        />

        <select v-model="form.metodo_pago" class="border p-2 rounded">
          <option value="efectivo">💵 Efectivo</option>

          <option value="tarjeta">💳 Tarjeta</option>

          <option value="wallet">📱 Wallet</option>
        </select>

        <div
          v-if="servicioActivo?.promociones"
          class="flex flex-wrap gap-2 mt-2"
        >
          <span
            v-for="promo in servicioActivo.promociones.split(',')"
            :key="promo"
            class="bg-green-100 text-green-700 px-2 py-1 rounded-full text-xs"
          >
            {{ promo }}
          </span>
        </div>

        <button
          @click="calcularDistancia"
          class="bg-gray-500 text-white p-2 rounded"
        >
          Calcular distancia
        </button>

        <div v-if="form.distancia_km">
          Distancia:
          {{ form.distancia_km }} km
        </div>

        <button @click="solicitar" class="bg-blue-500 text-white p-2 rounded">
          Solicitar
        </button>
      </div>
    </div>

    <ReporteIncidenteModal
      v-if="mostrarModalReporte"
      :servicio-id="servicioActivo.id"
      @cerrar="mostrarModalReporte = false"
      @guardado="
        mostrarModalReporte = false;
        tieneReporte = true;
        showToast('Reporte enviado');
      "
    />
  </div>
</template>

<script setup>
import MapaViaje from "../../components/MapaViaje.vue";
import ReporteIncidenteModal from "../../components/ReporteIncidenteModal.vue";
import { reactive, ref, onMounted } from "vue";

const toast = ref(null);
const toastType = ref("success");

const servicioActivo = ref(null);

const puntos = ref(0);

const nivel = ref("Bronce");

const notificacion = ref(null);

const mostrarModalReporte = ref(false);

const tieneReporte = ref(false);

const form = reactive({
  direccion_origen: "",
  direccion_destino: "",
  tipo_servicio: "viaje",
  distancia_km: 0,
  valor_oferta: 0,
  metodo_pago: "efectivo",
});

const showToast = (msg, type = "success") => {
  toast.value = msg;

  toastType.value = type;

  setTimeout(() => {
    toast.value = null;
  }, 2500);
};

const calcularDistancia = () => {
  form.distancia_km = Math.floor(Math.random() * 16) + 5;
};

const obtenerPuntos = async () => {
  const res = await fetch("http://localhost:8000/pasajeros/puntos");

  if (!res.ok) return;

  const data = await res.json();

  puntos.value = data.puntos;

  nivel.value = data.nivel;
};

const obtenerNotificacion = async () => {
  const res = await fetch("http://localhost:8000/notificaciones");

  if (!res.ok) return;

  const data = await res.json();

  notificacion.value = data.mensaje;
};

const obtenerServicio = async () => {
  const res = await fetch("http://localhost:8000/servicios/pasajero");

  if (!res.ok) return;

  const data = await res.json();

  if (data) {
    servicioActivo.value = data;

    await verificarReporte();
  }
};

const solicitar = async () => {
  const res = await fetch("http://localhost:8000/servicios", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(form),
  });

  if (!res.ok) {

    const error = await res.json();

    showToast(
      error.detail,
      "error"
    );

    return;
  }

  const data = await res.json();

  servicioActivo.value = data;

  tieneReporte.value = false;

  showToast("Servicio solicitado");
};

const cancelar = async () => {
  const res = await fetch(
    `http://localhost:8000/servicios/cancelar/${servicioActivo.value.uuid_servicio}`,
    {
      method: "PUT",
    }
  );

  if (!res.ok) {
    showToast("Error", "error");

    return;
  }

  servicioActivo.value = null;

  form.direccion_origen = "";
  form.direccion_destino = "";

  showToast("Servicio cancelado");
};

const ejecutarAccion = async (tipo) => {
  console.log("acaaa");

  const res = await fetch(`http://localhost:8000/acciones/${tipo}`, {
    method: "POST",
  });

  if (!res.ok) {
    showToast("Error", "error");

    return;
  }

  const data = await res.json();

  showToast(data.mensaje);
};

const generarComprobante = async (
  servicioId,
  tipo
) => {

  window.open(
    `http://localhost:8000/comprobante/${servicioId}/${tipo}`,
    "_blank"
  );

};
const verificarReporte = async () => {
  if (!servicioActivo.value) return;

  try {
    const response = await fetch(
      `http://localhost:8000/servicios/${servicioActivo.value.id}/reporte`
    );

    if (!response.ok) return;

    const data = await response.json();

    tieneReporte.value = !!data;
  } catch (error) {
    console.log(error);
  }
};

onMounted(() => {
  obtenerServicio();

  obtenerPuntos();

  obtenerNotificacion();
});
</script>