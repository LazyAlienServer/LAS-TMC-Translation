import api from './axiosInstance'

function getChannelSnapshot() {
    return api.get('/pages/youtube_channel_snapshot', {})
}

export {
    getChannelSnapshot,
}
