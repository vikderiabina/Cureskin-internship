# Created by vderiabina at 6/28/2023
Feature: Tests for Amazon Privacy Notice page

Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original window
 And Click on Amazon Privacy Notice link
 And Switch to new window
 Then Verify Amazon Privacy Notice page is opened
 And Return to original window