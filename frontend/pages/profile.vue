<template>
    <div>
        <div class="w-full h-full absolute z-[-0]">
                <img src="~/assets/img/frame1.svg" class="fixed top-0 left-[-210px]" alt="">
                <img src="~/assets/img/frame2.svg" class="fixed bottom-[-20px] right-[-240px]" alt="">
        </div>
        <div class="flex flex-col items-center">
            <h1 class="text-2xl my-6 font-normal">My Profile</h1>
            <div class="flex flex-col items-center gap-2 z-[100]">
                <div class="bg-slate-600 w-28 h-28 rounded-full"></div>
                <h2 class="text-xl font-bold text-[#424242]">Pedro Vinícius Paladino Carvalho</h2>
            </div>
            <div class="flex items-center bg-[#F5F5F5] w-5/6 rounded-lg py-4 mt-4">
                <div class="w-full flex flex-col items-center">
                    <p class="text-base text-[#424242]">Total Donation</p>
                    <p class="font-bold text-[#212121]">R$ 3.520,20</p>
                </div>
                <div class="border-2 rounded-lg h-16 border-[#E0E0E0]">
                </div>
                <div class="w-full flex flex-col items-center">
                    <p class="text-base text-[#424242]">Sheltered Donated</p>
                    <p class="font-bold text-[#212121]">55 shelter(s)</p>
                </div>
            </div>
        </div>
        <div class="flex mt-8 gap-12 flex-col mx-4">
            <div class="flex gap-4">
                <Icon name="material-symbols:person-2-rounded" class="text-2xl text-[#424242]" />
                <p class="text-base">My Datas</p>
            </div>
            <div class="flex gap-4">
                <Icon name="material-symbols:volunteer-activism-rounded" class="text-2xl text-[#424242]" />
                <p class="text-base">Recents Donate</p>
            </div>
            <div class="flex gap-4">
                <Icon name="material-symbols:credit-card" class="text-2xl text-[#424242]" />
                <p class="text-base">Payments</p>
            </div>
            <div class="flex gap-4">
                <Icon name="material-symbols:info-rounded" class="text-2xl text-[#424242]" />
                <p class="text-base">Notifications</p>
            </div>
            <div class="flex gap-4">
                <Icon name="material-symbols:output-rounded" class="text-2xl text-red-600" />
                <p class="text-base text-red-600">Sign out</p>
            </div>

        </div>
        <BottomBar />
    </div>
</template>