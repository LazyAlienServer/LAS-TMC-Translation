import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Contact from "@/views/Contact.vue";
import Donate from "@/views/Donate.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Profile from "@/views/Profile.vue";
import Videos from "@/views/Videos.vue"
import { useUserStore } from "@/stores/useUserStore";


let hasInitialized = false;

router.beforeEach(async (to, _from) => {
    const userStore = useUserStore();

    if (!hasInitialized) {
        await userStore.initializeUser();
        hasInitialized = true;
    }

    const isLoggedIn = userStore.isLoggedIn;

    if (to.meta?.requiresAuth && !isLoggedIn) {
        return { name: 'login' };
    }

    if (to.name === "login" || to.name === "register") {
        return { name: 'home' };
    }
})

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
    },
    {
        path: '/contact-us',
        name: 'contact',
        component: Contact,
    },
    {
        path: '/donate',
        name: 'donate',
        component: Donate,
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
    {
        path: '/profile/:username',
        name: 'profile',
        component: Profile,
        meta: { requiresAuth: true },
    },
    {
        path: '/videos',
        name: 'videos',
        component: Videos,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
