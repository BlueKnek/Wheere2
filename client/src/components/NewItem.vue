<template>
  <h1>Creating new item...</h1>
</template>

<script>

import {socket} from '../main'

const emptyItemData = {
  name: '',
  tags: [],
  description: '',
  images: [],
}

export default {
  mounted () {
    socket.emit('new', {tableName: 'items', data: emptyItemData}, id => {
      this.$router.replace({ name: 'EditItem', params: {item_id: id} })
    })
  },
}
</script>

<style scoped>
</style>
