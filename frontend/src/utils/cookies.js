import Cookies from "js-cookie";


function setRefreshToken(token, expiresDays = 30) {
    Cookies.set("refreshToken", token, {
        expires: expiresDays,
        secure: true,
    });
}

function getRefreshToken() {
    return Cookies.get('refreshToken');
}

function removeRefreshToken() {
    Cookies.remove('refreshToken');
}

export {
    setRefreshToken,
    getRefreshToken,
    removeRefreshToken,
};
