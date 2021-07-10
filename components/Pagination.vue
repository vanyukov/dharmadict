<template>
  <div
    class="text-gray-600 w-full p-2 flex flex-col justify-center items-center"
  >
    <div class="flex flex-row no-wrap w-full justify-center items-center">
      <NuxtLink
        :to="
          '/translators/' +
          this.$route.params.username +
          '/terms/' +
          Math.max(1, this.page - 1)
        "
        class="py-2 px-3 m-1 focus:outline-none bg-white rounded-sm border p-6"
        v-bind:disabled="this.page <= 1"
      >
        Назад
      </NuxtLink>
      <input
        type="range"
        class="
          rounded-lg
          border-2
          overflow-hidden
          appearance-none
          h-3
          w-full
          cursor-pointer
          disabled:opacity-50
        "
        v-model="slider"
        min="1"
        :max="numberOfPages"
        @change="sliderChange"
      />
      <NuxtLink
        :to="
          '/translators/' +
          this.$route.params.username +
          '/terms/' +
          Math.min(numberOfPages, this.page + 1)
        "
        class="
          py-2
          px-3
          m-1
          focus:outline-none
          bg-white
          rounded-sm
          border
          p-6
          disabled:opacity-50
        "
        v-bind:disabled="this.page == numberOfPages"
      >
        Вперед
      </NuxtLink>
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
      Страница {{ slider }} из {{ numberOfPages }}
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
      type: Number,
      required: true,
    },
    page: {
      type: Number,
      default: 1,
    },
  },
  data() {
    return {
      slider: this.$route.params.page || 1,
    }
  },
  watch: {
    '$route.query': 'updateSlider',
  },
  methods: {
    sliderChange() {
      this.$router.push(
        '/translators/' + this.$route.params.username + '/terms/' + this.slider,
      )
    },
    updateSlider() {
      this.slider = this.$route.params.page || 1
    },
  },
  computed: {
    numberOfPages: {
      cache: true,
      get: function () {
        return Math.ceil(this.count / parseInt(this.per_page))
      },
    },
  },
}
</script>

<style scoped>
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type='range']::-webkit-slider-thumb {
    width: 15px;
    -webkit-appearance: none;
    appearance: none;
    height: 15px;
    cursor: ew-resize;
    background: #e5e7eb;
    box-shadow: -405px 0 0 400px #10b981;
    border-radius: 50%;
    border: 1px solid #d1d5db;
  }
}
</style>