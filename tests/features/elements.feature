Feature:Check Elements Page Functionality

#  Background:
#    Given I am on Elements page

  Scenario Outline: Click on "<menu_link>" menu
    When I click on "<menu_link>" menu
    Then I should navigate to "<menu_link>" Page

  Examples:
    | menu_link |
    | Text Box |
    | Check Box |
    | Radio Button |
    | Web Tables |
    | Buttons |
    | Links |
    | Broken Links - Images |
    | Upload and Download |
    | Dynamic Properties |

