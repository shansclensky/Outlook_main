Feature: Compose mail in outlook

Background: User logs into outlook web application
    Given user logged in to outlook

  Scenario Outline: To compose mail 
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail
    Then user verifies mail sent successfully // yet to be implemented


    Examples:
    |recipient_address|subject_line|mail_body|
    |abc@outlook.com   | sample mail | mail to check outlook functionality|



#UserFlow scenarios listed below:

Background: User logs into outlook web application
    Given user logged in to outlook

  Scenario Outline: To compose mail with to address and subject
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds mail contents with <subject_line>
    And user sends the mail

    Examples:
    |recipient_address|subject_line|
    |abc@outlook.com   | sample mail |


  Scenario Outline: To compose mail with to address, subject and mail body
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail
    Then user verifies mail sent successfully // yet to be implemented


    Examples:
    |recipient_address|subject_line|mail_body|
    |abc@outlook.com   | sample mail | mail to check outlook functionality|


  Scenario Outline: To compose mail with to address ,cc, subject and mail body
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds cc recipient address with <cc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail



    Examples:
    |recipient_address|cc_recipient_address|subject_line|mail_body|
    |abc@outlook.com   | cc@outlook.com              |sample mail | mail to check outlook functionality|

  Scenario Outline: To compose mail with to address ,bcc, subject and mail body
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds bcc recipient address with <bcc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail



    Examples:
    |recipient_address|bcc_recipient_address|subject_line|mail_body|
    |abc@outlook.com   | bcc@outlook.com              |sample mail | mail to check outlook functionality|


  Scenario Outline: To compose mail with to address ,bcc,cc, subject and mail body
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds cc recipient address with <cc_recipient_address>
    And user adds bcc recipient address with <bcc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user sends the mail



    Examples:
    |recipient_address|cc_recipient_address|bcc_recipient_address|subject_line|mail_body|
    |abc@outlook.com   | cc@outlook.com    |bcc@outlook.com              |sample mail | mail to check outlook functionality|




  Scenario Outline: To compose mail with to address ,bcc,cc, subject and mail body and attachment
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds cc recipient address with <cc_recipient_address>
    And user adds bcc recipient address with <bcc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user adds attachment file <attachment> and <path to attachment>
    And user sends the mail



    Examples:
    |recipient_address|cc_recipient_address|bcc_recipient_address|subject_line|mail_body|attachment|path to attachment|
    |abc@outlook.com   | cc@outlook.com    |bcc@outlook.com              |sample mail | mail to check outlook functionality|sample_file|path_users_docs|



  Scenario Outline: To compose mail with to address ,bcc,cc, subject and mail body and image
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds cc recipient address with <cc_recipient_address>
    And user adds bcc recipient address with <bcc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
    And user adds attachment file <image_files> and <path to image_files>
    And user sends the mail



    Examples:
    |recipient_address|cc_recipient_address|bcc_recipient_address|subject_line|mail_body|image_files|path to image_files|
    |abc@outlook.com   | cc@outlook.com    |bcc@outlook.com              |sample mail | mail to check outlook functionality|sample_file|path_users_docs|



  Scenario Outline: To compose mail with to address ,bcc,cc, subject and mail body and image
    When user navigates to the Outlook page
    And user adds recipient address with <recipient_address>
    And user adds cc recipient address with <cc_recipient_address>
    And user adds bcc recipient address with <bcc_recipient_address>
    And user adds mail contents with <subject_line> <mail_body>
       And user adds attachment file <attachment> and <path to attachment>
    And user adds attachment file <image_files> and <path to image_files>
    And user sends the mail



    Examples:
    |recipient_address|cc_recipient_address|bcc_recipient_address|subject_line|mail_body|attachment|image_files|path to attachment|path to image_files|
    |abc@outlook.com   | cc@outlook.com    |bcc@outlook.com              |sample mail | mail to check outlook functionality|sample_file|sample_file_2|path_users_docs|path_users_images|

