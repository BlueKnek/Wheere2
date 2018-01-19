<template>
  <div class="root">
    <h1>Add item</h1>
    <input v-model="name"/> <br/>
    <textarea v-model="description"/> <br/>
    <button @click="addItem()">Add item</button> <br/>
    <span>{{status}}</span>

    <h2>Upload images</h2>
    <ImageUploader @uploaded="addImage"/>
  </div>
</template>

<script>
import ImageUploader from './ImageUploader'

export default {
  components: {
    ImageUploader,
  },
  data () {
    return {
      name: '',
      description: '',
      status: 'idle',
      images: [],
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
    addImage (image) {
      console.log(image)
    },
  },
}
</script>

<style scoped>
</style>
