import React from 'react'

import StoreProvider from './store/StoreContext'
import AuthProvider from './store/AuthContext'
import ViewportProvider from './store/ViewportContext'
import Main from './containers/Main'
const App = () => {
    return (
        <StoreProvider>
            <ViewportProvider>
                <AuthProvider>
                    <Main></Main>
                </AuthProvider>
            </ViewportProvider>
        </StoreProvider>
    )
}

export default App
