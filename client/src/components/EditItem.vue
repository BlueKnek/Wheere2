<template>
  <div class="root">
    <h1>Edit item</h1>
    <input v-model="name"/> <br/>
    <TagsInput v-model="tags"/>
    <textarea v-model="description"/> <br/>
    <button @click="addItem()">Update item</button> <br/>
    <span>{{status}}</span>
    <Thumbnail v-for="image in images" :image="image" :key="image.filename"/>

    <h2>Upload images</h2>
    <ImageUploader @uploaded="addImage"/>

    <h2 v-if="status === 'downloading'">Downloading ...</h2>
  </div>
</template>

<script>
import ImageUploader from './ImageUploader'
import Thumbnail from './Thumbnail'
import TagsInput from './TagsInput'

export default {
  components: {
    ImageUploader,
    Thumbnail,
    TagsInput,
  },
  props: ['item_id'],
  data () {
    return {
      name: '',
      description: '',
      status: 'downloading',
      tags: [],
      images: [],
    }
  },
  mounted () {
    fetch('/api/item/' + this.item_id + '.json')
      .then(r => r.json())
      .then(j => {
        console.log(j)
        this.name = j.name
        this.tags = j.tags
        this.description = j.description
        this.images = j.images.map(i => ({
          filename: i,
        }))
        this.status = 'downloaded'
      })
  },
  methods: {
    addItem () {
      this.status = 'sending'

      fetch('/api/item/' + this.item_id + '/update', {
        headers: {
          'Content-Type': 'application/json',
        },
        method: 'POST',
        body: JSON.stringify({
          name: this.name,
          tags: this.tags,
          description: this.description,
          images: this.images.map(i => i.filename),
        }),
      })
        .then(r => { this.status = 'done' })
        .catch(r => { this.status = 'fail' })
    },
    addImage (image) {
      this.images.push(image)
    },
  },
}
</script>

<style scoped>
</style>
