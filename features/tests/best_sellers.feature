# Created by vderiabina at 5/21/2023
Feature: Tests  for amazon BestSellers functionality

  Scenario:   Scenario: User sees all links
    Given Open Amazon Bestsellers
    Then Verify there are 5 links for BestSellers


  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens