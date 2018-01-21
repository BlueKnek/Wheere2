<template lang="pug">
  div.ItemCard(@click="go")
    Thumbnail(:filename="item.images[0]")
    div.space
    div.ItemCard-info
      span.name {{item.name}}
      Tags(:value="item.tags")
</template>

<script>
import Thumbnail from './Thumbnail'
import Tags from './Tags'

export default {
  components: {
    Thumbnail,
    Tags,
  },
  props: ['item', 'itemId'],
  methods: {
    go () {
      this.$router.push({name: 'EditItem', params: {item_id: this.itemId}})
    },
  },
}
</script>

<style scoped>
  .ItemCard {
    --space: 1rem;
    background-color: var(--background-color);
    display: flex;
    margin: var(--space);
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
    transition: all 0.5s;
    cursor: pointer;
  }

  .ItemCard:hover {
    box-shadow: 0 16px 24px 2px rgba(0, 0, 0, 0.14), 0 6px 30px 5px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.3);
  }

  .ItemCard-info {
    padding: 0.125rem 0.5rem;
    display: flex;
    flex-direction: column;
  }

  .name {
    font-size: 1.5rem;
  }
</style>
