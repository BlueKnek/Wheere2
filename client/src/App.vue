<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Roboto');

  body {
    font-family: 'Roboto', sans-serif;
    background-color: #EEE;
    --background-color: #FFF;
    --color-interactive: rgb(42, 60, 138);
    --color-active: rgb(78, 108, 241);
    --input-border: 1px solid var(--input-border-color);
    --input-padding: 0.125rem;
    --input-border-color: #e5e5e5;
    margin: 0;
    padding-top: 5rem;
  }

  textarea, input { outline: none; }
</style>
