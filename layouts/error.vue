<template>
  <div>
    <div v-if="error.statusCode === 404">
      <h1>Ошибка 404</h1>
      <h2>Страница не найдена</h2>
    </div>
    <h1 v-else>Произошла ошибка</h1>
  </div>
</template>
<script>
export default {
  props: ['error'],
  layout: 'error',
}
</script>
