<template>
  <nav class="bg-green-500">
    <div class="max-w-7xl mx-auto px-4 py-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline">
              <NuxtLink
                to="/"
                exact=""
                active-class=" bg-gray-900 "
                class="px-3 py-2 rounded-md text-sm font-medium text-white focus:outline-none focus:text-white focus:bg-gray-700"
              >
                Главная
              </NuxtLink>
              <p v-if="$fetchState.pending">
                <Loading />
              </p>
              <p v-else-if="$fetchState.error">An error occurred :(</p>
              <NuxtLink
                v-for="item of menu"
                :key="item.id"
                :to="'/' + item.url"
                active-class=" bg-gray-900 "
                class="ml-4 px-3 py-2 rounded-md text-sm font-medium text-white hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700"
              >
                {{ item.shortTitle || item.title }}
              </NuxtLink>
            </div>
            <SearchBar />
          </div>
        </div>
        <div class="-mr-2 flex md:hidden">
          <!-- Mobile menu button -->
          <button
            @click="toggle"
            class="inline-flex items-center bg-gray-900 justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:bg-gray-700 focus:text-white"
          >
            <svg
              :class="[isOpen ? 'hidden' : 'block', 'h-6 w-6']"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              ></path>
            </svg>
            <svg
              :class="[isOpen ? 'block' : 'hidden', 'h-6 w-6']"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <div :class="[isOpen ? '' : 'hidden', 'md:hidden']">
      <div class="flex flex-col px-2 pt-2 pb-3 sm:px-3">
        <NuxtLink
          to="/"
          exact=""
          active-class=" bg-gray-900 "
          class="px-3 py-2 rounded-md text-sm font-medium text-white focus:outline-none focus:text-white focus:bg-gray-700"
        >
          Главная
        </NuxtLink>
        <p v-if="$fetchState.pending">
          <Loading />
        </p>
        <p v-else-if="$fetchState.error">An error occurred :(</p>
        <NuxtLink
          v-for="item of menu"
          :key="item.id"
          :to="'/' + item.url"
          active-class=" bg-gray-900 "
          class="px-3 py-2 rounded-md text-sm font-medium text-white hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700"
        >
          {{ item.shortTitle || item.title }}
        </NuxtLink>
      </div>
    </div>
  </nav>
</template>

<script>
import Loading from '@/components/Loading'
import SearchBar from '@/components/SearchBar'
export default {
  components: {
    Loading,
    SearchBar,
  },
  data() {
    return {
      menu: [],
      isOpen: false,
    }
  },
  async fetch() {
    this.menu = await this.$api('v1', 'mainmenu/links')
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen
    },
  },
}
</script>
