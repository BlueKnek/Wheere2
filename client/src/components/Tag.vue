<template lang="pug">
  span.Tag(:style="style", @click="click") {{value}}
</template>

<script>
import ColorHash from 'color-hash'
let colorHash = new ColorHash()

export default {
  props: ['value'],
  computed: {
    style () {
      let hsl = colorHash.hsl(this.value)
      return `background-color: hsl(${hsl[0]}, ${hsl[1] * 100}%, 90%);`
    },
  },
  methods: {
    click () {
      this.$emit('click')
    },
  },
}
</script>

<style scoped>
  .Tag {
    display: inline-block;
    background-color: #CCC;
    font-size: 0.75rem;
    padding: 0.125rem 0.3rem;
    margin: 0.125rem;
  }
</style>
