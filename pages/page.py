import re
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Outlook_Assignment.Outlook_UI import config
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(config.APP_NAME)


class Page(object):

    def __init__(self, app):
        self._app = app

        self.driver_name = None
        self.driver_path = None
        self.implicit_wait = 30
        self.driver = self._app.driver

    def go_to_url(self, url):
        if url:
            self.driver.get(url)

    def click(self, selector=None):
        if re.match(r'^(\/\/)', selector):
            self.driver.find_element_by_xpath(xpath=selector).click()
        else:
            self.driver.find_element_by_css_selector(css_selector=selector).click()

    def close(self):
        self.driver.quit()

    def get_page_title(self):
        print("VALUE OF GET_PAGE_TITLE {0}".format(self.driver.title))
        return self.driver.title

    def logout(self):
        self.driver.find_element_by_xpath("//a[@title='Help']/preceding-sibling::span[1]/span").click()
        self.driver.find_element_by_css_selector("span[title='Log Out']").click()

    def refresh(self):
        self.driver.refresh()


