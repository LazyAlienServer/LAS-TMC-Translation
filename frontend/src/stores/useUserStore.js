import { defineStore } from 'pinia';
import { ref } from 'vue';
import {
    loginUser,
    getUserProfile,
    refreshUserLoginToken,
    api,
} from "@/api";
import {
    setRefreshToken,
    getRefreshToken,
    removeRefreshToken,
} from "@/utils";


const useUserStore = defineStore('user', () => {
    /* states */
    const accessToken = ref(localStorage.getItem("accessToken"));
    const refreshToken = ref(getRefreshToken());
    const userInfo = ref(null);
    const isLoggedIn = ref(!!accessToken.value);


    /* Tools */
    let refreshTimer = null;

    function scheduleTokenRefresh(expiresInSeconds) {
        clearTimeout(refreshTimer);
        const refreshDelay = (expiresInSeconds - 60) * 1000;

        refreshTimer = setTimeout(() => {
            refreshAccessToken().catch((error) => {
                console.warn(error);
            })
        }, refreshDelay);
    }

    function setToken(access, refresh, refresh_token_lifetime) {
        accessToken.value = access;
        refreshToken.value = refresh;

        localStorage.setItem("accessToken", access);
        setRefreshToken(refresh, refresh_token_lifetime);

        api.defaults.headers.common['Authorization'] = 'Bearer ' + access;
    }

    function removeToken() {
        localStorage.removeItem("accessToken");
        removeRefreshToken();

        delete api.defaults.headers.common['Authorization'];
    }


    /* actions */
    async function login(email, password) {
        const response = await loginUser(email, password);

        setToken(response.data.access, response.data.refresh, parseInt(response.data.refresh_token_lifetime));
        isLoggedIn.value = true;
        console.log("logged in")

        try {
            await loadUserInfo();
        } catch (error) {
            console.warn(error);
        }

        scheduleTokenRefresh(parseInt(response.data.access_token_lifetime));
    }

    function logout() {
        clearTimeout(refreshTimer);

        accessToken.value = '';
        refreshToken.value = '';
        userInfo.value = null;
        isLoggedIn.value = false;

        removeToken();
    }

    async function loadUserInfo() {
        if (!accessToken.value) {
            throw new Error('Access token is missing (this should not happen)');
        }

        try {
            const response = await getUserProfile(accessToken.value);
            userInfo.value = response.data;

        } catch (error) {
            console.log("Obtain user info failed: ", error);
            throw error;
        }
    }
    async function refreshAccessToken() {
        const storedRefreshToken = getRefreshToken();

        if (!storedRefreshToken) {
            throw new Error('Refresh token is missing');
        }

        try {
            const response = await refreshUserLoginToken(storedRefreshToken);

            accessToken.value = response.data.access;
            localStorage.setItem("accessToken", accessToken.value);
            api.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken.value;

            isLoggedIn.value = true;

            scheduleTokenRefresh(parseInt(response.data.access_token_lifetime));

        } catch(error) {
            console.log("Refresh access token failed: ", error);
            logout();
        }
    }

    async function initializeUser() {
        if (accessToken.value) {
            api.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken.value;

            try {
                await loadUserInfo();
            } catch (error) {
                console.warn("Access token is invalid, trying to refresh...");
                try {
                    await refreshAccessToken();
                    await loadUserInfo();
                } catch (error) {
                    console.error("Refresh failed, logging out.");
                    logout();
                }
            }
        }
    }

    return {
        accessToken,
        refreshToken,
        userInfo,
        isLoggedIn,
        login,
        logout,
        loadUserInfo,
        refreshAccessToken,
        initializeUser,
    };
});

export { useUserStore };
