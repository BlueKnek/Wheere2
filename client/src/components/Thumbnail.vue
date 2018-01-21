<template>
  <img v-if="url" :src="url"/>
</template>

<script>
import noImg from '@/assets/no-img.png'

export default {
  props: ['image', 'filename'],
  computed: {
    url () {
      if (this.filename) {
        return '/api/img/' + this.filename
      }
      if (this.image && this.image.url) {
        return this.image.url
      }
      return noImg
    },
  },
}
</script>

<style scoped>
img {
  width: 5rem;
  height: 5rem;
  object-fit: cover;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
</style>
