<template>
  <div class="root">
    <h1>Edit item</h1>
    <input v-model="name" @input="updatedModel"/> <br/>
    <TagsInput v-model="tags" @input="updatedModel"/>
    <MarkdownInput v-model="description" @input="updatedModel"/>
    <span>{{status}}</span>
    <Thumbnail v-for="image in images" :image="image" :key="image.filename"/>

    <h2>Upload images</h2>
    <ImageUploader @uploaded="addImage"/>

    <h2 v-if="status === 'downloading'">Downloading ...</h2>
  </div>
</template>

<script>
import _ from 'lodash'

import ImageUploader from './ImageUploader'
import Thumbnail from './Thumbnail'
import TagsInput from './TagsInput'
import MarkdownInput from './MarkdownInput'

export default {
  components: {
    ImageUploader,
    Thumbnail,
    TagsInput,
    MarkdownInput,
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
    updateItem () {
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
    debouncedUpdateItem: _.debounce(function () {
      this.updateItem()
    }, 500),
    addImage (image) {
      this.images.push(image)
      this.updatedModel()
    },
    updatedModel () {
      this.status = 'updated'
      this.debouncedUpdateItem()
    },
  },
}
</script>

<style scoped>
</style>
