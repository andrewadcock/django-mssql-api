//This is the component for the standard website footer
import React from 'react';
import './App.css';

const WebsiteFooter = () => {
    return (
        <footer>
            {/* 3 Column Banner of Footer */}
            <section class="ds-base--inverse">
                <div class="ds-l-container ds-u-padding--2 ds-u-padding-top--4">
                <div class="ds-l-row">
                    {/* Contact Us */}
                    <div class="ds-l-col--12 ds-l-sm-col--4 ds-l-lg-col--4 ds-u-margin-bottom--4 ds-u-margin-top--2">
                    <h6 class="ds-h4">Contact Us</h6>
                    <p class="ds-u-font-size--small">
                        Need help with CARTS?
                        <br></br>
                        <a href="mailto:MACPro_CARTS_Support@collabralink.com">Email the CARTS Help Desk</a>
                    </p>
                    </div>
                    {/* CMS/HHS Websites */}
                    <dl class="ds-l-col--12 ds-l-sm-col--4 ds-l-lg-col--4 ds-u-margin-bottom--4">
                    <dt class="ds-h4">CMS &amp; HHS Websites</dt>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.cms.gov" target="_blank">CMS.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.medicare.gov" target="_blank">Medicare.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.mymedicare.gov" target="_blank">MyMedicare.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.medicaid.gov" target="_blank">Medicaid.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.healthcare.gov" target="_blank">HealthCare.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.HHS.gov/open" target="_blank">HHS.gov</a>
                    </dd>
                    </dl>
                    {/* Additional Resources */}
                    <dl class="ds-l-col--12 ds-l-sm-col--4 ds-l-lg-col--4 ds-u-margin-bottom--4">
                    <dt class="ds-h4">Additional Resources</dt>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="https://standards.usa.gov/" target="_blank">U.S. Web Design Standards</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.cms.gov/About-CMS/Agency-Information/Aboutwebsite/FOIA.html" target="_blank">Freedom of Information Act</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="https://oig.hhs.gov/" target="_blank">Inspector General</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.cms.gov/About-CMS/Agency-Information/Aboutwebsite/NoFearAct.html" target="_blank">No Fear Act</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.medicare.gov/about-us/plain-writing/plain-writing.html" target="_blank">Plain Writing</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="http://www.usa.gov" target="_blank">USA.gov</a>
                    </dd>
                    <dd class="ds-u-font-size--small ds-u-margin-left--0">
                        <a href="https://cms.gov/privacy/" target="_blank">Privacy Policy</a>
                    </dd>
                    </dl>
                </div>
                </div>
            </section>

            <section class="ds-base--inverse ds-u-padding-bottom--4">
                <div class="ds-l-container ds-u-padding-y--2 ds-u-text-align--center">
                <p class="ds-text ds-u-font-size--small">
                    A federal government website managed by <a href="www.collabralink.com" class="ds-c-link--inverse">CollabraLink Technologies, Inc.</a> 
                    for the Centers for Medicare &amp; Medicaid Services 7500 Security Boulevard, Baltimore, MD 21124
                </p>
                </div>
            </section>

            </footer>
    );
};

export default WebsiteFooter;