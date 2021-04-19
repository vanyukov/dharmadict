<template>
<div>
  <div class="flex space-x-4">
    <div class="flex-initial">
      <img src="/images/logo.jpeg" alt="logo" />
    </div>
    <div class="flex-1">
      <h1 class="text-3xl text-green-500">
        <strong>Буддийская терминология</strong>
        <br>
        <small> в русских переводах</small>
      </h1>
    </div>
  </div>

  <div class="container mb-2 mx-auto w-full my-12">
		<ul class="flex flex-col md:flex-row flex-wrap p-4 w-full items-stretch">
      <li class="flex-1 m-3 h-auto">
        <NuxtLink
          to="/pages/all"
        >
          <div
            class="select-none w-full h-full flex items-center p-4 transition duration-500 ease-in-out transform hover:-translate-y-2 rounded-2xl border-2 p-6 hover:shadow-2xl border-green-500"
          >
            <h4 class="w-full text-center text-xl">
              Все термины
            </h4>
          </div>
        </NuxtLink>
      </li>
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

  <div class="flex w-full px-8 my-12"> 
    <ul class="">
      <li
        v-for="item of menu"
        :key="item.id"
        class="w-full transform hover:translate-x-6 cursor-pointer m-3 my-6"
      >
        <br>
        <NuxtLink 
          :to="'/' + item.url"
        >
          <h5 class="w-full text-2xl">
            {{ item.title.trim() }}
          </h5>          
        </NuxtLink>
        <br>
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
    const mainPages = ['', 'pages/translators', 'pages/parallel_texts']
    this.menu = (await this.$api('v1', 'pages')).filter(item => !mainPages.includes(item.url));
    console.log(this.menu);
  },
}
</script>

<style scoped></style>
