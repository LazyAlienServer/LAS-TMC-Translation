import Cookies from "js-cookie";

const isProd = window.location.protocol === "https:";

function setRefreshToken(token, expiresDays = 30) {
    Cookies.set("refreshToken", token, {
        expires: expiresDays,
        secure: isProd,
        sameSite: "strict",
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
