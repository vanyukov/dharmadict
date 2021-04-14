<template>
  <h1>page</h1>
</template>

<script>
export default {
  async asyncData({ params, $api }) {
    console.log(params.id)
    const post = await $api('v1', `page/${params.id}`)
    return { post }
  },
}
</script>
