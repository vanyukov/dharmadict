<template>
<div>
    <div class="container mb-2 mx-auto px-8 w-full mt-4 md:mt-12 flex flex-wrap">
      <div class="flex-initial w-full md:w-1/3 flex justify-center">
        <img src="/images/logo.jpeg" alt="logo" class="w-1/2 md:w-3/4"/>
      </div>
      <div class="flex-2 flex flex-col justify-center w-full md:w-2/3 py-6">
        <h1 class="text-4xl md:text-5xl lg:text-6xl text-green-500 text-center md:text-left">
          <strong>Буддийская терминология</strong>
          <br>
          <small class="text-xl md:text-2xl"> в русских переводах</small>
        </h1>
      </div>
    </div>

  <div class="container mb-2 mx-auto w-full my-4 md:my-12">
		<ul class="flex flex-col md:flex-row flex-wrap p-4 w-full items-stretch">
      <li class="flex-1 m-3 h-auto">
        <NuxtLink
          to="/pages/parallel_texts"
        >
          <div
            class="select-none w-full h-full flex items-center p-4 transition duration-500 ease-in-out transform hover:-translate-y-2 rounded-2xl border-2 p-6 hover:shadow-2xl border-green-500"
          >
            <h4 class="w-full text-center text-xl">
              Параллельные тексты
            </h4>
          </div>
        </NuxtLink>
      </li>
      <li class="flex-1 m-3 h-auto">
        <NuxtLink
          to="/pages/translators"
        >
          <div
            class="select-none w-full h-full flex items-center p-4 transition duration-500 ease-in-out transform hover:-translate-y-2 rounded-2xl border-2 p-6 hover:shadow-2xl border-green-500"
          >
            <h4 class="w-full text-center text-xl">
              Переводчики
            </h4>
          </div>
        </NuxtLink>
      </li>
    </ul>
  </div>

  <p v-if="$fetchState.pending">
    <Loading />
  </p>
  <p v-else-if="$fetchState.error">An error occurred :(</p>

  <div class="flex w-full px-8 my-12"> 
    <ul class="">
      <li
        v-for="item of menu"
        :key="item.id"
        class="w-full cursor-pointer m-3 my-6"
      >
        <NuxtLink 
          :to="'/' + item.url"
        >
          <h5 class="w-full text-2xl transform hover:translate-x-6 my-1">
            {{ item.title.trim() }}
          </h5>
          <p class="w-full text-sm text-gray-500">
            {{ item.description }} 
          </p>      
        </NuxtLink>
      </li>
    </ul>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      menu: [],
    }
  },
  async fetch() {
    this.menu = (await this.$api('v1', 'mainpage/links'));
  },
}
</script>

<style scoped></style>