<template>
    <div class="text-gray-600">
        <span class="inline-block">
            <button 
                type="button" 
                class="py-2 px-3 mx-1 focus:outline-none bg-white transition duration-500 ease-in-out transform hover:-translate-y-0.5 hover:shadow-lg rounded-sm border p-6" 
                @click="changePage(page, -1)"
            > Назад </button>
        </span>
        <span class="inline-block">
            <button 
                type="button" 
                class="inline-block py-2 px-3 mx-1 focus:outline-none bg-white transition duration-500 ease-in-out transform hover:-translate-y-0.5 hover:shadow-lg rounded-sm border p-6"
                v-for="pageNumber in pages.slice(getFirst(page), getLast(page))" 
                @click="changePage(pageNumber, 0)"
                v-bind:key="pageNumber"
                :class="pageNumber === page ? 'text-green-500' : ''"
            > {{pageNumber}} </button>
        </span>
        <span class="inline-block">
            <button 
                type="button" 
                @click="changePage(page, 1)" 

                class="py-2 px-3 mx-1 focus:outline-none bg-white transition duration-500 ease-in-out transform hover:-translate-y-0.5 hover:shadow-lg rounded-sm border p-6"
            > Вперёд </button>
        </span>
    </div>
</template>

<script>
export default {
    props: {
        count: {
            type: Number,
            required: true
        },
        per_page: {
            type: String,
            required: true
        },
        openPage: {
            type: Function,
            required: true
        }
    },
    data () {
		return {
			posts : [''],
			page: 1,
			pages: [],		
		}
	},
	methods:{
        changePage(page, incr) {
            if (page === 1 && incr === -1) {
                return
            } else if (page === this.pages.length && incr === 1) {
                return
            } else {
                this.page = page + incr;
                this.openPage(this.page);
            }
        },
        getFirst (page) {
            if (page === 1) {
                return 0
            } else if (page === this.pages.length) {
                return page - 3
            } else {
                return page - 2
            }
        },
        getLast (page) {
            if (page === 1) {
                return 3
            } else if (page === this.pages.length) {
                return page
            } else {
                return page + 1
            }
        },
		setPages () {
			let numberOfPages = Math.ceil(this.count / parseInt(this.per_page));
			for (let index = 1; index <= numberOfPages; index++) {
				this.pages.push(index);
			}
		},
	},
	created(){
        this.setPages();
	},
}
</script>

<style scoped>

</style>