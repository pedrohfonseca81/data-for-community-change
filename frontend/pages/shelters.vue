<template>
    <div>
        <h1 class="font-bold text-2xl ml-4 mt-4">Shelters</h1>
        <div class="p-4">
            <SearchInput />
        </div>
        <div>
            <div v-for="element in elements" :key="element.id">
                <ShelterCard :element="element" class="mx-4 my-4" />
            </div>
        </div>
        <div class="my-28"></div>
        <BottomBar />
    </div>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';

const elements = reactive([
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
])
</script>
