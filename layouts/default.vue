<template>
  <div class="page-container">
    <Navbar />
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
  min-height: calc(100vh - 64px);
  border: 1px solid rgba(#000, 0.12);
}

.nuxt-link-active {
  color: rgb(201, 201, 201);
}

// Demo purposes only
.md-drawer {
  width: 230px;
  max-width: calc(100vw - 125px);
}
</style>

<script>
import Navbar from '@/components/Navbar'
export default {
  components: {
    Navbar,
  },
}
</script>
