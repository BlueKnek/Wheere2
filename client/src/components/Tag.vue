<template lang="pug">
  span.Tag {{value}}
</template>

<script>
export default {
  props: ['value'],
}
</script>

<style scoped>
  .Tag {
    background-color: #CCC;
    font-size: 0.75rem;
    padding: 0.125rem 0.3rem;
    margin: 0.125rem;
  }
</style>
