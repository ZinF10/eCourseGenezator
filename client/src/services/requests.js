import axiosClient, { BASE_URL } from "./axiosClient";


export const fetchAPIs = async ({ queryKey }) => {
    const [url, page] = queryKey;
    let apiUrl = `${BASE_URL}${url}/?`
    if (page) apiUrl += `page=${page}`;
    const response = await axiosClient.get(`${apiUrl}`)
    return response.data.results || response.data;
}