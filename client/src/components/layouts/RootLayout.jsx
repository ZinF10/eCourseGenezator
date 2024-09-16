import { Outlet } from "react-router-dom"
import Header from "../ui/organisms/Header"

const RootLayout = () => {
    return (
        <div>
            <Header />
            <main className="container mx-auto h-screen">
                <Outlet />
            </main>
        </div>
    )
}

export default RootLayout