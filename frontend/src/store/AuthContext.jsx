import React, { createContext, useState, useContext, useEffect } from 'react'

const authContext = createContext()

export default function AuthProvider({ children }) {
    const [auth, setAuth] = useState({
        logado: false,
        token: '',
    })

    useEffect(() => {
        // console.log('localStorage.setItem')
        if (localStorage.getItem('auth')) {
            setAuth(Object.assign({}, JSON.parse(localStorage.getItem('auth'))))
        } else {
            localStorage.setItem('auth', JSON.stringify(auth))
        }
    }, [])

    useEffect(() => {
        localStorage.setItem('auth', JSON.stringify(auth))
    }, [auth.logado])

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
