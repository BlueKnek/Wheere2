import Vue from 'vue'
import Router from 'vue-router'
import Root from '@/components/Root'
import EditItem from '@/components/EditItem'
import NewItem from '@/components/MarkdownInput'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Root',
      component: Root,
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
    {
      path: '/test',
      name: 'MarkdownInput',
      component: NewItem,
    },
  ],
})
