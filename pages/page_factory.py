"""
This modules defines the Page factory class for all the Page objects
"""

import weakref

# Outlook_Assignment web Portal page object grouping
from Outlook_UI.pages.LoginPage import *
from Outlook_UI.pages.MainPage import*



class PageFactory(object):
    """
    This class defines page objects as factory class attributes.
    """

    def __init__(self, webdriver):
        self.driver = webdriver
        self._page = Page(weakref.proxy(self))

    def __is_on_valid_page(self, pageclass):
        if pageclass.page_title == self._page.get_page_title():
            return pageclass
        else:
            raise Exception("PageNotFound: Application not on {0}".format(pageclass.page_title))

    @property
    def login_page(self):
        """This property will return login page"""
        return Loginpage(weakref.proxy(self))

    @property
    def main_page(self):
        """This property will return the dashboard page"""
        return Mainpage(weakref.proxy(self))



