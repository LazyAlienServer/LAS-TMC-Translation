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
        meta: { title: 'Home' },
    },
    {
        path: '/login',
        name: 'login',
        component: views.LoginView,
        meta: { title: 'Login' },
    },
    {
        path: '/logout',
        name: 'logout',
        component: views.LogoutView,
        meta: { title: 'Logout' },
    },
    {
        path: '/register',
        name: 'register',
        component: views.RegisterView,
        meta: { title: 'Register' },
    },
    {
        path: '/profile/:username',
        name: 'profile',
        component: views.ProfileView,
        meta: {
            requiresAuth: true,
            title: 'Profile',
        },
    },
    {
        path: '/cookie-policy',
        name: 'cookie',
        component: views.CookiePolicyView,
        meta: { title: 'Cookie Policy' },
    },
    {
        path: '/profile/settings/appearance',
        name: 'appearance',
        component: views.AppearanceSettingView,
        meta: {
            requiresAuth: true,
            title: 'Appearance',
        },
    },
    {
        path: `/studio/my-articles`,
        name: 'my-articles',
        component: views.MyArticleListView,
        meta: {
            requiresAuth: true,
            title: 'My Articles',
        }
    },
    {
        path: `/pending-articles`,
        name: 'pending-articles',
        component: views.PendingArticleListView,
        meta: {
            requiresAuth: true,
            title: 'Pending Articles',
        }
    },
    {
        path: `/studio/articles/:id/edit/`,
        name: 'article-editor',
        component: views.SourceArticleEditorView,
        meta: {
            requiresAuth: true,
            title: 'Article Editor',
            showPageHeader: true,
        }
    },
    {
        path: `/studio/articles/:id/review/`,
        name: 'article-review',
        component: views.SourceArticleReviewView,
        meta: {
            requiresAuth: true,
            title: 'Article Review',
        }
    },
    {
        path: `/articles/:id/`,
        name: 'article-detail',
        component: views.PublishedArticleDetailView,
        meta: {
            requiresAuth: true,
            title: 'Article Detail',
        }
    },
    {
        path: `/articles/`,
        name: 'article-list',
        component: views.PublishedArticleListView,
        meta: {
            requiresAuth: true,
            title: 'Article List',
        }
    },
    {
        path: '/:pathMatch(.*)*',
        name: '404',
        component: () => import("@/views/misc/NotFoundView.vue"),
        meta: {title: '404'},
    },
]

export default routes
