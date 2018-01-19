import Vue from 'vue'
import Router from 'vue-router'
import Root from '@/components/Root'
import AddItem from '@/components/AddItem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Root',
      component: Root,
    },
    {
      path: '/AddItem',
      name: 'AddItem',
      component: AddItem,
    },
  ],
})
