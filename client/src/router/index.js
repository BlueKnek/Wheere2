import Vue from 'vue'
import Router from 'vue-router'
import ItemsList from '@/components/ItemsList'
import EditItem from '@/components/EditItem'
import NewItem from '@/components/NewItem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ItemsList',
      component: ItemsList,
    },
    {
      path: '/item/:item_id/edit',
      name: 'EditItem',
      component: EditItem,
      props: true,
    },
    {
      path: '/new-item',
      name: 'NewItem',
      component: NewItem,
    },
  ],
})
