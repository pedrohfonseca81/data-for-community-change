<template>
  <button
    class="w-fit p-2 rounded-lg bg-[#F5FFFA] flex items-center justify-center"
    :class="props.class"
  >
    <slot />
  </button>
</template>

<script setup>
const props = defineProps(["class"]);
</script>
