Feature: Compose mail in outlook

  Background: User logs into outlook web application
    Given user logged in to outlook

  Scenario Outline: To compose mail in outlook
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail
    Then user verifies mail sent successfully // yet to be implemented


    Examples:
    |recipient_address|subject_line|mail_body|
    |abc@gmail.com   | sample mail | mail to check outlook functionality|


  Scenario Outline: To create an event in outlook
    When user navigates to the event in Outlook page
    And user adds title of the event <event_title>
    And user adds date and time of the event
    And creates an event
    Then user verifies event <event_title> created successfully

    Examples:
      |event_title |
      |sample_event|

  Scenario Outline : to add contact in outlook
    When user navigates to add contact in Outlook page
    And user adds contact first name <first_name> and last name <last_name>
    And user adds contacts mail id <mail_id>
    And user addds contact phone number <phone_number>
    And user adds the new contact created
    Then user verifies created contact name in list

    Examples:
    |first_name|last_name|mail_id|phone_number|
    |abc       |abc      |abc@gmail.com|445566|

