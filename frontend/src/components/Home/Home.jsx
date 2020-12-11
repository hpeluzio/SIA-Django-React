import React, { useState } from 'react'
import styled from 'styled-components'

import { useAuth } from '../../store/AuthContext'

function Home() {
    const { auth, setAuth } = useAuth()

    return (
        <>
            <h3>Home</h3>
            <br />
            <div>Logado: {auth.logado ? 'Sim' : 'Nao'}</div>
            <br />
            <div>Token: {auth.token}</div>
            <br />
        </>
    )
}

const Button = styled.button`
    /* width: 10rem;
    height: 4rem;
    background: DodgerBlue;
    color: white;
    font-weight: bold;
    border: 2px solid rgba(0, 0, 0, 0.4); */

    background-color: DodgerBlue; /* Green */
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: white;
    font-weight: bold;
    padding: 1rem 2rem;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
`
const LoremDiv = styled.div`
    padding: 1rem;
`

export default Home
