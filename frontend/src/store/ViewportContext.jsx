import React, { useState, useEffect, useContext, createContext } from 'react'

const viewportContext = createContext({})

export default function ViewportProvider({ children }) {
    const [width, setWidth] = useState(window.innerWidth)
    const [height, setHeight] = useState(window.innerHeight)
    const [layout, setLayout] = useState('none')
    const [toggle, setToggle] = useState(true)

    const handleWindowResize = () => {
        setWidth(window.innerWidth)
        setHeight(window.innerHeight)
    }

    useEffect(() => {
        window.addEventListener('resize', handleWindowResize)
        return () => window.removeEventListener('resize', handleWindowResize)
    }, [])

    useEffect(() => {
        if (width >= 768) setLayout('desktop')
        else setLayout('mobile')
    }, [width])

    useEffect(() => {
        if (layout === 'desktop') setToggle(true)
        if (layout === 'mobile') setToggle(false)
    }, [layout])

    return (
        <viewportContext.Provider value={{ layout, toggle, setToggle }}>
            {children}
        </viewportContext.Provider>
    )
}
export function useViewport() {
    const { layout, toggle, setToggle } = useContext(viewportContext)
    return { layout, toggle, setToggle }
}
