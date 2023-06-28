Feature: Open "cart" on Amazon

  Scenario: User clicks on cart icon and sees empty cart
    Given Open amazon home page
    When Open cart page
    Then Verify that Amazon Cart has the following text Your Amazon Cart is empty