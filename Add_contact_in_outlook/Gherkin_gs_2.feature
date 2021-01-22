 Feature: add contact  in outlook

  Background: User logs into outlook web application
    Given user logged in to outlook

  Scenario Outline : to add contact
    When user navigates to add contact in Outlook page
    And user adds contact first name <first_name> and last name <last_name>
    And user adds contacts mail id <mail_id>
    And user addds contact phone number <phone_number>
    And user adds the new contact created
    Then user verifies created contact name in list

    Examples:
    |first_name|last_name|mail_id|phone_number|
    |abc       |abc      |abc@outlook.com|445566|
