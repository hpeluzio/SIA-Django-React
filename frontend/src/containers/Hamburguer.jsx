import React from 'react'
import styled from 'styled-components'

import { useViewport } from '../store/ViewportContext'

const Hamburguer = () => {
    const { layout, toggle, setToggle } = useViewport()

    const xhamburguer = () =>
        layout === 'mobile' && toggle === true ? true : false

    return (
        <MenuToggle
            xhamburguer={xhamburguer()}
            value={toggle}
            onClick={() => {
                setToggle(!toggle)
            }}
        >
            <div className="one"></div>
            <div className="two"></div>
            <div className="three"></div>
        </MenuToggle>
    )
}

const MenuToggle = styled.div`
    background: rgba(0, 0, 0, 0);
    /* background: purple; */
    margin-left: 10px;
    margin-right: 10px;
    /* margin-top: 2.5px; */

    transition-property: all;
    transition-duration: 0.5s;

    :hover {
        .one,
        .two,
        .three {
            background-color: #19b3d3;
        }
    }

    .one,
    .two,
    .three {
        width: 30px;
        height: 5px;
        background: white;
        margin: 0 0 5px auto;
        opacity: 1;
        transition-property: all;
        transition-duration: 0.5s;
    }

    .one {
        transform: ${(props) =>
            props.xhamburguer && 'rotate(45deg) translate(0.6rem, 0.6rem)'};
    }
    .two {
        opacity: ${(props) => props.xhamburguer && '0'};
    }

    .three {
        transform: ${(props) =>
            props.xhamburguer && 'rotate(-45deg) translate(0.85rem, -0.8rem)'};
    }
`

export default Hamburguer
