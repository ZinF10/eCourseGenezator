import { BrowserRouter, Route, Routes } from "react-router-dom";
import { PublicRoutes } from "./routes/routes";
import RootLayout from "./components/layouts/RootLayout";
import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'

const queryClient = new QueryClient()

const publicRoutes = PublicRoutes.map((route) => {
  const Page = route.component;
  return (
    <Route
      key={route}
      path={route.path}
      element={<Page />}
    />
  );
})

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route element={<RootLayout />}>
            {publicRoutes}
          </Route>
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App