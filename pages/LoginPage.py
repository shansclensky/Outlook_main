import time

from Outlook_Assignment.Outlook_UI.pages.page import Page
from core.interface.locust_rest_client import Singleton

class Loginpage(Page, metaclass=Singleton):

    __metaclass__ = Singleton

    @property
    def login_button(self):
        return self.driver.find_element_by_css_selector(".btn-group.btn-group-toggle")

    @property
    def username_field(self):
        return self.driver.find_element_by_xpath("//*[@id=\"userNameId\"]/input")

    @property
    def password_field(self):
        return self.driver.find_element_by_xpath("//*[@id=\"pwdId\"]/input")

    @property
    def add_username_field(self):
        return self.driver.find_element_by_css_selector("//input[@name='loginfmt']")

    @property
    def click_next_button(self):
        return self.driver.find_element_by_css_selector(".button.primary")

    @property
    def add_password_field(self):
        return self.driver.find_element_by_css_selector(".input.text-box")

    @property
    def add_account_button(self):
        return self.driver.find_element_by_css_selector("#otherTileText")

    @property
    def signin_button(self):
        return self.driver.find_element_by_css_selector(".btn-group.btn-group-toggle")

    @property
    def reduce_signin(self):
        return self.driver.find_element_by_css_selector("#idBtn_Back")

    def click_logout(self):
        self.driver.find_element_by_css_selector("#profile-menu").click()
        self.driver.find_element_by_xpath("//span[text()='Logout']")[0].click()
        self.driver.find_element_by_css_selector(".btn.btn-primary.btn-sm").click()
        self.driver.find_element_by_css_selector(".tile-img").click() #which account to sign out from - for noe the first image have to pass the name as well later


    def login_user(self, username=None, password=None):
        self.login_button.click()
        self.add_account_button.click()
        self.add_username_field.send_keys(username)
        self.click_next_button.click()
        self.add_password_field.send_keys(password)
        self.signin_button.click()
        self.reduce_signin.click()
        time.sleep(5)

