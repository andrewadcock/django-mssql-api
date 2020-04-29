//This is the component for the standard left-hand menu that a State User sees
import React from 'react';
import './App.css';
import MD from "./maryland.jpg";

const MenuStateUser = props => {
    return (
        <nav class="ds-l-md-col--3 da-u-padding--2 ds-u-fill--white docs__sidebar">
            {/**State Icon & Name */}
            <div class="ds-l-row ds-u-margin--0">
            <img class="ds-u-padding-left--3 ds-u-padding-top--1 ds-u-padding-bottom--0" src={MD}></img>
            <p class="ds-u-padding-left--3 ds-u-padding-top--0"><b> {props.state} </b></p>
            </div>

            <ul class="ds-c-veritcal-nav c-nav__list">
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Preamble</a>
                </li>
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Section I: Snapshot</a>
                </li>
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Section II: Performance</a>
                </li>
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Section III: Assessment</a>
                </li>
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Section IV: Financing</a>
                </li>
                <li class="ds-c-veritcal-nav__item">
                    <a class="ds-c-veritcal-nav__label" href="/">Section V: Challenges</a>
                </li>
            </ul>
        </nav>
    );
};

export default MenuStateUser;