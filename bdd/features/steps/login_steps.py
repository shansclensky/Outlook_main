import allure
import logging
import time
from Outlook_UI import config
from behave import when, then, step
from Outlook_UI.test_scripts.bdd.behave_utils import strip_behave_params
from allure_commons.types import AttachmentType

logger = logging.getLogger(config.APP_NAME)

@when(u"I login to the QA portal")
def i_login_to_the_QA_portal(context):
    logger.info("Login to QA Portal")
    print("Login to QA Portal")
    context.page_factory.base_page.go_to_url(config.HOST)
    # context.page_factory.base_page.go_to_url(config.HOST_QA)
    context.page_factory.login_page.login_user(config.USERNAME_IL_QA, config.PASSWORD_QA)


@when(u"I login to the QA portal with {username} {password}")
def i_login_to_the_tenant_portal(context, **kwargs):
    if context.table is not None:
        for each_row in context.table.rows:
            context.page_factory.base_page.go_to_url(config.HOST_QA)
            context.page_factory.login_page.login_user(each_row[0], each_row[1])

    else:
        context.page_factory.base_page.go_to_url(config.HOST_QA)
        context.page_factory.login_page.login_user(strip_behave_params(kwargs['username']),
                                                   strip_behave_params(kwargs['password'], lower_case=False))