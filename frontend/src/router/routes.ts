import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', redirect: '/add' },
      { path: '/add', component: () => import('pages/Add.vue') },
      { path: '/solve', component: () => import('pages/Solve.vue') },
      { path: '/docs', component: () => import('pages/Docs.vue') },
      { path: '/about', component: () => import('pages/About.vue') },
    ],
  },

  // // Always leave this as last one,
  // // but you can also remove it
  // {
  //   path: '/:catchAll(.*)*',
  //   component: () => import('pages/ErrorNotFound.vue'),
  // },
];

export default routes;
