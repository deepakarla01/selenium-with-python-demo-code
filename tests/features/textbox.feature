Feature: Text Box Page Functionality

  Scenario Outline: Enter the user details
    Given I am on "Text Box" Page
    When I enter a value "<full_name>" in the Full Name field
    And I enter a value "<e_mail>" in the E-mail field
    And I enter a value "<current_address>" in the Current Address field
    And I enter a value "<permanent_address>" in the Permanent Address field
    And I click on Submit button
    Then I should see the success information

    Examples:
    | full_name | e_mail | current_address | permanent_address |
    | John Doe | John.Doe@gmail.com | 123 Main St, Redmond, USA | 321 Main St, Redmond, USA |
    | Jane Doe | Jane.Doe@gmail.com | 456 Elm St, Bellevue, USA | 654 Elm St, Bellevue, USA |
