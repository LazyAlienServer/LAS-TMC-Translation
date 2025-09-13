import axios from 'axios'
import { useUserStore } from "@/stores/useUserStore";

const api = axios.create({
    baseURL: '/api/v1',
    timeout: 10000,
})

let isRefreshing = false
let refreshPromise = null
const subscribers = []

function onRefreshed(newToken) {
    subscribers.forEach(callback => callback(newToken))
    subscribers.length = 0;
}

function addSubscriber(callback) {
    subscribers.push(callback)
}

api.interceptors.request.use((config) => {
    const userStore = useUserStore();

    // If there is an accessToken available but the caller forgets to set it
    if (userStore.accessToken && !(config.headers && config.headers.authorization)) {
        config.headers = {...(config.headers || {}), Authorization: `Bearer ${userStore.accessToken}` };
    }

    return config;
})

api.interceptors.response.use(
    function (response) {
        return response;
    },
    async function (error) {
        const userStore = useUserStore();
        const originalRequest = error.config || {};
        const status = error?.response?.status

        // Only enter the refresh logic when the status is 401
        if (status !== 401) {
            return Promise.reject(error);
        }

        if ( !userStore.refreshToken || originalRequest._retry) {
            userStore.logout();
            return Promise.reject(error);
        }
        originalRequest._retry = true;

        // If a refresh process exists, put the new refresh request in the waiting queue
        if (isRefreshing && refreshPromise) {
            return new Promise((resolve, reject) => {
                // Add a callback function into the subscriber list
                addSubscriber((newToken) => {
                    try {
                        // Use the updated token to retry the request
                        originalRequest.headers = { ...(originalRequest.headers || {}), Authorization: `Bearer ${newToken}` }
                        resolve(api(originalRequest))

                    } catch (error) {
                        reject(error)
                    }
                })
            })
        }

        // The part that triggers a refresh process
        try {
            isRefreshing = true

            //  Use the bare refresh function (only use axios)
            refreshPromise = userStore.refreshAccessTokenBare()
            await refreshPromise

            const newToken = userStore.accessToken
            onRefreshed(newToken)

            // retry the request
            originalRequest.headers = { ...(originalRequest.headers || {}), Authorization: `Bearer ${newToken}` }
            return api(originalRequest)

        } catch (refreshErr) {
            // If the refresh fails
            userStore.logout()
            return Promise.reject(refreshErr)

        } finally {
            isRefreshing = false
            refreshPromise = null
        }

        return Promise.reject(error);
    }
);

export default api
