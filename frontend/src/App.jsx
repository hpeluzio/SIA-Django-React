import React from 'react'

import StoreProvider from './store/StoreContext'
import AuthProvider from './store/AuthContext'
import ViewportProvider from './store/ViewportContext'
import Main from './containers/Main'
const App = () => {
    return (
        <StoreProvider>
            <AuthProvider>
                <ViewportProvider>
                    <Main></Main>
                </ViewportProvider>
            </AuthProvider>
        </StoreProvider>
    )
}

export default App
