<template>
  <div>
    <input
      class="search-input text-lg px-2 rounded-lg border-green-500 border-2"
      type="text"
      placeholder=""
      v-model="query"
      v-on:keyup.enter="search"
    />
    <button v-bind:class="classBtn" @click="search">Найти</button>
  </div>
</template>

<script>
export default {
  props: ['classBtn'],
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