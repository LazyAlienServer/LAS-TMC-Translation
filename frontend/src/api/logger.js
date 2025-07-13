import api from './axiosInstance'

function sendLogToServer(logEntry) {
    return api.post('/pages/log_collect/', logEntry)
}

export {
    sendLogToServer,
}
