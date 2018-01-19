<template>
  <div class="root">
    <h1>Wheere2</h1>
    <router-link to="/AddItem">Add item</router-link>
    <div>{{data}}</div>
  </div>
</template>

<script>
export default {
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
