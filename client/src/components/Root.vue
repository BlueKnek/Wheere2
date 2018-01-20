<template>
  <div class="root">
    <Header/>
    <div class="page">
      <ItemCard v-for="item in data.items" :item="item" :key="item.item_id"/>
    </div>
  </div>
</template>

<script>
import Header from './Header'
import ItemCard from './ItemCard'

export default {
  components: {
    Header,
    ItemCard,
  },
  data () {
    fetch('/api/data.json')
      .then(r => r.json())
      .then(j => { this.data = j })
    return {
      data: false,
    }
  },
}
</script>

<style scoped>
  .page {
    margin: auto;
    max-width: 30rem;
  }
</style>
