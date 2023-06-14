
Feature: Amazon Sign in tests

  Scenario: User can see Sign in page
    Given Open amazon main page
    When Click Orders
    Then Verify Sign In page opens

  Scenario: Sign In page can be opened from SignIn popup
    Given Open amazon main page
    When Click on button from SignIn popup
    Then Verify Sign In page opens

  Scenario: Amazon users see sign in button
    Given Open amazon main page
    Then Verify Sign In is clickable
    When Wait for 5 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears



