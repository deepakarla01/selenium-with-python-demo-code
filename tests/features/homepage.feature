Feature: Homepage Functionality

  Background:
    Given I am on Demo QA Homepage

  Scenario Outline: Click on the "<card_name>" Card
    When I click on "<card_name>" Card
    Then I should navigate to "<card_name>" Page

  Examples:
    | card_name |
    | Elements |
    | Forms |
    | Alerts_Frame_Windows |
    | Widgets |
    | Interactions |
    | Books |