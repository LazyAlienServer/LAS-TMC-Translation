import api from './axiosInstance'

function fetchSnapshot(snapshot) {
    return api.get('/pages/youtube_channel_snapshot', snapshot)
}

export {
    fetchSnapshot,
}
