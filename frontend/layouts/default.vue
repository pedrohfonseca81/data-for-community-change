<template>
    <div>
        <slot />
        <BottomBar />
    </div>
</template>

<script lang="ts" setup>
useHead({
    script: [{ src: 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js' }],
    link: [
        {
            rel: 'stylesheet',
            href: 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
        },
    ],
});

</script>