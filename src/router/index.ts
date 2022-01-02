import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import CreateAccount from '@/components/CreateAccount.vue'
import Login from '@/components/Login.vue'
import HelloWorld from '@/components/HelloWorld.vue'


const routes = [
    {
        path: '/',
        name: "Home",
        component: Home,
        children: [
            {
                path: '/new',
                name: "CreateAccountForm",
                component: CreateAccount
            },
            {
                path: '/',
                name: "Login",
                component: Login
            },
        ]
    },
    {
        path: '/hello-world', //to delete on production
        name: "HelloWorld",
        component: HelloWorld,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !localStorage.token) next({
        path: '/'
    })
    else next()
})


export default router