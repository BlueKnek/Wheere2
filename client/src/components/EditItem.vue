<template>
  <div class="root">
    <h1>Add item</h1>
    <input v-model="name"/> <br/>
    <textarea v-model="description"/> <br/>
    <button @click="addItem()">Update item</button> <br/>
    <span>{{status}}</span>

    <h2>Upload images</h2>
    <ImageUploader @uploaded="addImage"/>

    <h2 v-if="status === 'downloading'">Downloading ...</h2>
  </div>
</template>

<script>
import ImageUploader from './ImageUploader'

export default {
  components: {
    ImageUploader,
  },
  props: ['item_id'],
  data () {
    return {
      name: '',
      description: '',
      status: 'downloading',
      images: [],
    }
  },
  mounted () {
    fetch('/api/item/' + this.item_id + '.json')
      .then(r => r.json())
      .then(j => {
        this.name = j.name
        this.description = j.description
        this.status = 'downloaded'
      })
  },
  methods: {
    addItem () {
      this.status = 'sending'

      let formData = new FormData()
      formData.append('name', this.name)
      formData.append('description', this.description)
      fetch('/api/item/' + this.item_id + '/update', {
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
