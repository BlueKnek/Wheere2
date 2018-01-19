<template>
  <h1>Creating new item...</h1>
</template>

<script>
export default {
  mounted () {
    fetch('/api/new-item', { method: 'POST' })
      .then(r => r.json())
      .then(j => { this.$router.replace({ name: 'EditItem', params: {item_id: j.item_id} }) })
  },
}
</script>

<style scoped>
</style>
