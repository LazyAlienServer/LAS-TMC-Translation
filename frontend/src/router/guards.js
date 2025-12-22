import { useUserStore, useArticleStore } from "@/stores";


let hasInitialized = false;

async function globalBeforeEach(to) {
    const userStore = useUserStore();
    const articleStore = useArticleStore();

    if (!hasInitialized) {
        await userStore.initializeUser();
        hasInitialized = true;
    }

    const isLoggedIn = userStore.isLoggedIn;

    if (to.meta.requiresAuth && !isLoggedIn) {
        return { name: 'login' };
    }

    if ((to.name === "login" || to.name === "register") && isLoggedIn) {
        return { name: 'home' };
    }

    if (to.meta.title) {
        document.title = to.meta.title;
    }

    if (to.name === 'article-editor' && to.params.id) {
        articleStore.switchArticle(to.params.id)
    }
}


export {
    globalBeforeEach,
}
