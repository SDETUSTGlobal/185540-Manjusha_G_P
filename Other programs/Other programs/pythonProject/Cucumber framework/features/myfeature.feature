Feature: OrangeHRM Logo
  Scenario: Logo presence in home page
    Given Launch chrome browser
    When Open orange home page
    Then verify logo is present
    And close browser
