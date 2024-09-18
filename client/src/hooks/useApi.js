import { useQuery } from "@tanstack/react-query";
import { fetchAPIs } from "../services/requests";

const useApi = (url, page) => {
    const { isLoading, isError, data = [], error } = useQuery({
        queryKey: [url, page],
        queryFn: fetchAPIs,
    });

    isError && console.error(error.message)

    return { isLoading, data }
}

export default useApi