<template>

<div class="h-64 w-full rounded overflow-hidden relative z-0">

  <l-map
    ref="map"
    :zoom="13"
    :center="center"
    style="height: 100%; width: 100%;"
  >

    <l-tile-layer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />

    <!-- ORIGEN -->
    <l-marker :lat-lng="origen" />

    <!-- DESTINO -->
    <l-marker :lat-lng="destino" />

    <!-- RUTA -->
    <l-polyline
      :lat-lngs="[origen, destino]"
    />

  </l-map>

</div>

</template>

<script setup>
import { ref, onMounted } from "vue";

import {
  LMap,
  LTileLayer,
  LMarker,
  LPolyline
} from "@vue-leaflet/vue-leaflet";

const map = ref(null);

const center = [7.1064458, -73.10781355];

const origen = [7.0951872, -73.1037608];

const destino = [7.1177044, -73.1118663];

onMounted(() => {

  setTimeout(() => {

    const leafletMap = map.value.leafletObject;

    leafletMap.fitBounds([
      origen,
      destino
    ]);

  }, 300);

});
</script>