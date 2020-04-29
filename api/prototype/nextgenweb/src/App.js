import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import SiteHeader from './WebsiteHeader';
import SiteFooter from './WebsiteFooter';
import MenuStateUser from './MenuStateUser';
import MD from "./maryland.jpg";

function App() {
  return (
    <body class="ds-base">
      <div id="js-root">
        <div class="docs" data-reactroot>
      
        {/* Website Title Header*/}
        <SiteHeader/>

          {/* Body of Webpage */}
          <div class="ds-l-row ds-u-margin--0">
            
            {/* Left-Hand Menu/Navigation Pane */}
            <MenuStateUser state="Maryland"/>

            {/* Main Text Body */}
            <main id="main" class="ds-l-md-col ds-u-padding--0 ds-u-padding-bottom--4">
              <div>

                {/* PREAMBLE OF FORM */}
                <header class="ds-u-padding--3 ds-u-sm-padding--6 ds-u-display--block ds-u-fill--gray-lightest">
                  <h1 class="ds-display" id="">Preamble</h1>
                  <div class="ds-u-clearfix"></div>
                  <div class="ds-u-font-size--small"></div>
                </header>
                <div class="ds-u-border-top--1 ds-u-padding-x--3 ds-u-sm-padding-x--6">
                  <article class="ds-u-margin-y--3 ds-u-sm-margin-y--6 l-content">
                  <div class="c-details ds-u-margin-top--2 ds-u-measure--wide">
                    <h2>
                      FRAMEWORK FOR THE ANNUAL REPORT OF THE CHILDREN'S HEALTH INSURANCE PLANS 
                      UNDER TITLE XXI OF THE SOCIAL SECURITY ACT
                    </h2>
                    <p>
                      Section 2108(a) and Section 2108(e) of the Social Security Act (the Act) provide that each state and territory* 
                      must assess the operation of its state child health plan in each federal fiscal year and report to the Secretary, 
                      by January 1 following the end of the federal fiscal year, on the results of the assessment. 
                      In addition, this section of the Act provides that the state must assess the progress made in reducing the number 
                      of uncovered, low-income children.  The state is out of compliance with CHIP statute and regulations if the report 
                      is not submitted by January 1. The state is also out of compliance if any section of this report relevant to 
                      the state’s program is incomplete.
                    </p>
                    <p>The framework is designed to:</p>
                    <ul>
                      <li>Recognize the <b>diversity</b> of state approaches to CHIP and allow states <b>flexibility</b> to highlight key 
                      accomplishments and progress of their CHIP programs, <b>AND</b></li>
                      <li>Provide <b>consistency</b> across states in the structure, content, and format of the report, <b>AND</b></li>
                      <li>Build on data <b>already collected</b> by CMS quarterly enrollment and expenditure reports, <b>AND</b></li>
                      <li>Enhance <b>accessibility</b> of information to stakeholders on the achievements under Title XXI</li>
                    </ul>
                    <p>The CHIP Annual Report Template System (CARTS) is organized as follows:</p>
                    <ul>
                      <li>Section I: Snapshot of CHIP Programs and Changes</li>
                      <li>Section II: Program's Performance Measurement and Progress</li>
                      <li>Section III: Assessment of State Plan and Program Operation</li>
                      <li>Section IV: Program Financing for State Plan</li>
                      <li>Section V: Program Challenges and Accomplishments</li>
                    </ul>
                    <p class="ds-u-font-size--small">*When "state" is referenced throught this template it is defined as either a state or a territory.</p>
                    <p class="ds-u-font-size--small"><b>
                      Disclosure: According to the Paperwork Reduction Act of 1995, no persons are required to respond to a collection 
                      of information unless it displays a valid OMB control number. The valid OMB control number for this information 
                      collection is 0938-1148. The time required to complete this information collection is estimated to average 40 hours 
                      per response, including the time to review instructions, search existing data resources, gather the data needed, 
                      and complete and review the information collection. If you have any comments concerning the accuracy of the time 
                      estimate(s) or suggestions for improving this form, write to: 
                      CMS, 7500 Security Blvd., Attn: PRA Reports Clearance Officer, Mail Stop C4-26-05, Baltimore, Maryland 21244-1850.
                    </b></p>
                  </div>
                  </article>
                </div>
              </div>
            </main>
          </div>

          {/* Website Footer */}
          <SiteFooter/>
          
          </div>
          <div id="root"></div>
        </div>
    </body>
  );
}

export default App;
