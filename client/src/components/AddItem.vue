<template>
  <div class="root">
    <h1>Add item</h1>
    <input v-model="name"/> <br/>
    <textarea v-model="description"/> <br/>
    <input @change="addImageFiles($event.target.files)" type="file" accept="image/*" capture="camera"/> <br/>
    <button @click="addItem()">Add item</button> <br/>
    <span>{{status}}</span>

    <h2>Images</h2>
    <div v-for="image in images" :key="image.name">
      <img v-if="image.dataUrl" :src="image.dataUrl"/>
      {{image.status}}
    </div>
  </div>
</template>

<script>
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
    addImageFiles (files) {
      for (let index = 0; index < files.length; index++) {
        this.addImageFile(files[index])
      }
    },
    addImageFile (file) {
      let image = {
        file: file,
        dataUrl: false,
        status: 'uploading',
      }

      blobToDataUrl(file)
        .then(dataUrl => { image.dataUrl = dataUrl })

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
img {
  max-width: 100%;
}
</style>
