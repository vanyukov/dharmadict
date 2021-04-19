<template>
  <nav
    class="flex fixed w-full items-center justify-between px-6 h-16 bg-green-500 text-gray-700 border-b border-gray-200 z-10"
  >
    <div class="flex items-center flex-grow">
        <!-- <input type="text" name="search" id="search" class="focus:outline-none w-full rounded-md text-base border-gray-300 h-8 px-2 mr-6 max-w-md" placeholder="Поиск"> -->

      <div class="w-full relative h-8 max-w-md focus:outline-none mr-6">
        <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search w-4 h-4 absolute my-auto inset-y-0 ml-3 left-0 z-10 text-gray-700 dark:text-gray-300 w-4 h-4 absolute my-auto inset-y-0 ml-3 left-0 z-10 text-gray-700 dark:text-gray-300">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" class="form-control w-full box px-10 text-gray-700 dark:text-gray-300 placeholder-theme-13 h-8 focus:outline-none rounded-md" placeholder="Поиск">
      </div>
      

    </div>
    <div class="flex items-center">
      <div class="md:block md:flex md:justify-between md:bg-transparent">
        <button class="focus:outline-none transform" aria-label="Open Menu" @click="drawer">
          <svg
            fill="none"
            stroke="white"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            viewBox="0 0 24 24"
            class="w-8 h-8"
          >
            <path d="M 4 6 h 16 M 4 12 h 16 M 10 18 h 10"></path>
          </svg>
        </button>
      </div>
    </div>
    <transition
      enter-class="opacity-0"
      enter-active-class="ease-out transition-medium"
      enter-to-class="opacity-100"
      leave-class="opacity-100"
      leave-active-class="ease-out transition-medium"
      leave-to-class="opacity-0"
    >
      <div
        @keydown.esc="isOpen = false"
        v-show="isOpen"
        class="z-10 fixed inset-0 transition-opacity"
      >
        <div
          @click="isOpen = false"
          class="absolute inset-0 bg-black opacity-50"
          tabindex="0"
        ></div>
      </div>
    </transition>
    <aside
      class="transform top-0 right-0 w-full md:w-64 bg-white fixed h-full overflow-auto ease-in-out transition-all duration-300 z-30"
      :class="isOpen ? 'translate-x-0' : 'translate-x-full'"
    >
      <span
        @click="isOpen = false"
        class="flex w-full items-center p-4 border-b justify-end"
      >
        <button class="mr-2 z-50 focus:outline-none transform" aria-label="Open Menu" @click="drawer">
          <svg
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            viewBox="0 0 24 24"
            class="w-8 h-8"
          >
            <path d="m 4 6 l 12 12 M 16 6 l -12 12"></path>
          </svg>
        </button>
      </span>

      <NuxtLink
        to="/"
        exact=""
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              class="w-6 h-6"
            >
              <path
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
              ></path>
            </svg>
          </span>

          <span>Главная</span></span
        >
      </NuxtLink>
      <!-- <Loading />
      <p v-if="$fetchState.pending">
        <Loading />
      </p>
      <p v-else-if="$fetchState.error">An error occurred :(</p> -->

      <NuxtLink
        to="/pages/"
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z" />
            </svg>
          </span>
          <span>Все термины</span></span
        >
      </NuxtLink>

      <NuxtLink
        to="/pages/parallel_texts"
      >
      <span
        @click="isOpen = false"
        class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
        ><span class="mr-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
        </span>
        <span>Параллельные тексты</span></span
      >
      </NuxtLink>
      <NuxtLink
        to="/pages/translators"
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M12 14l9-5-9-5-9 5 9 5z" />
              <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
            </svg>
          </span>
          <span>Переводчики</span></span
        >
      </NuxtLink>
      <!-- <hr>
      <NuxtLink
        to="/pages/translation_features"
      >
      <span
        @click="isOpen = false"
        class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
        ><span class="mr-2">
          <svg
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            viewBox="0 0 24 24"
            class="w-6 h-6"
          >
            <path
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
        </span>
        <span>Особенности переводов</span></span
      >
      </NuxtLink>
      <NuxtLink
        to="/pages/history"
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </span>
          <span>История буддийских текстов в России</span></span
        >
      </NuxtLink>
      <NuxtLink
        to="/pages/about"
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
            </svg>
          </span>
          <span>Цели проекта "Русский буддийский словарь"</span></span
        >
      </NuxtLink> -->
      <hr>
      <NuxtLink
        to="/pages"
      >
        <span
          @click="isOpen = false"
          class="flex items-center p-4 hover:bg-indigo-500 hover:text-white "
          ><span class="mr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
            </svg>
          </span>
          <span>Предложить термин для перевода</span></span
        >
      </NuxtLink>
    </aside>
  </nav>
</template>

<script>
import Loading from '@/components/Loading'
export default {
  components: {
    Loading,
  },
  data() {
    return {
      // menu: [],
      isOpen: false,
    }
  },
  // async fetch() {
  //   this.menu = await this.$api('v1', 'pages');
  // },
  methods: {
    drawer() {
      this.isOpen = !this.isOpen;
    }
  },
  // watch: {
  //   isOpen: {
  //     immediate: true,
  //     // handler(isOpen) {
  //     //   if (process.client) {
  //     //     if (isOpen) document.body.style.setProperty("overflow", "hidden");
  //     //     else document.body.style.removeProperty("overflow");
  //     //   }
  //     // }
  //   }
  // },
  mounted() {
    document.addEventListener("keydown", e => {
      if (e.keyCode == 27 && this.isOpen) this.isOpen = false;
    });
  }
};
</script>