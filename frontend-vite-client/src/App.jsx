import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router'

// Components
import Login from './components/pages/Login/Login'
import Preview from './components/pages/Preview/Preview'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Router>
        <Routes>

          {/* для не авторизированных пользователей */}
          <Route path="/login" element={<Login />} />
          <Route path="/registration" element={<Login isRegistration={true} />} />
          <Route path="/preview" element={<Preview />} />
          


          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
    </>

  )
}

export default App
