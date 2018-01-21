<template lang="pug">
  div.Tags
    Tag(v-for="tag in value", :value="tag", :key="tag", @click="click(tag)")
</template>

<script>
import Tag from './Tag'

export default {
  components: {
    Tag,
  },
  props: ['value'],
  methods: {
    click (tag) {
      console.log('click', tag)
      this.$emit('click', tag)
    },
  },
}
</script>
