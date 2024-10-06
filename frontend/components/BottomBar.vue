<template>
  <div class="fixed w-full h-20 bottom-4 z-[999] flex justify-center">
    <div class="bg-opacity-50 w-4/5 rounded-lg shadow-lg">
      <div
        class="bg-white rounded flex md:justify-evenly justify-center gap-4 items-center w-full h-full"
      >
        <div v-for="page in pages" :key="page.name">
          <NuxtLink :to="page.route">
            <div
              class="flex justify-center w-20 rounded-md bg-opacity-70 items-center flex-col hover:bg-[#98F9C8]"
              :class="page.selected && 'bg-[#98F9C8]'"
            >
              <Icon :name="page.icon" class="text-[#0E874A] text-4xl" />
              <p class="text-md text-[#0E874A]" :class="page.selected && 'font-bold'">
                {{ page.name }}
              </p>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, onMounted } from "vue";

onMounted(() => {
  const route = useRoute();
  const path = route.path;

  pages.forEach((page) => {
    if (page.route === path) {
      page.selected = true;
    } else {
      page.selected = false;
    }
  });
});

const pages = reactive([
  {
    name: "Map",
    icon: "material-symbols:map",
    route: "/",
    selected: false,
  },
  {
    name: "Shelters",
    icon: "material-symbols:family-home-rounded",
    route: "/shelters",
    selected: false,
  },
  {
    name: "Profile",
    icon: "material-symbols:person-2-rounded",
    route: "/profile",
    selected: false,
  },
]);
</script>
