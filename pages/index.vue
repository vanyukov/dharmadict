<template>
  <div class="container mb-2 mx-auto px-8 w-full flex flex-wrap justify-evenly">
    <div class="flex-initial w-2/3 md:w-1/3 flex">
      <img src="/images/manj.png" id="image" alt="logo" class="w-full h-full" />
    </div>
    <div
      class="flex-2 flex flex-col justify-center w-full md:w-2/3 py-6 md:pl-9"
    >
      <h1 class="text-4xl text-green-500 text-center md:text-left">
        <strong>Буддийская терминология</strong>
        <br />
        <small class="text-xl md:text-3xl"> в русских переводах</small>
      </h1>
      <SearchBar
        class="mt-4 md:mt-8 flex justify-center md:justify-start"
        classBtn="ml-2 px-2 md:px-4 py-1 text-lg rounded-md bg-green-500 text-white"
      />
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
export default {
  components: {
    SearchBar,
  },
}
</script>

<style scoped>
.image {
  width: 100%;
  height: 100%;
}
</style>