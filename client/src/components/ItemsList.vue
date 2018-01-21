<template lang="pug">
  div.root
    Header
    div.page
      div.filter
        TagsInput
      ItemCard(v-for="{itemId, itemData} in itemsList", :item="itemData", :itemId="itemId" :key="itemId")
</template>

<script>
import Header from './Header'
import ItemCard from './ItemCard'
import TagsInput from './TagsInput'
import { mapGetters } from 'vuex'

export default {
  components: {
    Header,
    ItemCard,
    TagsInput,
  },
  computed: mapGetters([
    'itemsList',
  ]),
}
</script>

<style scoped>
  .page {
    margin: auto;
    max-width: 30rem;
  }

  .filter {
    display: flex;
    flex-direction: column;
    --space: 1rem;
    background-color: var(--background-color);
    margin: var(--space);
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
    padding: 1rem;
  }
</style>
