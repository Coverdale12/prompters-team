import { createContext} from "react";

export const AuthContext = createContext();


export function AuthProvider({ children }) {
  function setAuthLS(token) {
    localStorage.setItem("token", token)
  }
  function getAuthLS() {
    const token = localStorage.getItem("token")
    if (token) {
      return token
    } else {
      return false
    }
  }
  return (
    <AuthContext.Provider value={{ setAuthLS, getAuthLS }}>
      {children}
    </AuthContext.Provider>
  )

}