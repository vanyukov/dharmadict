<template>
  <div class="container mx-auto">
    <Navbar />
    <main>
      <div class="max-w-7xl mx-auto py-6 px-6 lg:px-8">
        <Nuxt />
      </div>
    </main>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  components: {
    Navbar,
  },
}
</script>
