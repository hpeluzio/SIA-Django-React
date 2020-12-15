import React, { useState } from 'react'
import styled from 'styled-components'
import { Link } from 'react-router-dom'

import { useViewport } from '../store/ViewportContext'
import { useAuth } from '../store/AuthContext'
import Hamburguer from './Hamburguer'
import Logout from './Logout'

const Header = () => {
    const { layout, toggle, setToggle } = useViewport()
    const { auth, setAuth } = useAuth()
    const [showLogoutModal, setShowLogoutModal] = useState(false)

    const mobile = () => (layout === 'mobile' ? true : false)

    // const logout = () => {
    //     setAuth({ logado: false, token: '' })
    // }
    const logout = () => {
        // return <Logout></Logout>
        setShowLogoutModal(!showLogoutModal)
    }

    return (
        <>
            {showLogoutModal === true && <Logout logout={logout}></Logout>}
            {auth.logado === true && mobile() === true && toggle === true && (
                <Backwrap
                    onClick={() => {
                        setToggle(!toggle)
                    }}
                ></Backwrap>
            )}
            <HeaderBar>
                <LeftHeader>
                    {auth.logado === true && (
                        <Hamburguer
                            layout={layout}
                            toggle={toggle}
                            setToggle={setToggle}
                        />
                    )}
                    <Spacer />

                    <Link to="/" className="logo_home">
                        <h3>
                            App <span>Logo</span>
                        </h3>
                    </Link>
                </LeftHeader>

                <RightHeader>
                    <Spacer />

                    {auth.logado === false && (
                        <LinkHeader to="/register">
                            <div>Register</div>
                        </LinkHeader>
                    )}
                    {auth.logado === false && (
                        <LinkHeader to="/login">
                            <div>Login</div>
                        </LinkHeader>
                    )}
                    {auth.logado === true && (
                        <LinkHeader onClick={logout} to="/login">
                            <div>Logout</div>
                        </LinkHeader>
                    )}
                </RightHeader>
            </HeaderBar>
        </>
    )
}

// HEADER
const HeaderBar = styled.div`
    z-index: 5;
    position: fixed;
    width: 100%;
    height: var(--header-height);
    background: #22242a;
    display: flex;
    align-items: center;
`

const LeftHeader = styled.div`
    height: 100%;
    margin: 0;
    display: flex;
    align-items: center;
    width: var(--sidebar-width);

    i {
        display: fixed;
        font-size: 25px;
        margin-left: 15px;
        margin-right: 10px;
        transition-duration: 0.1s;
        color: #fff;
        opacity: 1;
        cursor: pointer;

        :hover {
            color: #19b3d3;
        }
    }

    h3 {
        display: flex;
        color: #fff;
        text-transform: uppercase;
        font-size: 22px;
        font-weight: 900;
    }

    span {
        margin-left: 5px;
        color: #19b3d3;
    }
`

const RightHeader = styled.div`
    width: 100%;
    height: 100%;
    margin: 0;
    display: flex;
    align-items: center;
`

const LinkHeader = styled(Link)`
    padding: 2.5rem;
    font-size: 1.6rem;
    color: #fff;
    transition-duration: 0.5s;
    transition-property: all;

    :hover {
        font-weight: bold;
        background: #19b3d3;
    }

    a {
        color: white;
    }
`

const Spacer = styled.div`
    flex-grow: 1;
`

const Backwrap = styled.div`
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 2;
    background: rgba(0, 0, 0, 0.5);
`

export default Header
