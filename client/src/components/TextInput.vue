<template lang="pug">
  input(:value="name", @input="input")
</template>

<script>
export default {
  props: ['value'],
  methods: {
    input (event) {
      this.$emit('input', event.target.value)
    }
  }
}
</script>

<style scoped>
  input {
    font-size: 1.5rem;

    border: var(--input-border);
    padding: var(--input-padding);

    transition: 0.2s all;
  }

  input:hover, input:focus {
    border-color: var(--color-active);
  }

</style>