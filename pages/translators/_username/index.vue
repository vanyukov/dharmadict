<template>
  <div>
    <div class="flex flex-row items-center">
      <NuxtLink
        to="/pages/translators"
        class="
          ease-in-out
          transform
          text-white
          w-10
          h-10
          p-3
          m-3
          font-bold
          rounded-full
          inline-flex
          items-center
          justify-center
          focus:outline-none
          bg-green-500
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 19l-7-7m0 0l7-7m-7 7h18"
          />
        </svg>
      </NuxtLink>
      <h1 class="inline m-3 text-xl">
        {{
          `${data.translator.first_name} ${data.translator.middle} ${data.translator.last_name}`
        }}
      </h1>
    </div>

    <div class="flex flex-row flex-nowrap mt-6">
      <NuxtLink
        :to="'/translators/' + this.$route.params.username"
        prefetch
        class="
          flex-1
          p-3
          border-b-2
          focus:outline-none
          inline-flex
          items-center
          space-x-2
          justify-center
          text-gray-600
        "
        :class="
          this.$route.name === 'translators-username' ? 'border-green-500' : ''
        "
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 mr-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path d="M12 14l9-5-9-5-9 5 9 5z" />
          <path
            d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"
          />
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"
          />
        </svg>
        Переводчик
      </NuxtLink>
      <NuxtLink
        :to="'/translators/' + this.$route.params.username + '/terms'"
        prefetch
        class="
          flex-1
          p-3
          border-b-2
          focus:outline-none
          inline-flex
          items-center
          space-x-2
          justify-center
          text-gray-600
        "
        :class="this.$route.name === 'terms' ? 'border-green-500' : ''"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 mr-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"
          />
        </svg>
        Термины
      </NuxtLink>
    </div>
    <TranslatorTerms
      v-if="this.$route.name === 'terms'"
      :username="data.translator.username"
      :count="data.count"
      :per_page="'10'"
      :api="$api"
    />
    <AboutTranslator
      v-if="this.$route.name === 'translators-username'"
      :translator="data.translator"
      :about="about"
    />
  </div>
</template>

<script>
export default {
  async asyncData({ params, $api, error }) {
    try {
      const data = await $api(
        'v1',
        `translator/${params.username}/terms?page=1&per_page=1`,
      )

      const about = data.translator.page
        ? await $api('v1', `page/${data.translator.page}`)
        : { content: '' }
      return { data, about }
    } catch (e) {
      return error({
        statusCode: 404,
        message: e.message,
      })
    }
  },
  head() {
    return {
      title: `${this.data.translator.first_name} ${this.data.translator.last_name}`,
      meta: [
        {
          hid: '',
          name: 'content',
          content: `Словарь буддийской терминологии. Переводчик ${this.data.translator.first_name} ${this.data.translator.last_name}`,
        },
      ],
    }
  },
}
</script>
