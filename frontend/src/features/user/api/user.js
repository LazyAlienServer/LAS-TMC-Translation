import { api, apiBare } from '@/api'

function registerUser(email, password, confirmPassword) {
    return apiBare.post('/user/register/', {
        email: email,
        password: password,
        confirm_password: confirmPassword
    });
}

function loginUser(email, password) {
    return apiBare.post('/user/login/', {
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
    return api.get(
        '/user/profile/',
        { withCredentials: true },
    );
}

function refreshUserLoginToken(refreshToken) {
    return apiBare.post(
        '/user/refresh_login_token/',
        { refresh: refreshToken });
}

export {
    registerUser,
    loginUser,
    uploadAvatar,
    updateUsername,
    getUserProfile,
    refreshUserLoginToken,
}
