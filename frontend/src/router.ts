import { createRouter, createWebHashHistory } from 'vue-router'

const Home = () => import('./pages/Home.vue')
const Single = () => import('./pages/Single.vue')

const routes = [
    { path: '/', name:'home', component: Home },
    { path: '/product/:id', name: 'single', component: Single },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHashHistory(),
    routes
})

export default router;