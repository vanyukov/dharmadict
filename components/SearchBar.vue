<template>
  <div class="mt-2 flex md:justify-center content-center">
    <input
      class="search-input px-2 rounded-sm"
      type="text"
      placeholder=""
      v-model="query"
      v-on:keyup.enter="search"
    />
    <button
      class="ml-2 px-2 rounded-sm bg-white text-green-500"
      @click="search"
    >
      Найти
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
    }
  },
  methods: {
    search() {
      if (!this.query) return null

      const path = `/terms/?search=${this.query}`
      this.query = ''
      this.$nuxt.$router.replace({ path })
    },
  },
}
</script>

<style scoped>
.search-input {
  max-width: calc(100vw - 90px);
}
</style>