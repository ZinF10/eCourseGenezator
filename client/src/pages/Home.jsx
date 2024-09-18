import { useLocation } from "react-router-dom";
import useApi from "../hooks/useApi"

const Home = () => {
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const page = queryParams.get('page');
    const { isLoading, data } = useApi('categories')
    const { data: courses } = useApi('courses', page)

    return (
        <section className="mb-2">
            <h3 className="font-bold text-3xl mb-2">Categories</h3>

            {isLoading ? <span>Loading...</span>
                : (!Array.isArray(data) ? <span>No data</span>
                    :
                    <ul className="mb-3">
                        {data?.map(category => (
                            <li key={category.id}>{category.name}</li>
                        ))}
                    </ul>
                )
            }

            <h3 className="font-bold text-3xl mb-2">All Courses</h3>

            {courses?.map(course => (
                <ul key={course.id} className='my-3'>
                    <li className="font-bold">{course.subject}</li>
                    <li className="italic">Price: ${course.price}</li>
                </ul>
            ))}

        </section>
    )
}

export default Home