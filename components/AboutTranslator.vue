<template>
    <div class="flex flex-col items-center">
        <img 
            :src="translator.img" 
            class="h-48 w-48 rounded-full shadow-md m-6"
        />
        <div class="shadow-md rounded-md p-4 py-8 m-6 w-full html-content" v-html="about.content">
        </div>
    </div>
</template>

<script>
export default {
    props: {
        translator: {
            type: Object,
            required: true
        },
        about: {
            type: Object,
            required: false
        }
    },
}
</script>

<style scoped>
    .html-content::v-deep h2 {
        margin-top: 4rem;
        margin-bottom: 2rem;
        font-size: 1.25rem;
    }
    .html-content::v-deep p {
        margin-top: 1rem;
        margin-bottom: 1rem; 
    }
    .html-content::v-deep ul {
        list-style-type: disc;
        margin-left: 1rem;
    }
</style>