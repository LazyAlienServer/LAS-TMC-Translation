import * as views from "@/views";
/*
Import all views in @/views.
Be careful when using this import syntax in other files, as it import everything without explicit names.
*/


const routes = [
    {
        path: '/',
        name: 'home',
        component: views.HomeView,
        meta: {title: 'Home'},
    },
    {
        path: '/contact-us',
        name: 'contact',
        component: views.ContactView,
        meta: {title: 'Contact Us'},
    },
    {
        path: '/donate',
        name: 'donate',
        component: views.DonateView,
        meta: {title: 'Donate'},
    },
    {
        path: '/login',
        name: 'login',
        component: views.LoginView,
        meta: {title: 'Login'},
    },
    {
        path: '/logout',
        name: 'logout',
        component: views.LogoutView,
        meta: {title: 'Logout'},
    },
    {
        path: '/register',
        name: 'register',
        component: views.RegisterView,
        meta: {title: 'Register'},
    },
    {
        path: '/profile',
        name: 'profile',
        component: views.ProfileView,
        meta: {
            requiresAuth: true,
            title: 'Profile',
        },
    },
    {
        path: '/videos',
        name: 'videos',
        component: views.VideosView,
        meta: {title: 'Videos'},
    },
    {
        path: '/cookie-policy',
        name: 'cookie',
        component: views.CookiePolicyView,
        meta: {title: 'Cookie Policy'},
    },
    {
        path: '/settings/appearance',
        name: 'appearance',
        component: views.AppearanceSettingView,
        meta: {
            requiresAuth: true,
            title: 'Appearance',
        },
    },
    {
        path: '/settings/language',
        name: 'language',
        component: views.LanguageSettingView,
        meta: {
            requiresAuth: true,
            title: 'Language',
        },
    },
    {
      path: '/bookmarks',
      name: 'bookmarks',
      component: views.BookmarksView,
      meta: {
          requiresAuth: true,
          title: 'Bookmarks'
      },
    },
    {
        path: '/:pathMatch(.*)*',
        name: '404',
        component: () => import("@/views/NotFoundView.vue"),
        meta: {title: '404'},
    },
]

export default routes
