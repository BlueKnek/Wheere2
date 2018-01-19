import Vue from 'vue'
import Root from '@/components/Root'

describe('Root.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Root)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.root h1').textContent)
      .toEqual('Wheere2')
  })
})
