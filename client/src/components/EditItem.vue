<template lang="pug">
  div
    Header
    div.content
      input(v-model="name", @input="updatedField('name')", placeholder="Item name")
      TagsInput(v-model="tags", @input="updatedField('tags')")
      MarkdownInput(v-model="description", @input="updatedField('description')")
      div.thumbnails
        Thumbnail(v-for="filename in images", :filename="filename", :key="filename")

      h2 Upload images
      ImageUploader(@uploaded="addImage")
</template>

<script>
import Header from './Header'
import ImageUploader from './ImageUploader'
import Thumbnail from './Thumbnail'
import TagsInput from './TagsInput'
import MarkdownInput from './MarkdownInput'

import {socket} from '../main'

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
      tags: [],
      images: [],
    }
  },
  mounted () {
    fetch('/api/item/' + this.item_id + '.json')
      .then(r => r.json())
      .then(j => {
        this.name = j.name
        this.tags = j.tags
        this.description = j.description
        this.images = j.images
      })
  },
  methods: {
    updatedField (name) {
      socket.emit('update', {
        tableName: 'items',
        id: this.item_id,
        data: {[name]: this[name]}},
      )
    },
    addImage (image) {
      this.images.push(image.filename)
      this.updatedField('images')
    },
  },
}
</script>

<style scoped>
  .content {
    display: flex;
    flex-direction: column;
    max-width: 50em;
    margin: auto;
    background-color: var(--background-color);
    padding: 1rem;
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
  }

  .content > * {
    margin: 0.25rem;
  }

  .content input {
    font-size: 1.5rem;

    border: var(--input-border);
    padding: var(--input-padding);

    transition: 0.2s all;
  }

  .content input:hover, .content input:focus {
    border-color: var(--color-active);
  }

</style>
