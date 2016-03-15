Feature: title test

  Scenario: visiting google
    When visiting google
    Then its title should be "Google"

  Scenario: visiting another google
    When visiting google
    Then its title should be "Google"
