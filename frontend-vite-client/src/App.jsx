import { useState, useContext } from 'react'
import { BrowserRouter as Router, Route, Routes, Navigate, Outlet } from 'react-router'


// Providers
import { AuthProvider } from './context/AuthContext'

// Contexts

import { AuthContext } from './context/AuthContext'

// Components
import Login from './components/pages/Login/Login'
import Preview from './components/pages/Preview/Preview'
import Applications from './components/layout/Applications/Applications'
import MainAside from './components/layout/MainAside/MainAside'
import StartApp from './components/layout/StartApp/StartApp'


export default function App() {
  return (
    <>
      <AuthProvider>
        <Router>
          <Routes>

            {/* для не авторизированных пользователей */}
            <Route path="/login" element={<Login />} />
            <Route path="/registration" element={<Login isRegistration={true} />} />
            <Route path="/preview" element={<Preview />} />
            <Route path="/" element={<Navigate to="/preview"/>}/>

            {/* защищенные роуты */}
            <Route path="/user" element={<ProtectedRoutes/>}> 
              <Route index element={<Applications/>}/>
              {/* <Route path="/startapp" element={<StartApp/>}/> */}
            </Route>

            
            <Route path="*" element={<Navigate to="/"/>} />
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

