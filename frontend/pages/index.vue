<template>
    <div>
        <SplashScreen>
            <div v-if="app.filters.forestFire">
                <FireMap />
            </div>

            <div v-else>
                <Map />
            </div>
            
            <BottomBar />
        </SplashScreen>
    </div>
</template>

<script lang="ts" setup>
const app = useAppStore();
</script>

d