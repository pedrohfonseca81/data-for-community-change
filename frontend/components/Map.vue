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
const brStates = await import("../assets/brstates.json");
const rsCities = await import("../assets/RS.json");

const openMenuState = ref(false);

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
    ],
  },
};

onMounted(async () => {
  const { default: Leaflet } = await import("leaflet");

  const map = Leaflet.map("map", {
    zoomControl: false,
  }).setView([-30.08, -51.244], 13);

  Leaflet.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  const greenIcon = Leaflet.icon({
    iconUrl: "~/assets/img/green_pin.png",
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  });

  data.data.results.forEach((element) => {
    const popupNode = document.createElement("div");
    const popupApp = createApp(PopupContent, { element });
    popupApp.mount(popupNode);

    const popup = Leaflet.popup().setContent(popupNode);

    const marker = Leaflet.marker({ icon: greenIcon });

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

  function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
      weight: 5,
      color: "#666",
      dashArray: "",
      fillOpacity: 0.7,
    });

    if (!Leaflet.Browser.ie && !Leaflet.Browser.opera && !Leaflet.Browser.edge) {
      layer.bringToFront();
    }
  }

  function resetHighlight(e) {
    geojson.resetStyle(e.target);
  }


  // L.geoJson(rsCities.default).addTo(map);
  L.geoJson(brStates.default, {
    style: function (feature) {
      console.log(feature);
      return {
        fillColor: "yellow" || "red",
        weight: 0.5,
        opacity: 0.5,
        color: 'darkgray',
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
