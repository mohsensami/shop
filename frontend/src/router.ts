import { createRouter, createWebHashHistory } from 'vue-router'

const Home = () => import('./pages/Home.vue')
const Single = () => import('./pages/Single.vue')
const Cart = () => import('./pages/Cart.vue')

const routes = [
    { 
        path: '/',
        name: 'home',
        component: Home 
    },

    { 
        path: '/products/:id',
        name: 'single',
        component: Single 
    },

    { 
        path: '/cart/:id',
        name: 'cart',
        component: Cart 
    },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;