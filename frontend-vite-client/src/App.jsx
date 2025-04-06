import { useState, useContext } from 'react'
import { BrowserRouter as Router, Route, Routes, Navigate, Outlet } from 'react-router'


// Providers
import { AuthProvider } from './context/AuthContext'

// Contexts

import { AuthContext } from './context/AuthContext'

// Components
import Login from './components/pages/Login/Login'
import Preview from './components/pages/Preview/Preview'
import Main from './components/pages/Main/Main'
import Applications from './components/layout/Applications/Applications'
import MainAside from './components/layout/MainAside/MainAside'


export default function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <AuthProvider>
        <Router>
          <Routes>

            {/* для не авторизированных пользователей */}
            <Route path="/login" element={<Login />} />
            <Route path="/registration" element={<Login isRegistration={true} />} />
            <Route path="/preview" element={<Preview />} />

            {/* защищенные роуты */}
            <Route path="/user" element={<ProtectedRoutes/>}> 
              <Route index element={<Applications/>}/>
            </Route>


            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Router>
      </AuthProvider>
    </>

  )
}


function ProtectedRoutes(){
  const {getAuthLS} = useContext(AuthContext);

  return(
    <>
      {getAuthLS() ? <>
        <MainAside />
        <main className="content main">
          <Outlet/>
        </main>
      </> : <Navigate to="/login" />}
    
    </>
  )
}

