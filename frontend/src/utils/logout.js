import { useUserStore } from "@/stores";
import { logger } from "@/utils";


function handleLogout() {
    // Handle Logout Request
    const userStore = useUserStore();

    logger.info("User logout successfully")

    userStore.logout();
}

export {
    handleLogout,
}
