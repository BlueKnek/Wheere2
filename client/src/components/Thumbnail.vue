<template>
  <img v-if="url" :src="url"/>
</template>

<script>
import noImg from '@/assets/no-img.png'

export default {
  props: ['image'],
  computed: {
    url () {
      if ((!this.image.url) && (!this.image.filename)) {
        return noImg
      }
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
