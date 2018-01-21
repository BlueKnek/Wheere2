<template>
  <div>
    <Header/>
    <div class="content">
      <input v-model="name" @input="updatedModel"/> <br/>
      <TagsInput v-model="tags" @input="updatedModel"/>
      <MarkdownInput v-model="description" @input="updatedModel"/>
      <span>{{status}}</span>
      <Thumbnail v-for="filename in images" :filename="filename" :key="filename"/>

      <h2>Upload images</h2>
      <ImageUploader @uploaded="addImage"/>

      <h2 v-if="status === 'downloading'">Downloading ...</h2>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

import Header from './Header'
import ImageUploader from './ImageUploader'
import Thumbnail from './Thumbnail'
import TagsInput from './TagsInput'
import MarkdownInput from './MarkdownInput'

export default {
  components: {
    Header,
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
        this.images = j.images
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
      this.images.push(image.filename)
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
  .content {
    max-width: 50em;
    margin: auto;
    background-color: var(--background-color);
    padding: 1rem;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
  }
</style>
