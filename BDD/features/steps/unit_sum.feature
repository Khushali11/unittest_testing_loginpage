Feature: Addition Function
  In order to use the add function correctly
  As a developer
  I want to ensure it adds numbers properly

  Scenario: Adding positive numbers
    Given I have the numbers 1 and 2
    When I add the numbers
    Then the result should be 3

  Scenario: Adding negative numbers
    Given I have the numbers -1 and -2
    When I add the numbers
    Then the result should be -3

  Scenario: Adding mixed numbers
    Given I have the numbers 1 and -2
    When I add the numbers
    Then the result should be -1

    Given I have the numbers -1 and 2
    When I add the numbers
    Then the result should be 1