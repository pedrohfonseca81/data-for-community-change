<template>
    <Button>
        <Icon :name="props.name" :class="props.class" />
    </Button>
</template>

<script setup>
const props = defineProps(['name', 'class'])
</script>
