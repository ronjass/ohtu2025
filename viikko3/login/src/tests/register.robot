*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  newpassword123
    Set Password Confirmation  newpassword123
    Click Button  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  newpassword123
    Set Password Confirmation  newpassword123
    Click Button  Register
    Page Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  newuser
    Set Password  new
    Set Password Confirmation  new
    Click Button  Register
    Page Should Contain  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  newuser
    Set Password  newpassword
    Set Password Confirmation  newpassword
    Click Button  Register
    Page Should Contain  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  newuser
    Set Password  newpassword123
    Set Password Confirmation  differentpassword123
    Click Button  Register
    Page Should Contain  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  newpassword123
    Set Password Confirmation  newpassword123
    Click Button  Register
    Page Should Contain  Username is already taken

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Registration Should Succeed
    Welcome Page Should Be Open

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page