<template lang="pug">
  div.TagsInput
    Tags(:value="value" @click="removeTag")
    input.input(v-model="newTag", @keyup="checkIfEnter")
</template>

<script>
import Tags from './Tags'

export default {
  components: {
    Tags,
  },
  data () {
    return {
      newTag: '',
    }
  },
  props: ['value'],
  methods: {
    changeTo (newValue) {
      console.log('changeTo', newValue)
      this.$emit('input', newValue)
    },
    removeTag (tag) {
      console.log(tag)
      this.changeTo(this.value.filter(v => v !== tag))
    },
    checkIfEnter (event) {
      if (event.keyCode === 13) {
        console.log(this.newTag, [...this.value, this.newTag])
        this.changeTo([...this.value, this.newTag])
        this.newTag = ''
      }
      if (event.keyCode === 8 && event.target.selectionStart === 0) {
        this.removeTag(this.value[this.value.length - 1])
      }
    },
  },
}
</script>

<style scoped>
  .TagsInput {
    display: flex;
    border: 1px solid gray;
  }
  .input {
    flex-grow: 1;
  }
</style>
