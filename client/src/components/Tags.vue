<template lang="pug">
  div.Tags
    Tag(v-for="tag in value", :value="tag", :key="tag")
</template>

<script>
import Tag from './Tag'

export default {
  components: {
    Tag,
  },
  props: ['value'],
}
</script>
