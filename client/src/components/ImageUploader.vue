<template>
  <div class="root">
    <input @change="addImageFiles($event.target.files)" type="file" accept="image/*" capture="camera"/> <br/>
    <div v-for="image in images" :key="image.name">
      <Thumbnail :image="image"/>
      {{image.status}}
    </div>
  </div>
</template>

<script>
import Thumbnail from './Thumbnail'

function blobToDataUrl (blob) {
  return new Promise((resolve, reject) => {
    let reader = new FileReader()
    reader.onload = event => {
      let dataUrl = event.target.result
      resolve(dataUrl)
    }
    reader.readAsDataURL(blob)
  })
}

export default {
  components: {
    Thumbnail,
  },
  data () {
    return {
      images: [],
    }
  },
  methods: {
    addImageFiles (files) {
      for (let index = 0; index < files.length; index++) {
        this.addImageFile(files[index])
      }
    },
    addImageFile (file) {
      let image = {
        file: file,
        url: false,
        status: 'uploading',
      }

      blobToDataUrl(file)
        .then(dataUrl => { image.url = dataUrl })

      let formData = new FormData()
      formData.append('image', file, file.name)
      fetch('/api/upload-image', {
        method: 'POST',
        body: formData,
      })
        .then(r => r.json())
        .then(j => {
          if (j.filename) {
            image.filename = j.filename
            image.status = 'success'
            this.$emit('uploaded', image)
          } else {
            throw Error('Image not saved')
          }
        })
        .catch(e => { image.status = 'fail' })
      this.images.push(image)
    },
  },
}
</script>

<style scoped>
</style>
