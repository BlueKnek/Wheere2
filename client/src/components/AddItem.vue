<template>
  <div class="root">
    <h1>Add item</h1>
    <input v-model="name"/> <br/>
    <textarea v-model="description"/> <br/>
    <button @click="addItem()">Add item</button> <br/>
    <span>{{status}}</span>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: '',
      description: '',
      status: 'idle',
    }
  },
  methods: {
    addItem () {
      this.status = 'sending'

      let formData = new FormData()
      formData.append('name', this.name)
      formData.append('description', this.description)
      fetch('/api/add-item', {
        method: 'POST',
        body: formData,
      })
        .then(r => { this.status = 'done' })
        .catch(r => { this.status = 'fail' })
    },
  },
}
</script>

<style scoped>
</style>
