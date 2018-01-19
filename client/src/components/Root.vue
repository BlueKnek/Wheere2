<template>
  <div class="root">
    <h1>Wheere2</h1>
    {{data}}
  </div>
</template>

<script>
export default {
  data () {
    fetch('/data.json')
      .then(r => r.json())
      .then(j => { this.data = j })
    return {
      data: false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
