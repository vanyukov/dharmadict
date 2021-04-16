<template>
  <div class="container mx-auto sm:px-6">
    <Navbar />
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <Nuxt />
      </div>
    </main>
  </div>
</template>

<style lang="scss" scoped></style>

<script>
import Navbar from '@/components/Navbar'
export default {
  components: {
    Navbar,
  },
}
</script>
