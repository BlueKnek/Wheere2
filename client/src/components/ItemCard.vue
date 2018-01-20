<template>
  <div class="ItemCard" @click="go">
    <Thumbnail :image="{filename: item.images[0]}"/>
    <span class="name">{{item.name}}</span>
  </div>
</template>

<script>
import Thumbnail from './Thumbnail'

export default {
  components: {
    Thumbnail,
  },
  props: ['item'],
  methods: {
    go () {
      this.$router.push({name: 'EditItem', params: {item_id: this.item.item_id}})
    },
  },
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
    cursor: pointer;
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
