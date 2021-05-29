<template>
    <div class="flex flex-col items-center my-4">
        <p v-if="$fetchState.pending"><Loading /></p>
        <p v-else-if="$fetchState.error">Ошибка при загрузке терминов</p>
        <div
            v-else
            class="mt-3 mb-6 w-full shadow-md rounded-md p-2"
            v-for="word of Object.keys(terms)"
            v-bind:key="word"
        >
            <div class="word-title relative">
                <span
                    class="text-xl font-bold p-1"
                    v-for="field of translateFields"
                    v-bind:key="field"
                >
                    {{ terms[word][field] }}
                    {{ separator }}
                </span>
                <button
                    class="arrow arrow_open absolute text-xl p-1 justify-self-end  px-2"
                    @click="toggleTranslete(terms[word].id)"
                    v-if="isWordOpen(terms[word].id)"
                >
                    >
                </button>
                <button
                    class="arrow arrow_close absolute text-xl p-1 justify-self-end px-2"
                    @click="toggleTranslete(terms[word].id)"
                    v-if="!isWordOpen(terms[word].id)"
                >
                    >
                </button>
            </div>
            <div v-if="isWordOpen(terms[word].id)">
                <div
                    class="border rounded-md p-2 mt-2"
                    v-for="meaning of terms[word].meanings"
                    v-bind:key="meaning.id"
                >
                    <div class="flex justify-between">
                        <span>{{ meaning.meaning }}</span>                      
                    </div>
                    <div class="flex mt-2" v-if="meaning.interpretation">
                        {{ meaning.interpretation }}
                    </div>
                    <div class="flex mt-2" v-if="meaning.context">
                        {{ meaning.context }}
                    </div>
                    <div class="flex mt-2" v-if="meaning.rationale">
                        {{ meaning.rationale }}
                    </div>
                </div>
            </div>
        </div> 
        <Pagination 
            :class="$fetchState.pending ? 'fixed bottom-3' : ''"
            :count="count"
            :per_page="per_page"
            :openPage="openPage"
        />     
    </div>
</template>

<script>
export default {
    props: {
        username: {
            type: String,
            required: true
        },
        count: {
            type: Number,
            required: true
        },
        per_page: {
            type: String,
            required: true
        },
        api: {
            type: Function,
            required: true
        }
    },
    data() {
        return {
            translateFields: ['wylie', 'sa2ru', 'sanscrit', 'tibetan', 'sa2en'],
            separator: '/',
            hiddenWordsId: [],
            page: 1,
            terms: {}
        }
    },
    async fetch() {
        try {
            const data = await this.api('v1', `translator/${this.username}/terms?page=${this.page}&per_page=10&order_by=wylie`)
            this.terms = data.terms
        } catch (e) {
            throw new Error('Terms not found')
        }
    },
    methods: {
        openPage(page) {
            this.page = page;
            this.$fetch();
        },
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
    },
}
</script>

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
</style>