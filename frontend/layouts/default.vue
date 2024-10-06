<template>
  <div>
    <slot />
  </div>
</template>

<style>
html,
body {
  background-color: #f5fffa;
}
</style>

<script lang="ts" setup>
useHead({
  script: [
    { src: "https://unpkg.com/leaflet/dist/leaflet.js" },
    { src: "https://unpkg.com/vue2-leaflet" },
  ],
  link: [
    {
      rel: "stylesheet",
      href: "https://unpkg.com/leaflet/dist/leaflet.css",
    },
    {
      rel: "preconnect",
      href: 'https://fonts.googleapis.com"',
    },
    {
      rel: "preconnect",
      href: "https://fonts.gstatic.com",
      crossorigin: true,
    },
    {
      rel: "stylesheet",
      href:
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
    },
  ],
});
</script>
