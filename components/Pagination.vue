<template>
  <div
    class="text-gray-600 w-full p-2 flex flex-col justify-center items-center"
  >
    <div class="flex flex-row no-wrap w-full">
      <button
        type="button"
        class="
          py-2
          px-3
          m-1
          focus:outline-none
          bg-white
          transition
          duration-500
          ease-in-out
          transform
          hover:-translate-y-0.5
          hover:shadow-lg
          rounded-sm
          border
          p-6
        "
        @click="changePage(-1)"
      >
        Назад
      </button>
      <input
        type="range"
        class="flex-grow w-full max-w-lg cursor-pointer"
        v-model="slider"
        min="1"
        :max="pages.length"
        @change="sliderChange"
      />
      <button
        type="button"
        @click="changePage(1)"
        class="
          py-2
          px-3
          m-1
          focus:outline-none
          bg-white
          transition
          duration-500
          ease-in-out
          transform
          hover:-translate-y-0.5
          hover:shadow-lg
          rounded-sm
          border
          p-6
        "
      >
        Вперёд
      </button>
    </div>
    <output
      class="
        text-center
        max-w-lg
        py-2
        px-3
        m-1
        focus:outline-none
        bg-white
        rounded-sm
        p-6
      "
    >
      Страница {{ slider }} из {{ pages.length }}
    </output>
  </div>
</template>

<script>
export default {
  props: {
    count: {
      type: Number,
      required: true,
    },
    per_page: {
      type: String,
      required: true,
    },
    openPage: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      posts: [''],
      slider: '1',
      page: 1,
      pages: [],
    }
  },
  methods: {
    sliderChange() {
      this.page = Number(this.slider)
      this.openPage(this.page)
    },
    changePage(incr) {
      if (this.page === 1 && incr === -1) {
        return
      } else if (this.page === this.pages.length && incr === 1) {
        return
      } else {
        this.page = this.page + incr
        this.slider = this.page
        this.openPage(this.page)
      }
    },
    setPages() {
      let numberOfPages = Math.ceil(this.count / parseInt(this.per_page))
      for (let index = 1; index <= numberOfPages; index++) {
        this.pages.push(index)
      }
    },
  },
  created() {
    this.setPages()
  },
}
</script>

<style scoped>
</style>