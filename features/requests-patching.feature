Feature: The requests library should be patched to set default headers
  As a requests user
  I want to be able to have some headers set on every request
  So that I can pass tracing headers through the system

  Scenario: Requests happen with default headers
    Given I have the default headers set to
      | Header             | Value   |
      | X-Default-Provided | example |
    When I make a request
    Then the request should contain the headers
      | Header             | Value   |
      | X-Default-Provided | example |

  Scenario: Requests happen with default headers plus user provided ones
    Given I have the default headers set to
      | Header             | Value   |
      | X-Default-Provided | example |
    When I make a request with the headers
      | Header          | Value        |
      | X-User-Provided | user-example |
    Then the request should contain the headers
      | Header             | Value        |
      | X-User-Provided    | user-example |
      | X-Default-Provided | example      |

  Scenario: Requests happen as normal without defaults
    When I make a request with the headers
      | Header          | Value        |
      | X-User-Provided | user-example |
    Then the request should contain the headers
      | Header          | Value        |
      | X-User-Provided | user-example |

