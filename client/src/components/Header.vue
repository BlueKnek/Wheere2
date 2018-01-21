<template lang="pug">
  div.Header
    <router-link to="/">Wheere2</router-link>
    <router-link to="/new-item">New item</router-link>
</template>

<script>
export default {
}
</script>

<style>
  .Header {
    font-size: 0;
    position: fixed;
    top: 0;
    width: 100%;
    background-color: var(--background-color);
    z-index: 1;

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
  }

  .Header a {
    font-size: 1.5rem;
    color: var(--color-interactive);
    text-decoration: none;
    padding: 0.5em;
    display: inline-block;
    transition: 0.2s all;
  }

  .Header a:hover {
    background-color: var(--color-active);
    color: var(--background-color);
  }
</style>
