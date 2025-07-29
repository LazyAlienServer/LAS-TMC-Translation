import { useUserStore } from "@/stores/useUserStore";


let hasInitialized = false;

async function globalBeforeEach(to) {
    const userStore = useUserStore();

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
}


export {
    globalBeforeEach,
}
