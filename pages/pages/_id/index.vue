<template>
  <div>
    <h1>{{ post.title }}</h1>
    <div v-html="post.content" />
  </div>
</template>

<script>
export default {
  async asyncData({ params, $api, error }) {
    try {
      const post = await $api('v1', `page/pages/${params.id}`)
      return { post }
    } catch (e) {
      return error({
        statusCode: 404,
        message: e.message,
      })
    }
  },
}
</script>
