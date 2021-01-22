Feature: Login functionality for Outlook

  Scenario Outline: To login to the QA portal and view event list successfully
    When User navigate to the Outlook page
    And User enter <username> and <password>
    Then User logged in to outlook mail

    Examples:
     |username|password|
     |abc     |abc     |

