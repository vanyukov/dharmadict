<template>
  <div>
    <h1>{{ post.title }}</h1>
    <md-content v-html="post.content" />
  </div>
</template>

<script>
export default {
  async asyncData({ params, $api }) {
    const post = await $api('v1', `page/pages/${params.id}`)
    return { post }
  },
}
</script>
