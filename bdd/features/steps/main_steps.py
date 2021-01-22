import logging
import time
from Outlook_UI import config
from behave import when, then, step
from Outlook_UI.test_scripts.bdd.behave_utils import strip_behave_params


logger = logging.getLogger(config.APP_NAME)
from Outlook_UI import config

logger = logging.getLogger(config.APP_NAME)

@when(u"user navigates to the Outlook page")
def user_navigate_to_outlook_page(context):
    logger.info("navigating to mail section")
    print("navigating to outlook inbox section")
    context.page_factory.main_page.compose_mail()

@when(u"user adds recipient address with {recipient_address}")
def user_add_receipient_address(context, **kwargs):
    logger.info("adding recipient address")
    recipient_address = strip_behave_params(kwargs["recipient_address"], lower_case=False).strip()
    print("navigating to Events section")
    context.page_factory.main_page.add_recipients(recipient_address)

@when(u"user adds mail contents with {mail_subject} {mail_body}")
def user_add_receipient_address(context, **kwargs):
    mail_subject = strip_behave_params(kwargs["subject_line"], lower_case=False).strip()
    mail_body = strip_behave_params(kwargs["mail_body"], lower_case=False).strip()
    print("subject line is  {0}".format(mail_subject))
    logger.info("subject line is : {} ".format(mail_subject))
    print("mail content is  {0}".format(mail_body))
    logger.info("mail content is : {} ".format(mail_body))
    context.page_factory.main_page.add_content(mail_subject,mail_body)

@when(u'user sends the mail')
def user_sends_mail(context):
    context.page_factory.main_page.send_mail()


