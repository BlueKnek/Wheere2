// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import io from 'socket.io-client'
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
    updateItem: (state, {id, data}) => {
      let entry = state.itemsList.find(entry => entry.id === id)
      if (entry) {
        Object.keys(data).forEach(key => {
          let value = data[key]
          entry.data[key] = value
        })
      } else {
        state.itemsList.push({id, data})
      }
    },
  },
  getters: {
    itemsList: state => {
      return state.itemsList
        .map(
          ({id, data}) => ({itemId: id, itemData: data})
        )
    },
  },
})

let socket = io()

socket.on('connect', () => {
  socket.emit('listen', {tableName: 'items'})
  socket.emit('list', {tableName: 'items'}, list => {
    let itemsList = list.filter(({data}) => data.filled)
    store.commit('setItemsList', {itemsList})
  })
})

socket.on('update', ({tableName, id, data}) => {
  if (tableName === 'items') {
    store.commit('updateItem', {id, data})
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
})
