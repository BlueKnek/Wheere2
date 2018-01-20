<template lang="pug">
  div.TagsInput
    span.tags
      span.tag(v-for="tag in value", @click="removeTag(tag)") {{tag}}
    input.input(v-model="newTag", @keyup="checkIfEnter")
</template>

<script>
export default {
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
      this.changeTo(this.value.filter(v => v !== tag))
    },
    checkIfEnter (event) {
      if (event.keyCode === 13) {
        console.log(this.newTag, [...this.value, this.newTag])
        this.changeTo([...this.value, this.newTag])
        this.newTag = ''
      }
      if (event.keyCode === 8 && event.target.selectionStart === 0) {
        this.removeTag(this.value[this.value.length-1])
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
  .tag {
    display: inline-block;
    background-color: #EEE;
    font-size: 0.75rem;
    margin: 0.25rem;
    padding: 0.25rem;
    border-radius: 0.25rem;
  }
  .input {
    flex-grow: 1;
  }
</style>
