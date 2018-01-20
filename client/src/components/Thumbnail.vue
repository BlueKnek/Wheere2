<template>
  <div>
    <img v-if="url" :src="url"/>
  </div>
</template>

<script>
export default {
  props: ['image'],
  computed: {
    url () {
      return this.image.url || '/api/img/' + this.image.filename
    },
  },
}
</script>

<style scoped>
img {
  width: 5rem;
  height: 5rem;
  border-radius: 0.5rem;
}
</style>
