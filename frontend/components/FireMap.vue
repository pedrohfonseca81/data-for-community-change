<template>
    <client-only>
        <div class="absolute top-0 w-full p-4 z-[9999]">
            <SearchInput />
            <div class="mt-4">
                <IconButton name="material-symbols:layers-rounded" class="text-2xl text-[#424242]" @click="openMenu" />
                <br />
                <Menu v-if="openMenuState" />
            </div>
        </div>

        <div id="map" style="height: 100vh"></div>
    </client-only>
</template>

<script lang="js" setup>
import { ref, onMounted, resolveComponent, cloneVNode, createApp } from "vue";
import redPin from "~/assets/img/red_pin.png";
const brStates = await import("~/assets/brstates.json");
const { default: fires } = await import("~/assets/fires.json");
const appStore = useAppStore();
const openMenuState = ref(false);


const leafletState = ref(null);

const temperature = [{ "temperature": 34.8, "coordinates": { "longitude": -70.5264976, "latitude": -9.0478679, "properties": { "name": "Acre", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 29.2, "coordinates": { "longitude": -41.9294776, "latitude": -12.285251, "properties": { "name": "Bahia", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.2, "coordinates": { "longitude": -36.6502426, "latitude": -9.6611661, "properties": { "name": "Alagoas", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.8, "coordinates": { "longitude": -51.9161977, "latitude": 1.3545442, "properties": { "name": "Amapá", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.7, "coordinates": { "longitude": -63.5185396, "latitude": -4.479925, "properties": { "name": "Amazonas", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.3, "coordinates": { "longitude": -39.7156073, "latitude": -5.3264703, "properties": { "name": "Ceará", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 34.3, "coordinates": { "longitude": -47.7970891, "latitude": -15.7754462, "properties": { "name": "Distrito Federal", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 25.6, "coordinates": { "longitude": -40.1721991, "latitude": -19.5687682, "properties": { "name": "Espírito Santo", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 41.2, "coordinates": { "longitude": -50.1392928, "latitude": -15.9323662, "properties": { "name": "Goiás", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.5, "coordinates": { "longitude": -45.3930262, "latitude": -5.2085503, "properties": { "name": "Maranhão", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.9, "coordinates": { "longitude": -45.18445836790818, "latitude": -18.57712805, "properties": { "name": "Minas Gerais", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 36.8, "coordinates": { "longitude": -54.4794731, "latitude": -19.5852564, "properties": { "name": "Mato Grosso do Sul", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.2, "coordinates": { "longitude": -37.5919699, "latitude": -8.4116316, "properties": { "name": "Pernambuco", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 38.4, "coordinates": { "longitude": -42.5043787, "latitude": -7.6992782, "properties": { "name": "Piauí", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24.9, "coordinates": { "longitude": -43.2093727, "latitude": -22.9110137, "properties": { "name": "Rio de Janeiro", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 34.6, "coordinates": { "longitude": -36.4781776, "latitude": -5.6781175, "properties": { "name": "Rio Grande do Norte", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 37.7, "coordinates": { "longitude": -62.8277863, "latitude": -10.943145, "properties": { "name": "Rondônia", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.6, "coordinates": { "longitude": -61.3631922, "latitude": 2.135138, "properties": { "name": "Roraima", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24, "coordinates": { "longitude": -53.7680577, "latitude": -29.8425284, "properties": { "name": "Rio Grande do Sul", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 26.8, "coordinates": { "longitude": -51.114965, "latitude": -27.0628367, "properties": { "name": "Santa Catarina", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 29.8, "coordinates": { "longitude": -37.3773519, "latitude": -10.6743911, "properties": { "name": "Sergipe", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.9, "coordinates": { "longitude": -36.7246845, "latitude": -7.1219366, "properties": { "name": "Paraíba", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 35, "coordinates": { "longitude": -48.3716912, "latitude": -10.8855129, "properties": { "name": "Tocantins", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.2, "coordinates": { "longitude": -51.8148872, "latitude": -24.4842187, "properties": { "name": "Paraná", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24.8, "coordinates": { "longitude": -46.6333824, "latitude": -23.5506507, "properties": { "name": "São Paulo", "state": "Brasil", "country": "Brasil" } } }];

onMounted(async () => {
    const { default: Leaflet } = await import("leaflet");

    const map = Leaflet.map("map", {
        zoomControl: false,
    }).setView([-30.08, -51.244], 13);

    leafletState.value = map;

    Leaflet.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    const redIcon = Leaflet.icon({
        iconUrl: redPin,
        iconSize: [30, 30],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41],
    });

    fires.forEach((element) => {
        const marker = Leaflet.marker(null, { icon: redIcon });

        const circle = Leaflet.circle();

        marker.setLatLng({ lat: element.latitude, lng: element.longitude }).addTo(map);
    });

    // function getColor(temp) {
    //   if (temp < 0) {
    //     return "blue";
    //   } else if (temp >= 0 && temp < 20) {
    //     return "yellow";
    //   } else {
    //     return "red";
    //   }
    // }

    function getColor(e) {
        switch (true) {
            case e > 30:
                return "red";
                break;
            case e > 20:
                return "yellow";
                break;
            case e >= 0:
                return "green";
                break;
        }
    }

    Leaflet.geoJson(brStates.default, {
        style: function (feature) {
            const data = temperature.find(e => {
                return e.coordinates.properties.name === feature.geometry_name;
            });

            return {
                fillColor: getColor(data?.temperature),
                weight: 0.5,
                opacity: 0.5,
                color: 'yellow',
                dashArray: 0,
                fillOpacity: 0.2,
            };
        }
    }).addTo(map);

});

function openMenu() {
    openMenuState.value = !openMenuState.value;
}
</script>

<!-- <style>
  .leaflet-popup-content {
  display: flex !important;
  justify-content: center !important;
  }
  
  .leaflet-popup-content-wrapper,
  .leaflet-popup-tip{
    background-color: transparent !important;
  }
  </style> -->