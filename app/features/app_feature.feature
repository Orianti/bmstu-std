Feature: Delete

  Scenario: Delete city
    Given city
      And location
    When I delete city
    Then response status code should be 204
      And I should not see location