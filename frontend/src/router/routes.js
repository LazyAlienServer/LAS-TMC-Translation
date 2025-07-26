import * as views from "@/views"
/*
Import all views in @/views.
Be careful when using this import syntax in other files, as it import everything without explicit names.
*/


const routes = [
    {
        path: '/',
        name: 'home',
        component: views.HomeView,
        meta: {title: 'Home - LAS'},
    },
    {
        path: '/contact-us',
        name: 'contact',
        component: views.ContactView,
        meta: {title: 'Contact Us - LAS'},
    },
    {
        path: '/donate',
        name: 'donate',
        component: views.DonateView,
        meta: {title: 'Donate - LAS'},
    },
    {
        path: '/login',
        name: 'login',
        component: views.LoginView,
        meta: {title: 'Login - LAS'},
    },
    {
        path: '/register',
        name: 'register',
        component: views.RegisterView,
        meta: {title: 'Register - LAS'},
    },
    {
        path: '/profile',
        name: 'profile',
        component: views.ProfileView,
        meta: {
            requiresAuth: true,
            title: 'Profile - LAS',
        },
    },
    {
        path: '/videos',
        name: 'videos',
        component: views.VideosView,
        meta: {title: 'Videos - LAS'},
    },
    {
        path: '/cookie-policy',
        name: 'cookie',
        component: views.CookiePolicyView,
        meta: {title: 'Cookie Policy - LAS'},
    },
]

export default routes
