<template>
  <div class="p-2 text-lg">
    <h1>Результаты поиска "{{ this.$route.query.search }}"</h1>
    <p>
      Найдено {{ Object.keys(terms).length }}
      {{
        declOfNum(Object.keys(terms).length, [
          'перевод',
          'перевода',
          'переводов',
        ])
      }}
    </p>
    <div
      class="mt-3 mb-6"
      v-for="words of Object.keys(terms)"
      v-bind:key="words"
    >
      <div
        class="border-2 rounded-md p-2"
        v-for="item of terms[words]"
        v-bind:key="item.id"
      >
        <div class="word-title relative">
          <template v-for="(value, name) in translateFields">
            <span
              v-bind:key="name"
              class="text-sm font-light pl-1"
              v-if="item[name]"
            >
              {{ value }}
            </span>
            <span
              v-bind:key="name"
              class="text-xl font-bold pl-1"
              v-if="item[name]"
            >
              {{ item[name] }}</span
            ><span v-bind:key="name" v-if="item[name]" class="separator"
              >,</span
            >
          </template>
          <button
            class="
              arrow arrow_open
              absolute
              text-xl
              font-bold
              p-1
              justify-self-end
              border-2
              rounded-md
              px-2
            "
            @click="toggleTranslete(item.id)"
            v-if="isWordOpen(item.id)"
          >
            >
          </button>
          <button
            class="
              arrow arrow_close
              absolute
              text-xl
              font-bold
              p-1
              justify-self-end
              border-2
              rounded-md
              px-2
            "
            @click="toggleTranslete(item.id)"
            v-if="!isWordOpen(item.id)"
          >
            >
          </button>
        </div>
        <div v-if="isWordOpen(item.id)">
          <div
            class="border-2 rounded-md p-2 mt-2"
            v-for="meaning of item.meanings"
            v-bind:key="meaning.id"
          >
            <div class="flex justify-between">
              <span class="font-semibold">{{ meaning.meaning }}</span>
              <span>
                {{ meaning.translator.first_name }}
                {{ meaning.translator.last_name }}
              </span>
            </div>

            <div v-for="(value, name) in meaningsFields" v-bind:key="name">
              <div class="flex flex-col mt-2" v-if="meaning[name]">
                <p class="text-gray-500 font-light">{{ value }}:</p>
                {{ meaning[name] }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.word-title {
  padding-right: 40px;
}
.arrow {
  right: 3px;
  top: -4px;
}

.arrow_open {
  transform: rotate(270deg);
}

.arrow_close {
  transform: rotate(90deg);
}

.separator:last-of-type {
  display: none;
}
</style>

<script>
export default {
  data() {
    return {
      translateFields: {
        sa2ru: 'санскр. рус.',
        sanscrit: 'санскр',
        tibetan: 'тиб',
        wylie: 'wylie',
        sa2en: 'санскр. англ.',
      },
      meaningsFields: {
        comment: 'Комментарий',
        context: 'Контекст',
        interpretation: 'Интерпретация',
        rationale: 'Логическое обоснование',
      },
      hiddenWordsId: [],
    }
  },

  async asyncData({ query, $api, error }) {
    try {
      const terms = await $api('v1', `terms/?search=${query.search}`)
      return { terms }
    } catch (e) {
      console.error('file: terms.vue -> asyncData -> e', e)

      return error({
        statusCode: 404,
        message: e.message,
      })
    }
  },

  key(route) {
    return route.query.search
  },

  watchQuery: ['search'],

  methods: {
    toggleTranslete(id) {
      if (this.hiddenWordsId.some(item => id === item)) {
        this.hiddenWordsId = this.hiddenWordsId.filter(item => id !== item)
      } else {
        this.hiddenWordsId.push(id)
      }
    },
    isWordOpen(id) {
      return !this.hiddenWordsId.some(item => id === item)
    },

    declOfNum(number, words) {
      return words[
        number % 100 > 4 && number % 100 < 20
          ? 2
          : [2, 0, 1, 1, 1, 2][number % 10 < 5 ? number % 10 : 5]
      ]
    },
  },

  async beforeMount() {
    if (!Object.keys(this.terms).length) {
      this.terms = await this.$api(
        'v1',
        `terms/?search=${this.$route.query.search}`,
      )
    }
  },
}
</script>
