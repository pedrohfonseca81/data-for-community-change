<template>
    <client-only>
        <div id="map" style="height: 100vh;"></div>
    </client-only>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue';

onMounted(async () => {
    const { default: Leaflet } = await import('leaflet');

    const map = Leaflet.map('map').setView([51.505, -0.09], 13);

    Leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
});
</script>