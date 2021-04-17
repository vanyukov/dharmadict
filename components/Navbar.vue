<template>
  <md-toolbar class="md-primary">
    <NuxtLink to="/" class="md-title"> Главная </NuxtLink>
    <p v-if="$fetchState.pending">
      <Loading />
    </p>
    <p v-else-if="$fetchState.error">An error occurred :(</p>
    <NuxtLink
      v-for="item of menu"
      :key="item.id"
      :to="'/' + item.url"
      class="md-title"
    >
      {{ item.title }}
    </NuxtLink>
  </md-toolbar>
</template>

<script>
import Loading from '@/components/Loading'
export default {
  components: {
    Loading,
  },
  data() {
    return {
      menu: [],
    }
  },
  async fetch() {
    this.menu = await this.$api('v1', 'pages')
  },
}
</script>

<style lang="scss" scoped>
.md-progress-spinner {
  margin: 12px;
}
</style>
