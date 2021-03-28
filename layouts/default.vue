<template>
  <div class="page-container">
    <md-toolbar class="md-primary">
      <NuxtLink to="/" class="md-title">
        Главная
      </NuxtLink>
    </md-toolbar>
    <md-app>
      <md-app-content>
        <Nuxt />
      </md-app-content>
    </md-app>
  </div>
</template>

<style lang="scss" scoped>
.md-toolbar + .md-toolbar {
  margin-top: 16px;
}
.md-app {
  max-height: 400px;
  border: 1px solid rgba(#000, 0.12);
}

// Demo purposes only
.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>

<script>
export default {}
</script>
