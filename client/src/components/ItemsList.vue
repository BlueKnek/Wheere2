<template lang="pug">
  div.root
    Header
    div.page
      ItemCard(v-for="{itemId, itemData} in itemsList", :item="itemData", :key="itemId")
</template>

<script>
import Header from './Header'
import ItemCard from './ItemCard'
import { mapGetters } from 'vuex'

export default {
  components: {
    Header,
    ItemCard,
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
</style>
