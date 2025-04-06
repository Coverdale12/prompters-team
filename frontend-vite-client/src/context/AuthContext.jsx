import { createContext, useState } from "react";

export const AuthContext = createContext();


export function AuthProvider({ children }) {
  const [isAuth, setAuth] = useState(true);


  return(
    <AuthContext.Provider value={{isAuth, setAuth}}>
      {children}
    </AuthContext.Provider>
  )

}