<template lang="pug">
  div.MarkdownInput
    div(ref="editor")
</template>

<script>
import Editor from 'tui-editor'

export default {
  props: ['value'],
  mounted () {
    this.editor = new Editor({
      initialEditType: 'wysiwyg',
      previewStyle: 'vertical',
      initialValue: this.value,
      el: this.$refs.editor,
      events: {
        change: () => {
          let newVal = this.editor.getMarkdown()
          if (this.value !== newVal) {
            this.$emit('input', newVal)
          }
        },
      },
    })
  },
  watch: {
    value (newVal, oldVal) {
      let currentMarkdown = this.editor.getMarkdown()
      if (newVal !== currentMarkdown) {
        this.editor.setMarkdown(newVal, false)
      }
    },
  },
}
</script>

<style src="tui-editor/dist/tui-editor.css"></style>
<style src="tui-editor/dist/tui-editor-contents.css"></style>
<style src="codemirror/lib/codemirror.css"></style>
