import api from './axiosInstance'

function fetchSnapshot(snapshot) {
    return api.get('/youtube_channel_snapshot', snapshot)
}

export {
    fetchSnapshot,
}
