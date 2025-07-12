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
    },
    {
        path: '/contact-us',
        name: 'contact',
        component: views.ContactView,
    },
    {
        path: '/donate',
        name: 'donate',
        component: views.DonateView,
    },
    {
        path: '/login',
        name: 'login',
        component: views.LoginView,
    },
    {
        path: '/register',
        name: 'register',
        component: views.RegisterView,
    },
    {
        path: '/profile',
        name: 'profile',
        component: views.ProfileView,
        meta: { requiresAuth: true },
    },
    {
        path: '/videos',
        name: 'videos',
        component: views.VideosView,
    },
    {
        path: '/cookie-policy',
        name: 'cookie',
        component: views.CookiePolicyView,
    },
]

export default routes
