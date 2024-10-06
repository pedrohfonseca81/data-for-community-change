<template>
    <Transition>
        <div v-if="app.isLoading">
            <div class="w-full h-full absolute bg-[#F5FFFA]">
                <img src="~/assets/img/frame1.svg" class="fixed top-0 left-[-20px]" alt="">
                <img src="~/assets/img/frame2.svg" class="fixed bottom-[-60px] right-[-80px]" alt="">
                <div class="flex justify-center items-center gap-2 h-full">
                    <img src="~/assets/img/logo.png" width="82px"></img>
                    <div>
                        <h3 class="text-4xl"><span class="font-bold">Resk.</span><span class="font-normal">us</span>
                        </h3>
                        <p class="text-base text-[#616161] font-normal">Where Solidarity Meets Need</p>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <slot />
        </div>
    </Transition>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
const app = useAppStore()

onMounted(() => {
    setTimeout(() => {
        app.setLoading(false);
    }, 1000);
});
</script>


<style>
.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}
</style>