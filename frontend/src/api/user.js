import api from './axiosInstance'
import axios from "axios"; // Import axios for bare refresh request (without the custom api wrapper)

function registerUser(email, password, confirmPassword) {
    return api.post('/user/register/', {
        email: email,
        password: password,
        confirm_password: confirmPassword
    });
}

function loginUser(email, password) {
    return api.post('/user/login/', {
        email: email,
        password: password,
    });
}

function uploadAvatar(file) {
    const formData = new FormData();
    formData.append('avatar', file);
    return api.patch('/user/update_avatar/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
}

function updateUsername(name) {
    return api.patch('/user/update_username/', {
        username: name,
    })
}

function getUserProfile() {
    return api.get('/user/profile/', { withCredentials: true });
}

function refreshUserLoginToken(refreshToken) {
    return api.post(
        '/user/refresh_login_token/',
        { refresh: refreshToken });
}

function refreshUserLoginTokenBare(refreshToken) {
    return axios.post(
        '/user/refresh_login_token/',
        { refresh: refreshToken },
        { withCredentials: false },
    );
}

export {
    registerUser,
    loginUser,
    uploadAvatar,
    updateUsername,
    getUserProfile,
    refreshUserLoginToken,
    refreshUserLoginTokenBare,
}
