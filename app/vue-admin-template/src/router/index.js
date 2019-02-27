import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if false, the item will hidden in breadcrumb(default is true)
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    // hidden: true,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '仪表盘', icon: 'dashboard' }
    }]
  },

  {
    path: '/asset',
    component: Layout,
    redirect: '/asset',
    name: 'Asset',
    meta: { title: '资产管理', icon: 'example' },
    children: [
      {
        path: 'network',
        name: 'Network',
        component: () => import('@/views/asset/network/index'),
        meta: { title: '网络设备', icon: 'tree' }
      },
      {
        path: 'physical',
        name: 'Physical',
        component: () => import('@/views/asset/physical/index'),
        meta: { title: '物理机', icon: 'tree' }
      },
      {
        path: 'virtual',
        name: 'Virtual',
        component: () => import('@/views/asset/virtual/index'),
        meta: { title: '虚拟机', icon: 'tree' }
      },
      {
        path: 'storage',
        name: 'Storage',
        component: () => import('@/views/asset/storage/index'),
        meta: { title: '存储设备', icon: 'tree' }
      },
      {
        path: 'room',
        name: 'Room',
        component: () => import('@/views/asset/room/index'),
        meta: { title: '机房', icon: 'tree' }
      }
    ]
  },

  {
    path: '/business',
    component: Layout,
    redirect: '/business',
    name: 'Business',
    meta: { title: '业务管理', icon: 'example' },
    children: [
      {
        path: 'application',
        name: 'Application',
        component: () => import('@/views/business/application/index'),
        meta: { title: '应用', icon: 'form' }
      },
      {
        path: 'service',
        name: 'Service',
        component: () => import('@/views/business/service/index'),
        meta: { title: '服务', icon: 'form' }
      },
      {
        path: 'web',
        name: 'Web',
        component: () => import('@/views/business/web/index'),
        meta: { title: 'Web', icon: 'form' }
      },
      {
        path: 'database',
        name: 'Database',
        component: () => import('@/views/business/database/index'),
        meta: { title: '数据库', icon: 'form' }
      },
      {
        path: 'workstation',
        name: 'Workstation',
        component: () => import('@/views/business/workstation/index'),
        meta: { title: '工作站', icon: 'form' }
      }
    ]
  },

  {
    path: '/nested',
    component: Layout,
    redirect: '/nested/menu1',
    name: 'Nested',
    meta: {
      title: 'Nested',
      icon: 'nested'
    },
    children: [
      {
        path: 'menu1',
        component: () => import('@/views/nested/menu1/index'), // Parent router-view
        name: 'Menu1',
        meta: { title: 'Menu1' },
        children: [
          {
            path: 'menu1-1',
            component: () => import('@/views/nested/menu1/menu1-1'),
            name: 'Menu1-1',
            meta: { title: 'Menu1-1' }
          },
          {
            path: 'menu1-2',
            component: () => import('@/views/nested/menu1/menu1-2'),
            name: 'Menu1-2',
            meta: { title: 'Menu1-2' },
            children: [
              {
                path: 'menu1-2-1',
                component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
                name: 'Menu1-2-1',
                meta: { title: 'Menu1-2-1' }
              },
              {
                path: 'menu1-2-2',
                component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
                name: 'Menu1-2-2',
                meta: { title: 'Menu1-2-2' }
              }
            ]
          },
          {
            path: 'menu1-3',
            component: () => import('@/views/nested/menu1/menu1-3'),
            name: 'Menu1-3',
            meta: { title: 'Menu1-3' }
          }
        ]
      },
      {
        path: 'menu2',
        component: () => import('@/views/nested/menu2/index'),
        meta: { title: 'menu2' }
      }
    ]
  },

  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
        meta: { title: 'External Link', icon: 'link' }
      }
    ]
  },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // 后端支持可开
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
