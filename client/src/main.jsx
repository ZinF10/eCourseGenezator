import { StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/index.css'
import App from './App'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Suspense fallback={<span>Loading...</span>}>
      <App />
    </Suspense>
  </StrictMode>,
)
