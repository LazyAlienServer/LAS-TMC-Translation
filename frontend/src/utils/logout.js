import { useUserStore } from "@/stores";


function handleLogout() {
    const userStore = useUserStore();
    userStore.logout();
}

export {
    handleLogout,
}
