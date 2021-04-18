<template>
  <nav
    class="flex fixed w-full items-center justify-between px-6 h-16 bg-green-500 text-gray-700 border-b border-gray-200 z-10"
  >
    <div class="flex items-center flex-grow">
      <input type="text" name="search" id="search" class="focus:outline-none block w-full rounded-md text-base border-gray-300 h-8 px-2 mr-6 max-w-md" placeholder="Поиск">
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
                d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
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
          <svg
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            stroke="currentColor"
            viewBox="0 0 24 24"
            class="w-6 h-6"
          >
            <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path>
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
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
            </svg>
          </span>
          <span>Переводчики</span></span
        >
      </NuxtLink>
      <hr>
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
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
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
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
            </svg>
          </span>
          <span>Цели проекта "Русский буддийский словарь"</span></span
        >
      </NuxtLink>
      <hr>
      <NuxtLink
        to="/pages"
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
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
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
  watch: {
    isOpen: {
      immediate: true,
      handler(isOpen) {
        if (process.client) {
          if (isOpen) document.body.style.setProperty("overflow", "hidden");
          else document.body.style.removeProperty("overflow");
        }
      }
    }
  },
  mounted() {
    document.addEventListener("keydown", e => {
      if (e.keyCode == 27 && this.isOpen) this.isOpen = false;
    });
  }
};
</script>