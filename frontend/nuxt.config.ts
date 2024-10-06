// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css', 'leaflet/dist/leaflet.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: ['@nuxtjs/leaflet', '@nuxt/icon', '@pinia/nuxt'],
  // app: {
  //   pageTransition: { name: 'page', mode: 'out-in' }
  // },
});