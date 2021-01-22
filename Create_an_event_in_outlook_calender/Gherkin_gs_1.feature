Feature: create an event  in outlook

  Background: User logs into outlook web application
    Given user logged in to outlook

Scenario Outline: To create an event
    When user navigates to the event in Outlook page
    And user adds title of the event <event_title>
    And user adds date and time of the event
    And creates an event
    Then user verifies event <event_title> created successfully

    Examples:
      |event_title |
      |sample_event|
