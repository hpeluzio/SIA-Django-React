import React, { useState } from 'react'
import styled from 'styled-components'

import { useAuth } from '../../store/AuthContext'

function Home() {
    const { auth, setAuth } = useAuth()
    const lorem =
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    const [lorens, setLorens] = useState([])

    return (
        <>
            <div>Logado: {auth.logado ? 'Sim' : 'Nao'}</div>
            <br />
            <div>Token: {auth.token}</div>
            <br />
            <Button
                onClick={() => {
                    var lor = [...lorens]
                    lor.push(lorem)
                    console.log(lor)
                    setLorens(lor)
                }}
            >
                ADD LOREM
            </Button>
            {lorens.map((lorem, idx) => {
                return (
                    <LoremDiv>
                        <h3>
                            <h5>
                                <h3>Lorem {idx}:</h3> {lorem}{' '}
                            </h5>
                            <hr />
                        </h3>
                    </LoremDiv>
                )
            })}
            <hr />
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
