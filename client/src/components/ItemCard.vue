<template>
  <div class="ItemCard">
    <Thumbnail :image="{filename: item.images[0]}"/>
    <scope class="name">{{item.name}}</scope>
  </div>
</template>

<script>
import Thumbnail from './Thumbnail'

export default {
  components: {
    Thumbnail,
  },
  props: ['item'],
}
</script>

<style scoped>
  .ItemCard {
    --space: 1rem;
    --space-inside: 0.25rem;
    background-color: var(--background-color);
    display: flex;
    padding: var(--space-inside);
    margin: var(--space);
    border-radius: var(--space-inside);
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.5s;
  }

  .ItemCard:hover {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }

  .ItemCard > * {
    margin: var(--space-inside);
  }

  .name {
    font-size: 2rem;
  }
</style>
