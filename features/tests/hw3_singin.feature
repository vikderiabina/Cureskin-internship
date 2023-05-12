
Feature: Returns and Orders Page for Logged-out Users

  Scenario: User can can see Sign in page on Amazon when clicking on Returns and Orders
    Given a user is not logged in
    When the user clicks on the Returns and Orders link
    Then Verify Sign In page is present
    Then Verify Sign email input field is present