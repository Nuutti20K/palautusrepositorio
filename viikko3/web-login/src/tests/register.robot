*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  ville1
    Set Confirmation  ville1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  villeville
    Set Confirmation  villeville
    Submit Credentials
    Register Should Fail With Message  Password cannot consist of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Confirmation  ville456
    Submit Credentials
    Register Should Fail With Message  Password confirmation was incorrect

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  ville123
    Set Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  ville
    Set Password  ville123
    Set Confirmation  ville123
    Submit Credentials
    Go To Login Page
    Input Text  username  ville
    Input Password  password  ville123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  ville
    Set Password  ville123
    Set Confirmation  ville12
    Submit Credentials
    Go To Login Page
    Input Text  username  ville
    Input Password  password  ville123
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page