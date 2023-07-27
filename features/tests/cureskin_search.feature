# Created by vderiabina at 7/16/2023
Feature: Cureskin Search tests

  Scenario: User can search in Cureskin
    Given Open main page
    When Click Search
    And Search for SPF
    Then Verify search results shown for “SPF”
