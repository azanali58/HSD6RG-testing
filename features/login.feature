Feature: User login

  Background:
    Given the user is on the login page

  @login
  Scenario Outline: Logging in with valid data
    When the email field is filled with '<email>'
    And the Password field is filled with '<password>'
    And the user clicks on the login button
    Then the user is logged in
    Examples:
      | email       | password  |
      | y2k@y2k.com | 1234      |
      |ali@abc.com  | asdf      |
      |srk@srk.com  | ABCXYZ    |


  @login
  Scenario Outline: Logging in with invalid data
    When the email field is filled with '<email>'
    And the Password field is filled with '<password>'
    And the user clicks on the login button
    Then a '<errormessage>' is displayed
    Examples:
      | email       | password | errormessage                                          |
      | y2k@y2k.com | [blank]  | Warning: No match for E-Mail Address and/or Password. |
      | [blank]     | 1234     | Warning: No match for E-Mail Address and/or Password. |
      | [blank]     | [blank]  | Warning: No match for E-Mail Address and/or Password. |
