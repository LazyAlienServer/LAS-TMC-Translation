import {createRouter, createWebHistory} from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import ContactUsPage from "@/views/ContactUsPage.vue";
import DonatePage from "@/views/DonatePage.vue";
import UserLoginPage from "@/views/UserLoginPage.vue";
import UserRegisterPage from "@/views/UserRegisterPage.vue";
import UserProfilePage from "@/views/UserProfilePage.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/contact-us',
        name: 'contact',
        component: ContactUsPage
    },
    {
        path: '/donate',
        name: 'donate',
        component: DonatePage
    },
    {
        path: '/login',
        name: 'login',
        component: UserLoginPage
    },
    {
        path: '/register',
        name: 'register',
        component: UserRegisterPage
    },
    {
        path: '/profile/:username',
        name: 'profile',
        component: UserProfilePage
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
