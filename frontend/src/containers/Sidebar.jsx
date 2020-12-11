import React, { useEffect, useState } from 'react'
import styled, { keyframes } from 'styled-components'

import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom'
// import { BrowserRouter as Router } from 'react-router-dom'

import 'fontsource-roboto'

import { useViewport } from '../store/ViewportContext'
import profile from '../images/profile.png'

const Sidebar = () => {
    const { layout, toggle, setToggle } = useViewport()

    const mobile = () => (layout === 'mobile' ? true : false)

    const hideSidebar = () => {
        if (layout === 'mobile' && toggle === true) return false
        if (layout === 'mobile' && toggle === false) return true
        if (layout === 'desktop' && toggle === true) return false
        if (layout === 'desktop' && toggle === false) return true
    }

    return (
        <SidebarContainer hideSidebar={hideSidebar()}>
            <div>
                <img src={profile} className="profile_image" alt="" />
                <h4>Jessica</h4>
            </div>

            <a href="#">
                <i className="fas fa-desktop"></i>
                <span>Dashboard</span>
            </a>
            <a href="#">
                <i className="fas fa-cogs"></i>
                <span>Components</span>
            </a>
            <a href="#">
                <i className="fas fa-table"></i>
                <span>Tables</span>
            </a>
            <a href="#">
                <i className="fas fa-th"></i>
                <span>Forms</span>
            </a>
            <a href="#">
                <i className="fas fa-info-circle"></i>
                <span>About</span>
            </a>
            <a href="#">
                <i className="fas fa-sliders-h"></i>
                <span>Settings</span>
            </a>
        </SidebarContainer>
    )
}

const SidebarContainer = styled.div`
    z-index: 3;
    position: fixed;
    left: 0;
    top: var(--header-height);
    width: var(--sidebar-width);
    height: 100%;
    background: #2f323a;
    display: flex;
    flex-direction: column;
    transition: 0.25s;
    transition-property: all;
    overflow-y: auto;

    width: ${(props) => props.hideSidebar && '0'};
    pointer-events: ${(props) => props.hideSidebar && 'none'};

    div {
        height: 22rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        opacity: 1;
        transition: 0.5s;
        transition-property: all;
    }

    img {
        margin-top: 5rem;
        width: 10rem;
        height: 10rem;
        border-radius: 10rem;
        margin-bottom: 1rem;
    }

    h4 {
        color: #ccc;
        margin-top: 1rem;
        margin-bottom: 20px;
    }

    a {
        display: flex;
        align-items: center;
        height: 6rem;
        font-size: 20px;
        color: #fff;
        padding: 2rem;
        transition: 0.5s;
        transition-property: background, font-weight;
    }

    a:hover {
        background: #19b3d3;
        font-weight: bold;
    }

    i {
        padding-right: 10px;
    }
`

export default Sidebar
