const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'Knapsack',
        component: () => import('pages/Knapsack.vue'),
      },
      {
        path: '',
        name: 'ItemsManagement',
        component: () => import('pages/ItemsManagement.vue'),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
