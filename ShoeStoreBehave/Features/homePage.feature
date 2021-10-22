Feature: I navigate to https://shoe-store-july.herokuapp.com/

  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Validating the navbar
    Given Launch the App
    When navbar element found
    Then navigate to All Shoes
    Then I click the All Shoes link
    And close the App