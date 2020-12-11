import React, { useEffect, useState } from 'react'
import axios from 'axios'

import { useAuth } from '../../store/AuthContext'

function Login() {
    // return <div>oi</div>
    const { auth, setAuth } = useAuth()
    const [data, setData] = useState([])
    const [username, setUsername] = useState('')
    const [pw, setPw] = useState('')

    useEffect(() => {
        // async function getSessoes() {
        //     const response = await axios.get(
        //         'http://127.0.0.1:8000/api/v1/sessoes/'
        //     )
        //     console.log(response.data)
        //     setData(response.data)
        // }
        // getSessoes()
    }, [])

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
        <div>
            <h3>Login</h3>
            <br />
            <form onSubmit={formHandler}>
                <input
                    name="username"
                    placeholder="E-mail"
                    onChange={(e) => {
                        // console.log(e.target.value)
                        setUsername(e.target.value)
                    }}
                ></input>
                <input
                    placeholder="Password"
                    type="password"
                    onChange={(e) => {
                        // console.log(e.target.value)
                        setPw(e.target.value)
                    }}
                ></input>
                <button>Botao</button>
            </form>
            <div>Logado: {auth.logado ? 'Sim' : 'Nao'}</div>
            <br />
            <div>Token: {auth.token}</div>
            <br />
            {/* {data.map((sessao) => {
                return (
                    <div>
                        <h3>Login: {JSON.stringify(sessao)}</h3>
                    </div>
                )
            })} */}
        </div>
    )
}

export default Login
