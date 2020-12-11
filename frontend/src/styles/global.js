import { createGlobalStyle } from 'styled-components'

export const Global = createGlobalStyle`
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    outline: 0;
}

:root {
    --header-height: 70px;
    --sidebar-width: 220px;
    --sidebar-height: 100%;
}

html {
    font-size: 62.5%;
}

body {
    font-size: 1.6rem;
    font-family: 'Roboto', Georgia, serif;
    /* background-color: rgba(0,0,0,.1); */
}

li {
    list-style: none;
}

a {
    text-decoration: none;
}

/* :root {
  font-size: 24px;

  @media (min-width: 768px) {
    font-size: 18px;
  }

  @media (min-width: 1024px) {
    font-size: 16px;
  }
} */


/* CUSTOM SCROLL */
::-webkit-scrollbar {
    width: 5px;
    height: 5px;
}

/* Track */
::-webkit-scrollbar-track {
    background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
    background: #888;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
    background: #555;
}

`

export default Global
