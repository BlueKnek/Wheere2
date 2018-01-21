// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'

Vue.config.productionTip = false

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    itemsList: [],
  },
  mutations: {
    setItemsList: (state, {itemsList}) => {
      state.itemsList = itemsList
    },
  },
  getters: {
    itemsList: state => {
      return state.itemsList
    },
  },
})

fetch('/api/items.json')
  .then(r => r.json())
  .then(j => {
    store.commit('setItemsList', j)
  })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
})
