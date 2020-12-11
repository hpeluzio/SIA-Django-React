import React, { createContext, useState, useContext } from 'react'

const authContext = createContext()

export default function AuthProvider({ children }) {
    const [auth, setAuth] = useState({
        logado: false,
        token: '',
    })
    return (
        <authContext.Provider value={{ auth, setAuth }}>
            {children}
        </authContext.Provider>
    )
}

export function useAuth() {
    const { auth, setAuth } = useContext(authContext)
    return { auth, setAuth }
}
