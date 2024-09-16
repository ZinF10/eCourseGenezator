import axiosClient, { BASE_URL } from "./axiosClient";

export const fetchAPIs = async ({ queryKey }) => {
    const response = await axiosClient.get(`${BASE_URL}${queryKey}`)
    return response.data.results || response.data;
}