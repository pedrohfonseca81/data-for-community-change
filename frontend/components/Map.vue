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
import PopupContent from "./PopupContent.vue";
import greenPin from "~/assets/img/green_pin.png";
const brStates = await import("../assets/brstates.json");
const appStore = useAppStore();
const openMenuState = ref(false);

const leafletState = ref(null);

const temperature = [{ "temperature": 34.8, "coordinates": { "longitude": -70.5264976, "latitude": -9.0478679, "properties": { "name": "Acre", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 29.2, "coordinates": { "longitude": -41.9294776, "latitude": -12.285251, "properties": { "name": "Bahia", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.2, "coordinates": { "longitude": -36.6502426, "latitude": -9.6611661, "properties": { "name": "Alagoas", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.8, "coordinates": { "longitude": -51.9161977, "latitude": 1.3545442, "properties": { "name": "Amapá", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.7, "coordinates": { "longitude": -63.5185396, "latitude": -4.479925, "properties": { "name": "Amazonas", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.3, "coordinates": { "longitude": -39.7156073, "latitude": -5.3264703, "properties": { "name": "Ceará", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 34.3, "coordinates": { "longitude": -47.7970891, "latitude": -15.7754462, "properties": { "name": "Distrito Federal", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 25.6, "coordinates": { "longitude": -40.1721991, "latitude": -19.5687682, "properties": { "name": "Espírito Santo", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 41.2, "coordinates": { "longitude": -50.1392928, "latitude": -15.9323662, "properties": { "name": "Goiás", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.5, "coordinates": { "longitude": -45.3930262, "latitude": -5.2085503, "properties": { "name": "Maranhão", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.9, "coordinates": { "longitude": -45.18445836790818, "latitude": -18.57712805, "properties": { "name": "Minas Gerais", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 36.8, "coordinates": { "longitude": -54.4794731, "latitude": -19.5852564, "properties": { "name": "Mato Grosso do Sul", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 33.2, "coordinates": { "longitude": -37.5919699, "latitude": -8.4116316, "properties": { "name": "Pernambuco", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 38.4, "coordinates": { "longitude": -42.5043787, "latitude": -7.6992782, "properties": { "name": "Piauí", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24.9, "coordinates": { "longitude": -43.2093727, "latitude": -22.9110137, "properties": { "name": "Rio de Janeiro", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 34.6, "coordinates": { "longitude": -36.4781776, "latitude": -5.6781175, "properties": { "name": "Rio Grande do Norte", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 37.7, "coordinates": { "longitude": -62.8277863, "latitude": -10.943145, "properties": { "name": "Rondônia", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.6, "coordinates": { "longitude": -61.3631922, "latitude": 2.135138, "properties": { "name": "Roraima", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24, "coordinates": { "longitude": -53.7680577, "latitude": -29.8425284, "properties": { "name": "Rio Grande do Sul", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 26.8, "coordinates": { "longitude": -51.114965, "latitude": -27.0628367, "properties": { "name": "Santa Catarina", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 29.8, "coordinates": { "longitude": -37.3773519, "latitude": -10.6743911, "properties": { "name": "Sergipe", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.9, "coordinates": { "longitude": -36.7246845, "latitude": -7.1219366, "properties": { "name": "Paraíba", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 35, "coordinates": { "longitude": -48.3716912, "latitude": -10.8855129, "properties": { "name": "Tocantins", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 31.2, "coordinates": { "longitude": -51.8148872, "latitude": -24.4842187, "properties": { "name": "Paraná", "state": "Brasil", "country": "Brasil" } } }, { "temperature": 24.8, "coordinates": { "longitude": -46.6333824, "latitude": -23.5506507, "properties": { "name": "São Paulo", "state": "Brasil", "country": "Brasil" } } }];

// const data = {
//   statusCode: 200,
//   message: "Successfully get shelters",
//   data: {
//     page: 1,
//     perPage: 20,
//     count: 859,
//     results: [
//       {
//         id: "b69c8fd1-d27a-4ac0-b24b-ac2a015dbe2a",
//         name: "Clube De Mães Idalina Vargas [centro De Distribuição]",
//         pix: null,
//         address: "R. Horacildo Albuquerque Do Canto, 119, Lami - Porto Alegre",
//         street: "R. Horacildo Albuquerque Do Canto",
//         neighbourhood: "Lami",
//         city: "Porto Alegre",
//         streetNumber: "119",
//         zipCode: "91787-669",
//         capacity: 0,
//         petFriendly: false,
//         shelteredPeople: 0,
//         prioritySum: 0,
//         verified: false,
//         latitude: -30.227734319810843,
//         longitude: -51.09758177116432,
//         actived: true,
//         category: "Shelter",
//         createdAt: "2024-06-14T13:16:26.875Z",
//         updatedAt: "2024-06-14T13:16:47.752Z",
//         shelterSupplies: [],
//       },
//       {
//         id: "d33332c9-bf71-4de5-9115-b00f4bc83769",
//         name:
//           "Projeto Social Vem Ser Jiu-jitsu [ponto De Coleta E Centro De Distribuição]",
//         pix: null,
//         address: "R. Selso Fidélis Jardim, 733, Olaria - Canoas",
//         street: "R. Selso Fidélis Jardim",
//         neighbourhood: "Olaria",
//         city: "Canoas",
//         streetNumber: "733",
//         zipCode: "92035-020",
//         capacity: 0,
//         petFriendly: false,
//         shelteredPeople: 0,
//         prioritySum: 0,
//         verified: false,
//         latitude: -29.922362993203667,
//         longitude: -51.12373790136875,
//         actived: true,
//         category: "Shelter",
//         createdAt: "2024-06-14T13:05:56.205Z",
//         updatedAt: "2024-06-14T13:06:15.593Z",
//         shelterSupplies: [],
//       },
//       {
//         id: "f14d4112-22b4-4d80-8cfb-8778d6171a84",
//         name: "Galpão - Ponta Grossa",
//         pix: null,
//         address: "Avenida Principal Da Ponta Grossa, 191, Ponta Grossa - Porto Alegre",
//         street: "Avenida Principal Da Ponta Grossa",
//         neighbourhood: "Ponta Grossa",
//         city: "Porto Alegre",
//         streetNumber: "191",
//         zipCode: "91778-083",
//         capacity: 28,
//         petFriendly: false,
//         shelteredPeople: 28,
//         prioritySum: 0,
//         verified: false,
//         latitude: -30.178590176149427,
//         longitude: -51.17830283204598,
//         actived: true,
//         category: "Shelter",
//         createdAt: "2024-06-14T12:43:51.007Z",
//         updatedAt: "2024-06-13T12:43:51.007Z",
//         shelterSupplies: [],
//       },
//     ],
//   },
// };

const data = {
  statusCode: 200,
  message: "Successfully get shelters",
  data: {
    page: 1,
    perPage: 20,
    count: 859,
    results: [
      {
        id: "b69c8fd1-d27a-4ac0-b24b-ac2a015dbe2a",
        name: "Clube De Mães Idalina Vargas [centro De Distribuição]",
        pix: null,
        address: "R. Horacildo Albuquerque Do Canto, 119, Lami - Porto Alegre",
        street: "R. Horacildo Albuquerque Do Canto",
        neighbourhood: "Lami",
        city: "Porto Alegre",
        streetNumber: "119",
        zipCode: "91787-669",
        capacity: 0,
        petFriendly: false,
        shelteredPeople: 0,
        prioritySum: 0,
        verified: false,
        latitude: -30.227734319810843,
        longitude: -51.09758177116432,
        actived: true,
        category: "Shelter",
        createdAt: "2024-06-14T13:16:26.875Z",
        updatedAt: "2024-06-14T13:16:47.752Z",
        shelterSupplies: [],
      },
      {
        id: "d33332c9-bf71-4de5-9115-b00f4bc83769",
        name:
          "Projeto Social Vem Ser Jiu-jitsu [ponto De Coleta E Centro De Distribuição]",
        pix: null,
        address: "R. Selso Fidélis Jardim, 733, Olaria - Canoas",
        street: "R. Selso Fidélis Jardim",
        neighbourhood: "Olaria",
        city: "Canoas",
        streetNumber: "733",
        zipCode: "92035-020",
        capacity: 0,
        petFriendly: false,
        shelteredPeople: 0,
        prioritySum: 0,
        verified: false,
        latitude: -29.922362993203667,
        longitude: -51.12373790136875,
        actived: true,
        category: "Shelter",
        createdAt: "2024-06-14T13:05:56.205Z",
        updatedAt: "2024-06-14T13:06:15.593Z",
        shelterSupplies: [],
      },
      {
        id: "f14d4112-22b4-4d80-8cfb-8778d6171a84",
        name: "Galpão - Ponta Grossa",
        pix: null,
        address: "Avenida Principal Da Ponta Grossa, 191, Ponta Grossa - Porto Alegre",
        street: "Avenida Principal Da Ponta Grossa",
        neighbourhood: "Ponta Grossa",
        city: "Porto Alegre",
        streetNumber: "191",
        zipCode: "91778-083",
        capacity: 28,
        petFriendly: false,
        shelteredPeople: 28,
        prioritySum: 0,
        verified: false,
        latitude: -30.178590176149427,
        longitude: -51.17830283204598,
        actived: true,
        category: "Shelter",
        createdAt: "2024-06-14T12:43:51.007Z",
        updatedAt: "2024-06-13T12:43:51.007Z",
        shelterSupplies: [],
      },
      {
        id: "a12f4ed9-3d18-4dfd-aec6-9481fd0d9e4f",
        name: "Centro Comunitário São João",
        pix: "centrosaojoao@pix.com",
        address: "Av. São João, 1456, Partenon - Porto Alegre",
        street: "Av. São João",
        neighbourhood: "Partenon",
        city: "Porto Alegre",
        streetNumber: "1456",
        zipCode: "91530-350",
        capacity: 50,
        petFriendly: true,
        shelteredPeople: 32,
        prioritySum: 15,
        verified: true,
        latitude: -30.039713,
        longitude: -51.172973,
        actived: true,
        category: "Shelter",
        createdAt: "2024-05-20T10:20:00.000Z",
        updatedAt: "2024-06-10T10:20:00.000Z",
        shelterSupplies: [
          { item: "Cestas básicas", quantity: 10 },
          { item: "Cobertores", quantity: 25 },
        ],
      },
      {
        id: "b98d88f4-1c9e-45d7-8d1c-df432f60cc98",
        name: "Associação dos Moradores da Tristeza",
        pix: "associacaotristeza@pix.com",
        address: "R. Dr. Pereira Neto, 78, Tristeza - Porto Alegre",
        street: "R. Dr. Pereira Neto",
        neighbourhood: "Tristeza",
        city: "Porto Alegre",
        streetNumber: "78",
        zipCode: "91920-000",
        capacity: 40,
        petFriendly: true,
        shelteredPeople: 35,
        prioritySum: 8,
        verified: true,
        latitude: -30.087635,
        longitude: -51.246089,
        actived: true,
        category: "Shelter",
        createdAt: "2024-06-05T09:00:00.000Z",
        updatedAt: "2024-06-15T09:00:00.000Z",
        shelterSupplies: [
          { item: "Água mineral", quantity: 50 },
          { item: "Roupas", quantity: 200 },
        ],
      },
      {
        id: "e43c7f8b-4e7e-42ad-a973-7ad9130e4b15",
        name: "Casa de Apoio Esperança",
        pix: "casaesperanca@pix.com",
        address: "R. das Palmeiras, 567, Centro - Viamão",
        street: "R. das Palmeiras",
        neighbourhood: "Centro",
        city: "Viamão",
        streetNumber: "567",
        zipCode: "94410-520",
        capacity: 30,
        petFriendly: false,
        shelteredPeople: 20,
        prioritySum: 10,
        verified: true,
        latitude: -30.082473,
        longitude: -51.022587,
        actived: true,
        category: "Shelter",
        createdAt: "2024-04-12T12:30:00.000Z",
        updatedAt: "2024-05-12T12:30:00.000Z",
        shelterSupplies: [
          { item: "Medicamentos", quantity: 15 },
          { item: "Fraldas", quantity: 100 },
        ],
      },
    ],
  },
};

appStore.$subscribe((mutation, state) => {
  if(state.filters.temperature) {
    
  }
});


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

  const greenIcon = Leaflet.icon({
    iconUrl: greenPin,
    iconSize: [80, 80],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  });

  data.data.results.forEach((element) => {
    const popupNode = document.createElement("div");
    const popupApp = createApp(PopupContent, { element });
    popupApp.mount(popupNode);

    const popup = Leaflet.popup().setContent(popupNode);

    const marker = Leaflet.marker(null, { icon: greenIcon });

    const circle = Leaflet.circle();

    marker.bindPopup(popup).openPopup();
    marker.setLatLng({ lat: element.latitude, lng: element.longitude }).addTo(map);

    marker.on("click", function (e) {
      marker.openPopup();
    });

    marker.on("mouseover", function (e) {
      marker.openPopup();
    });
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
