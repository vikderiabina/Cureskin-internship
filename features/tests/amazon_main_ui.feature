# Created by vderiabina at 5/19/2023
Feature: Tests for main page UI

  Scenario: User sees all footer links
    Given Open amazon main page
    Then Verify there are 36 links

  Scenario: User can see language options
    Given Open amazon main page
    When Hover over language options
    Then Verify Spanish option present
