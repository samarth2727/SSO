*** Settings ***
Library    SeleniumLibrary
Resource    ../../Resources/SsoAdmin/Login/login_keywords.robot
Library     ../../../Resources/CustomKeywords/utilities.py
Library     ../../Resources/testcontainers_library.py

Library     Testcontainer
Test Setup      Open SSO Application
Test Teardown   Close Browser

*** Variables ***
${login_td}=    ${CURDIR}${/}..${/}..${/}TestData${/}SsoAdmin${/}Login${/}login_testdata.xlsx
${sso_image}=   my-robotframework-image
*** Test Cases ***

SSO_001 Verify The Functionality Of Login Page With Valid Credentials
    [Tags]  regression
    Start SSO Container    ${sso_image}
    ${login_data}=   Fetch Testdata By Id    ${login_td}    SSO_001
    Login With Username And Password | SSO    ${login_data}
    Verify Login Is Successfull With Valid Username And Password
    Stop SSO Container

SSO_002 Verify The Functionality Of Login Page With Valid Email And Invalid Password
    [Tags]  regression
    ${login_data}=   Fetch Testdata By Id    ${login_td}    SSO_002
    Login With Username And Password | SSO    ${login_data}
    Verify Login With Valid Email And Invalid Password
    Stop SSO Container

SSO_003 Verify Enter Invalid Email & Valid Password Click On Login Button Then Check The Response.
    [Tags]  regression
    Start SSO Container    ${sso_image}
    ${login_data}=   Fetch Testdata By Id    ${login_td}    SSO_003
    Login With Username And Password | SSO    ${login_data}
    Verify Login With Valid Email And Invalid Password
    Stop SSO Container

SSO_004 Verify Check Whether Email And Password Are Case Sensitive Or Not
    [Tags]  regression
    Start SSO Container    ${sso_image}
    ${login_data}=   Fetch Testdata By Id    ${login_td}    SSO_004
    Login With Username And Password | SSO    ${login_data}
    Verify Login With Valid Email And Invalid Password
    Stop SSO Container



