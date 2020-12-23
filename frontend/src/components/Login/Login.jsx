import React, { useEffect, useState } from 'react'
import { Redirect } from 'react-router-dom'
import styled from 'styled-components'
import axios from 'axios'

import { useAuth } from '../../store/AuthContext'
import { useViewport } from '../../store/ViewportContext'

function Login() {
    // return <div>oi</div>
    const { auth, setAuth } = useAuth()
    const [data, setData] = useState([])
    const [username, setUsername] = useState('')
    const [pw, setPw] = useState('')
    const { toggle, setToggle } = useViewport()

    useEffect(() => {
        // setToggle(false)
        if (auth.logado === true) {
            console.log('Loguei')
            return <Redirect to="/" />
        }
    }, [auth.logado])

    const formHandler = (e) => {
        e.preventDefault()
        // http://127.0.0.1:8000/api-token-auth/
        async function login() {
            await axios
                .post('http://127.0.0.1:8000/api-token-auth/', {
                    username: username,
                    password: pw,
                })
                .then(function (response) {
                    console.log(response.data)
                    if (response.data.token) {
                        const newAuthState = { ...auth }
                        newAuthState.logado = true
                        newAuthState.token = response.data.token
                        setAuth(newAuthState)
                        return <Redirect to="/" />
                        // setToggle(true)
                    }
                })
                .catch(function (error) {
                    console.log(error)
                })
        }

        login()

        console.log('formHandler: ', username, ' - ', pw)
    }

    return (
        <>
            <Form onSubmit={formHandler}>
                <h3>Login</h3>
                <br />
                <Input
                    name="username"
                    placeholder="E-mail"
                    onChange={(e) => {
                        // console.log(e.target.value)
                        setUsername(e.target.value)
                    }}
                ></Input>
                <Input
                    placeholder="Password"
                    type="password"
                    onChange={(e) => {
                        // console.log(e.target.value)
                        setPw(e.target.value)
                    }}
                ></Input>
                <Button>Login</Button>
                <p class="message">
                    Não registrado? <a href="#">Criar uma conta</a>
                </p>
                <br />
                <div>Logado: {auth.logado ? 'Sim' : 'Nao'}</div>
                <br />
                <div>Token: {auth.token}</div>
            </Form>
        </>
    )
}

const Form = styled.form`
    background: white;
    width: 350px;
    height: 400px;
    position: relative;
    margin: 10vh auto;
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);

    .message {
        margin: 15px 0 0;
        color: #b3b3b3;
        font-size: 12px;
    }
    .message a {
        color: #4c9993;
        text-decoration: none;
    }
`

const Input = styled.input`
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1), 0 2px 2px 0 rgba(0, 0, 0, 0.2);
    background: #000000;
    font-family: 'Roboto', sans-serif;
    outline: 0;
    background: #dde4e9;
    width: 100%;
    border: 0;
    margin: 0 0 15px;
    padding: 15px;
    box-sizing: border-box;
    font-size: 14px;
`

const Button = styled.button`
    font-family: 'Roboto', sans-serif;
    text-transform: uppercase;
    outline: 0;
    background: #4c9993;
    width: 100%;
    border: 0;
    padding: 15px;
    color: #ffffff;
    font-size: 14px;
    -webkit-transition: all 0.3 ease;
    transition: all 0.3 ease;
    cursor: pointer;
`

export default Login
