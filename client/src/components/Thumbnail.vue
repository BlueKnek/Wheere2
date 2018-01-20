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
  object-fit: cover;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
</style>
