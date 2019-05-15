import Vue from 'vue'
import Router from 'vue-router'
import homepage from '@/components/homepage/homepage'
import ctx from '@/components/homepage/context'
import Menu from '@/components/homepage/Menu'
import Login from '@/components/loginpage/Login'
import details from '@/components/homepage/details/details'
Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path:'/',
    //   redirect:'/login'//自动跳转/login
    // },
    {
      path:'/details',
      name:'details',
      component:details
    },
    {
      path:'/programm',
      name:'programm',
      component:ctx
    },
    {
      path:'/live',
      name:'live',
      component:ctx
    },
    {
      path:'/Menu',
      name:'Menu',
      component:Menu
    },
    {
      path:'/login',
      name:'Login',
      component:Login
    },
    {
      path:'/homepage',
      name:'homepage',
      component:homepage
    },
 
  ]
})
