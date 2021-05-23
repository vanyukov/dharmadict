<template>
  <div>
    <div
      class="container mb-2 mx-auto px-8 w-full mt-4 md:mt-12 flex flex-wrap"
    >
      <div class="flex-initial w-full md:w-1/3 flex justify-center">
        <img src="/images/logo.jpeg" alt="logo" class="w-1/2 md:w-3/4" />
      </div>
      <div class="flex-2 flex flex-col justify-center w-full md:w-2/3 py-6">
        <h1
          class="text-4xl md:text-5xl lg:text-6xl text-green-500 text-center md:text-left"
        >
          <strong>Буддийская терминология</strong>
          <br />
          <small class="text-xl md:text-2xl"> в русских переводах</small>
        </h1>
      </div>
    </div>

    <ul
      class="container list-none mb-2 mx-auto w-full my-4 md:my-12 flex flex-col md:flex-row flex-wrap p-4 items-stretch"
    >
      <li
        class="m-3 flex-1 h-auto select-none h-full items-center p-4 transition duration-500 ease-in-out transform hover:-translate-y-0.5 hover:shadow-lg rounded-2xl border-2 p-6 border-green-500 text-center text-xl"
      >
        <NuxtLink to="/pages/parallel_texts"> Параллельные тексты </NuxtLink>
      </li>
      <li
        class="m-3 flex-1 h-auto select-none h-full items-center p-4 transition duration-500 ease-in-out transform hover:-translate-y-0.5 hover:shadow-lg rounded-2xl border-2 p-6 border-green-500 text-center text-xl"
      >
        <NuxtLink to="/pages/translators"> Переводчики </NuxtLink>
      </li>
    </ul>

    <p v-if="$fetchState.pending">
      <Loading />
    </p>
    <p v-else-if="$fetchState.error">An error occurred :(</p>

    <ul class="flex flex-col list-none w-full px-8 my-12">
      <li
        v-for="item of menu"
        :key="item.id"
        class="group w-full cursor-pointer my-6"
      >
        <NuxtLink :to="'/' + item.url">
          <h2 class="w-full text-2xl transform group-hover:translate-x-6 my-1">
            {{ item.title.trim() }}
          </h2>
          <p class="w-full text-sm text-gray-500">
            {{ item.description }}
          </p>
        </NuxtLink>
      </li>
    </ul>
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
    this.menu = (await this.$api('v1', 'mainpage/links')).sort(
      (a, b) => new Date(a.modified) - new Date(b.modified),
    )
  },
}
</script>

<style scoped></style>