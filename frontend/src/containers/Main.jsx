import React, { useState } from 'react'

import { BrowserRouter as Router } from 'react-router-dom'

import 'fontsource-roboto'

import Header from './Header'
import Sidebar from './Sidebar'
import Content from './Content'

import Global from '../styles/global'

const Main = () => {
    return (
        <Router>
            <Global />

            <Header></Header>
            <Sidebar></Sidebar>
            <Content></Content>
        </Router>
    )
}

export default Main
