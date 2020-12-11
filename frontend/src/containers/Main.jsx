import React, { useState } from 'react'

import { BrowserRouter as Router } from 'react-router-dom'

import 'fontsource-roboto'

import StoreProvider from '../store/StoreContext'
import AuthProvider from '../store/AuthContext'
import ViewportProvider from '../store/ViewportContext'

import Header from './Header'
import Sidebar from './Sidebar'
import Content from './Content'

import Global from '../styles/global'

const Main = () => {
    return (
        <Router>
            <Global />
            <StoreProvider>
                <ViewportProvider>
                    <AuthProvider>
                        <Header></Header>
                        <Sidebar></Sidebar>
                        <Content></Content>
                    </AuthProvider>
                </ViewportProvider>
            </StoreProvider>
        </Router>
    )
}

export default Main
