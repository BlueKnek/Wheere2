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
      let keys = Object.keys(data)
      let redo = keys.some(key =>
        (entry.data[key] === undefined) &&
        (data[key] !== undefined)
      )

      if (redo) {
        entry.data = {
          ...entry.data,
          ...data,
        }
      } else {
        keys.forEach(key => {
          let value = data[key]
          entry.data[key] = value
        })
      }
    },
    newItem: (state, {id, data}) => {
      state.itemsList.push({id, data})
    },
  },
  getters: {
    itemsList: state => {
      return state.itemsList
        .map(
          ({id, data}) => ({itemId: id, itemData: data})
        )
    },
    item: state => id => {
      return state.find(item => item.id === id)
    },
  },
})

export let socket = io()

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

socket.on('new', ({tableName, id, data}) => {
  if (tableName === 'items') {
    store.commit('newItem', {id, data})
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
