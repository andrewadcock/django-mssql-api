//This is the component for the standard website header
import React from 'react';
import './App.css';
import Logo from "./cms-site-logo.png";

const WebsiteHeader = () => {
    return (
        <header class="ds-base--inverse ds-u-padding--3 ds-u-display--flex ds-u-justify-content--between ds-u-align-items--center">
            <img alt="cms logo" src={Logo}/>  
            <h1 class="ds-h2 ds-u-margin-bottom--0">
                <a href="/" class="ds-c-link--inverse ds-u-text-decoration--none" title="Home">CHIP Annual Report Template System (CARTS)</a>
            </h1>
            <h6 class="ds-u-margin-bottom--0">[Login]</h6>
        </header>
    );
};

export default WebsiteHeader;