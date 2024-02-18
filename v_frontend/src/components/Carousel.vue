<template>
    <div class="flex justify-center items-center h-[1000px] ">
    <article class="relative w-[1400px] flex flex-shrink overflow-hidden shadow-2xl">
      <div class="rounded-full bg-gray-600 text-white absolute top-5 right-5 text-sm px-2 text-center z-10">
        <span>{{ currentIndex }}</span>/
        <span>{{ images.length }}</span>
      </div>
  
      <template v-for="(image, index) in images" :key="index">
        <transition 
          enter-active-class="transition transform duration-300"
          enter-class="opacity-0"
          enter-to-class="opacity-100"
          leave-active-class="transition transform duration-300"
          leave-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <figure class="h-[600px]" v-show="currentIndex === index + 1">
            <img :src="image" alt="Image" class="absolute rounded-xl inset-0 z-10 h-full w-full object-cover opacity-70" />
            <figcaption
              class="absolute inset-x-0 bottom-1 z-20 w-96 mx-auto p-4 font-light text-sm text-center tracking-widest leading-snug bg-gray-300 bg-opacity-25"
            >
              Any kind of content here!
              Primum in nostrane potestate est, quid meminerimus? Nulla erit controversia. Vestri haec verecundius, illi
              fortasse constantius.
            </figcaption>
          </figure>
        </transition>
      </template>
  
      <div class="absolute inset-0 flex items-center justify-between">
        <button
          @click="back"
          class="w-11 h-11 flex justify-center items-center rounded-full shadow-md z-10 bg-gray-100 hover:bg-gray-200 ml-4"
        >
          <svg
            class="w-8 h-8 font-bold transition duration-500 ease-in-out transform motion-reduce:transform-none text-gray-500 hover:text-gray-600 hover:-translate-x-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path>
          </svg>
        </button>
  
        <button
          @click="next"
          class="w-11 h-11 flex justify-center items-center rounded-full shadow-md z-10 bg-gray-100 hover:bg-gray-200 mb-0 mr-4"
        >
          <svg
            class="w-8 h-8 font-bold transition duration-500 ease-in-out transform motion-reduce:transform-none text-gray-500 hover:text-gray-600 hover:translate-x-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </article>
</div>

  </template>
  
  <script>
  export default {
    data() {
      return {
        currentIndex: 1,
        images: [
        'https://picsum.photos/id/1032/900/400',
        'https://picsum.photos/id/1033/900/400',
        'https://picsum.photos/id/1037/900/400',
        'https://picsum.photos/id/1035/900/400',
        'https://picsum.photos/id/1036/900/400',
        ]
      };
    },
    methods: {
      back() {
        this.currentIndex = Math.max(1, this.currentIndex - 1);
      },
      next() {
        this.currentIndex = (this.currentIndex % this.images.length) + 1;
      }
    }
  };
  </script>