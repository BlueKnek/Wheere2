<template>
  <div>
    <img v-if="image.url" :src="image.url"/>
  </div>
</template>

<script>
export default {
  props: ['image'],
}
</script>

<style scoped>
img {
  width: 5rem;
  height: 5rem;
  border-radius: 0.5rem;
}
</style>
