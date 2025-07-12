import axios from 'axios'
import { useUserStore } from "@/stores/useUserStore";

const api = axios.create({
    baseURL: '/api/v1',
    timeout: 10000,
})

api.interceptors.response.use(
    function (response) {
        return response;
    },
    async function (error) {
        const userStore = useUserStore();
        const originalRequest = error.config;

        if (
            error.response?.status === 401 &&
            !originalRequest._retry &&
            userStore.refreshToken
        ) {
            originalRequest._retry = true;

            try {
                await userStore.refreshAccessToken();
                originalRequest.headers['Authorization'] = 'Bearer ' + userStore.accessToken;
                return api(originalRequest);

            } catch (refreshError) {
                console.warn('Auto refresh access token failed');
                userStore.logout();
            }
        }

        return Promise.reject(error);
    }
);

export default api
