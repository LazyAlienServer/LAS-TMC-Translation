import api from './axiosInstance'


function registerUser(email, password) {
    return api.post('/user/register/', {
        email: email,
        password: password,
    });
}

function loginUser(email, password) {
    return api.post('/user/login', {
        email: email,
        password: password,
    });
}

function getUserProfile() {
    return api.get('/user/profile/', {});
}

function refreshUserLoginToken(refreshToken) {
    return api.post('/user/refresh_login_token/', {
        refresh: refreshToken,
    });
}

export {
    registerUser,
    loginUser,
    getUserProfile,
    refreshUserLoginToken,
}
