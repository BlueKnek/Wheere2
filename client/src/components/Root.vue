<template>
  <div class="root">
    <h1>Wheere2</h1>
    <router-link to="/new-item">New item</router-link>
    <ItemCard v-for="item in data.items" :item="item" :key="item.item_id"/>
    <div>{{data}}</div>
  </div>
</template>

<script>
import ItemCard from './ItemCard'

export default {
  components: {
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
