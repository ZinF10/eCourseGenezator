import axios from 'axios';

export const BASE_URL = 'http://127.0.0.1:5000/'

const axiosClient = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    timeout: 2500
});

export default axiosClient;
