import axios from 'axios'

const api = axios.create({
    baseURL: '/api/v1',
    timeout: 4000,
})

export default api
