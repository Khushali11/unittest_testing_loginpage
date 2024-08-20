Feature: Login and Validation
  In order to ensure proper authentication and input validation
  As a user of the system
  I want to test the login and validation functions of the LoginPage class

  Scenario: Successful login with valid credentials
    Given I have a login page with valid credentials
    When I log in with the username "validuser" and the password "validpassword"
    Then I should see "Login successful"

  Scenario: Login with invalid username
    Given I have a login page with valid credentials
    When I log in with the username "invaliduser" and the password "validpassword"
    Then I should see "Invalid credentials"

  Scenario: Login with invalid password
    Given I have a login page with valid credentials
    When I log in with the username "validuser" and the password "invalidpassword"
    Then I should see "Invalid credentials"

  Scenario: Login with invalid username and password
    Given I have a login page with valid credentials
    When I log in with the username "invaliduser" and the password "invalidpassword"
    Then I should see "Invalid credentials"

  Scenario: Validate username that is too short
    Given I have a login page with valid credentials
    When I validate the username "ab"
    Then I should see "Username too short"

  Scenario: Validate username that is too long
    Given I have a login page with valid credentials
    When I validate the username "aaaaaaaaaaaaaaaaaaaaa"
    Then I should see "Username too long"

  Scenario: Validate valid username
    Given I have a login page with valid credentials
    When I validate the username "validuser"
    Then I should see "Username valid"

  Scenario: Validate password that is too short
    Given I have a login page with valid credentials
    When I validate the password "short"
    Then I should see "Password too short"

  Scenario: Validate valid password
    Given I have a login page with valid credentials
    When I validate the password "validpassword"
    Then I should see "Password valid"