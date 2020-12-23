import React from 'react'
import styled from 'styled-components'
import { Link } from 'react-router-dom'

import { useAuth } from '../store/AuthContext'

const Logout = ({ logout }) => {
    const { auth, setAuth } = useAuth()

    const confirmLogout = () => {
        console.log('CONFIRM')
        setAuth({ logado: false, token: '' })
        logout()
    }

    return (
        <LogoutModal>
            <div className="container">
                <div className="title">Deseja realmenter efetuar logout?</div>
                <div className="btns">
                    <LogoutRetreat onClick={logout}>Não</LogoutRetreat>
                    <LogoutBtn onClick={confirmLogout}>Sim</LogoutBtn>
                </div>
            </div>
        </LogoutModal>
    )
    // return <div>LOGOUT</div>
}

const LogoutModal = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 6;
    background: rgba(0, 0, 0, 0.5);

    .container {
        box-sizing: border-box;
        margin-left: auto;
        margin-right: auto;
        margin-top: calc(500px - 150px);
        justify-content: center;
        width: 500px;
        height: 200px;
        background-color: white;

        .title {
            display: flex;
            align-items: center;
            background-color: rgba(0, 0, 0, 0.15);
            width: 100%;
            color: black;
            padding: 10px;
            height: 50px;
            /* margin: 15px; */
            font-weight: bold;
            font-size: 20px;
        }
        .btns {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 150px;
        }
    }
`

const LogoutBtn = styled.button`
    width: 200px;
    height: 60px;
    margin: 10px;
    border: 0px solid white;
    /* border: 1px solid rgba(0, 0, 0, 0.25); */
    background-color: darkgreen;
    font-weight: bold;
    font-size: 15px;
    color: white;
    transition: 0.25s all ease-in-out;
    cursor: pointer;

    :hover {
        background-color: green;
        box-shadow: 2px 2px 10px #888888;
    }
`

const LogoutRetreat = styled(LogoutBtn)`
    background-color: darkred;
    :hover {
        background-color: red;
    }
`

export default Logout
