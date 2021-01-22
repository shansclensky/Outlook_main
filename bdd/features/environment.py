"""
This module sets up configurations for test scripts
"""
import logging
from core.utils.log_utils import logging_data
from Outlook_UI.test_scripts.bdd.step_definitions.step_definitions import StepDefinitions
from selenium import webdriver
from appium import webdriver
from behave import fixture, use_fixture
from Outlook_UI.pages.page_factory import PageFactory
from code_generator import code_gen_config
from Outlook_UI import config

logger = logging.getLogger(config.APP_NAME)

@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    #https://behave.readthedocs.io/en/latest/fixtures.html
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': config.CHROME_DOWNLOAD_PATH}

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')
    context.browser = webdriver.Chrome(executable_path=code_gen_config.CHROME_DRIVER, chrome_options=options)
    context.browser.set_page_load_timeout(90)
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)

    # for android driver below modifications
    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '4.2'
    # desired_caps['deviceName'] = 'Android Emulator'
    # desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')
     # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# This method runs before all features """
def before_all(context):
    context.log_level = context.config.userdata.get('loglevel')
    logging_data.configure_logger(context.log_level)
    context.step_definitions = StepDefinitions()
    use_fixture(selenium_browser_chrome, context)
    context.page_factory = PageFactory(context.browser)


def after_scenario(context, scenario):
    logger.info("Start of After Scenario")

    if "chrome_quit" in context.tags:
        context.browser.quit()
        context.browser = None

    close_all_tabs(context)
    context.page_factory.login.click_logout()

    logger.info("Completed scenario {0}".format(scenario.name))
    logger.info("End of After Scenario")


def after_all(context):
    # site_cleanup(context)
    if 'browser' in context:
        context.browser.quit()


def close_all_tabs(context):
    total_windows = context.page_factory.driver.window_handles
    if len(total_windows) > 1:
        index = 0
        for each_window in total_windows:
            if index > 0:
                context.page_factory.driver.switch_to_window(each_window)
                context.page_factory.driver.close()
            index += 1
        context.page_factory.base_page.switch_to_original_window()

    # if context.page_factory.driver.current_url.find("login.action") == -1:
    #     try:
    #         context.page_factory.driver.get(config.HOST)
    #         context.page_factory.base_page.logout()
    #     except Exception as e:
    #         print(e)

def before_scenario(context, scenario):
    logger.info("Started scenario {0}".format(scenario.name))
    if 'chrome' in scenario.tags:
        logger.info("Launching Chrome Browser")
        print("Launching Chrome Browser")
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': config.CHROME_DOWNLOAD_PATH}

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--incognito')
        options.add_experimental_option('prefs', prefs)

        context.browser = webdriver.Chrome(executable_path=code_gen_config.CHROME_DRIVER, chrome_options=options)
        context.browser.set_page_load_timeout(90)
        context.browser.maximize_window()
        context.browser.implicitly_wait(10)
        logger.info("Page factory initialized")
        print("Page factory initialized")
