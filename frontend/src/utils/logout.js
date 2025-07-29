import { useUserStore } from "@/stores";
import { logger } from "@/utils";
import { useRouter } from "vue-router";


function handleLogout() {
    // Handle Logout Request
    const userStore = useUserStore();
    const router = useRouter();

    logger.info("User logout successfully")

    userStore.logout();

    router.push({ name: 'home' });
}

export {
    handleLogout,
}
