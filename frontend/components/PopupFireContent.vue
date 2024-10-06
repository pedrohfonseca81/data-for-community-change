<template>
  <!-- <div class="p-4 w-64 bg-white rounded-lg shadow-md"> -->
  <div class="font-poppins z-[999999999]" :class="class">
    <div class="flex items-center justify-between gap-2">
      <svg width="22" height="21" viewBox="0 0 18 19" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M0.717499 11C0.717499 9.12618 1.27583 7.31077 2.3925 5.55377C3.50917 3.79693 5.04717 2.24493 7.0065 0.897765C7.48617 0.563098 7.98542 0.543515 8.50425 0.839015C9.02308 1.13468 9.2825 1.5876 9.2825 2.19776V3.30002C9.2825 3.78668 9.45108 4.1946 9.78825 4.52377C10.1252 4.85293 10.5375 5.01752 11.025 5.01752C11.28 5.01752 11.518 4.96227 11.739 4.85177C11.96 4.74143 12.1561 4.58327 12.3273 4.37727C12.4971 4.1666 12.7147 4.03493 12.98 3.98226C13.2455 3.9296 13.4888 3.9841 13.7098 4.14577C14.8162 4.95227 15.6883 5.96002 16.326 7.16902C16.9637 8.37802 17.2825 9.65518 17.2825 11.0005C17.2825 12.499 16.9242 13.8656 16.2075 15.1003C15.4908 16.3349 14.5445 17.3163 13.3685 18.0445C13.683 17.609 13.9281 17.1328 14.1038 16.6158C14.2796 16.0986 14.3675 15.5497 14.3675 14.969C14.3675 14.2434 14.2333 13.5628 13.9648 12.9275C13.6964 12.2923 13.3117 11.7243 12.8107 11.2233L9 7.49227L5.22075 11.2218C4.70908 11.7333 4.3165 12.3051 4.043 12.9373C3.76933 13.5694 3.6325 14.2467 3.6325 14.969C3.6325 15.5469 3.72042 16.0949 3.89625 16.613C4.07192 17.1312 4.317 17.6083 4.6315 18.0445C3.4555 17.3163 2.50917 16.3349 1.7925 15.1C1.07583 13.8653 0.717499 12.4987 0.717499 11ZM9 11.211L10.9247 13.0983C11.1814 13.3559 11.3777 13.6418 11.5135 13.9558C11.6495 14.2699 11.7175 14.6064 11.7175 14.9653C11.7175 15.7036 11.4529 16.3328 10.9237 16.8528C10.3947 17.3726 9.75242 17.6325 8.99675 17.6325C8.24092 17.6325 7.59958 17.3726 7.07275 16.8528C6.54592 16.3328 6.2825 15.7036 6.2825 14.9653C6.2825 14.6101 6.35025 14.2736 6.48575 13.9558C6.62125 13.6381 6.81692 13.3536 7.07275 13.1023L9 11.211Z"
          fill="#B8231B" />
      </svg>

      <div class="w-4/5">
        Satelite: <span class="text-gray-900 font-bold">{{ props.element.satellite }}</span>
      </div>
      <div class="w-fit bg-red-400 p-1 rounded-xl">
        <span class="text-xs text-red-800 truncate font-semibold">C: {{ props.element.confidence }}</span>%
      </div>
    </div>
    <div class="p-2 bg-gray-100 rounded text-gray-800 mt-2 shadow">
      <h3 class="font-bold">Data:</h3>
      <ul class="list-none mt-1 text-xs font-medium text-gray-950 leading-6">
        <li class="flex flex-row items-center">
          <span class="mr-1"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M12 14q-.425 0-.712-.288T11 13t.288-.712T12 12t.713.288T13 13t-.288.713T12 14m-4 0q-.425 0-.712-.288T7 13t.288-.712T8 12t.713.288T9 13t-.288.713T8 14m8 0q-.425 0-.712-.288T15 13t.288-.712T16 12t.713.288T17 13t-.288.713T16 14m-4 4q-.425 0-.712-.288T11 17t.288-.712T12 16t.713.288T13 17t-.288.713T12 18m-4 0q-.425 0-.712-.288T7 17t.288-.712T8 16t.713.288T9 17t-.288.713T8 18m8 0q-.425 0-.712-.288T15 17t.288-.712T16 16t.713.288T17 17t-.288.713T16 18M5 22q-.825 0-1.412-.587T3 20V6q0-.825.588-1.412T5 4h1V2h2v2h8V2h2v2h1q.825 0 1.413.588T21 6v14q0 .825-.587 1.413T19 22zm0-2h14V10H5z" />
            </svg>
          </span>
          Acquisition Date: {{ props.element.acq_date }}
        </li>
        <li class="flex flex-row items-center">
          <span class="mr-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M12 22q-2.075 0-3.537-1.463T7 17q0-1.2.525-2.238T9 13V5q0-1.25.875-2.125T12 2t2.125.875T15 5v8q.95.725 1.475 1.763T17 17q0 2.075-1.463 3.538T12 22m-1-11h2v-1h-1V9h1V7h-1V6h1V5q0-.425-.288-.712T12 4t-.712.288T11 5z" />
            </svg>
          </span>
          Brightness Temperature: {{ props.element.bright_t31 }}
        </li>
        <li class="flex flex-row items-center">
          <span class="mr-1"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M12 23.3L8.65 20H4v-4.65L.7 12L4 8.65V4h4.65L12 .7L15.35 4H20v4.65L23.3 12L20 15.35V20h-4.65zm0-6.3q2.075 0 3.538-1.463T17 12t-1.463-3.537T12 7T8.463 8.463T7 12t1.463 3.538T12 17m0 3.5l2.5-2.5H18v-3.5l2.5-2.5L18 9.5V6h-3.5L12 3.5L9.5 6H6v3.5L3.5 12L6 14.5V18h3.5z" />
            </svg>
          </span>
          Brightness: {{ props.element.brightness }}
        </li>

        <li class="flex flex-row items-center">
          <span class="mr-1"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M12 22q-2.075 0-3.9-.788t-3.175-2.137q-1.35-1.35-2.137-3.175T2 12q0-2.075.788-3.9t2.137-3.175q1.35-1.35 3.175-2.137T12 2q2.075 0 3.9.788t3.175 2.137q1.35 1.35 2.138 3.175T22 12q0 2.075-.788 3.9t-2.137 3.175q-1.35 1.35-3.175 2.138T12 22Zm0-4q.675 0 1.3-.125t1.2-.4q-1.575-.725-2.538-2.175T11 12q0-1.85.963-3.3T14.5 6.525q-.575-.275-1.2-.4T12 6Q9.5 6 7.75 7.738T6 12q0 2.5 1.75 4.25T12 18Z" />
            </svg></span>
          Day/Night: {{ props.element.daynight }}
        </li>
        <li class="flex flex-row items-center">
          <span class="mr-1"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24">
              <path fill="currentColor" d="M3 21v-2h18v2zm4-4v-2h10v2zm-4-4v-2h18v2zm4-4V7h10v2zM3 5V3h18v2z" />
            </svg></span>
          FRP: {{ props.element.frp }}
        </li>
        <li class="flex flex-row items-center">
          <span class="mr-1"><svg width="14" height="13" viewBox="0 0 14 13" fill="none"
              xmlns="http://www.w3.org/2000/svg">

            </svg></span>
          Instrument: {{ props.element.instrument }}
        </li>
      </ul>
    </div>
    <div class="mt-4 flex p-2 gap-2 justify-evenly">
      <button
        class="p-2 text-[#F5FFFA] bg-[#B8231B] shadow-lg rounded-full text-xs flex flex-row items-center justify-around font-bold ">
        LA: {{ props.element.latitude }}
      </button>

      <button
        class="p-2  text-[#F5FFFA] bg-[#B8231B] shadow rounded-full text-xs flex flex-row items-center justify-around font-bold ">
        LN: {{ props.element.longitude }}
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps(["element", "class"]);
</script>
