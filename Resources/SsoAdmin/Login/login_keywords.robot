*** Settings ***
Library    SeleniumLibrary
Variables  ../../../Environment/environments.py
Variables  ../../../PageObjects/SsoAdmin/Login/login_locators.py
Variables  ../../../PageObjects/SsoAdmin/Dashboard/dashboard.py
Variables   ../../../PageObjects/SsoAdmin/Enterprises/enterprise_summary_locators.py
*** Keywords ***

Open SSO Application
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --disable-notifications
    Call Method  ${options}  add_argument  --disable-infobars
    Call Method  ${options}  add_argument  --disable-extensions
    Call Method  ${options}  add_argument  --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Call Method  ${options}  add_argument  --disable-dev-shm-usage
    Open Browser     ${sso_application_url}    ${browser}   options=${options}
#     Open Browser    ${sso_application_url}    ${browser}    options=add_argument("--headless")
    Set Window Size    ${window_height}    ${window_width}
    Wait Until Page Contains Element    ${login_page_title}
    Page Should Contain Element     ${login_page_title}

Verify Login Is Successfull With Valid Username And Password
    Wait Until Page Contains Element    ${enterprise_icon}
    Page Should Contain Element    ${enterprise_icon}

Verify Login With Valid Email And Invalid Password
    Wait Until Page Contains Element    ${alert}
    Page Should Contain Element     ${alert}

Login With Valid Username And Password | SSO
    [Arguments]     ${login_data}
    ${td_login}    Create Dictionary   &{login_data}
    Wait Until Page Contains Element    ${email_field}    timeout=20
    Input Text    ${email_field}    ${td_login.Email}
    Wait Until Element Is Enabled    ${password_field}
    Input Text    ${password_field}    ${td_login.Password}
    Click Element    ${login_button}
    Wait Until Page Contains Element    ${ginesys_logo}
    Page Should Contain Element    ${ginesys_logo}
    Page Should Contain Element    ${enterprises_header}

Login With Username And Password | SSO
    [Arguments]     ${login_data}
    ${td_login}    Create Dictionary   &{login_data}
    Input Text    ${email_field}    ${td_login.Email}
    Wait Until Element Is Enabled    ${password_field}
    Input Text    ${password_field}    ${td_login.Password}
    Click Element    ${login_button}

