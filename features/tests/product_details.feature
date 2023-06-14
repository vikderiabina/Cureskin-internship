# Created by vderiabina at 6/10/2023
Feature: Tests for product page

  Scenario Outline: User can select colors
    Given Open Amazon product <product_id> page
    Then Verify user can click through <colors>
    Examples:
      | product_id | colors |
      | B081YS2F7N   | Army Green,,Black,,Brown,,Burgundy,,Caramel,,Dark Blue|
      | B07BJKRR25   | Black,,Blue, Over Dye,,Bright White,,Dark Blue Vintage,,Dark Indigo/Rinsed,,Dark Khaki Brown|
