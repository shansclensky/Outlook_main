import time

from Outlook_Assignment.Outlook_UI.pages.page import Page
from core.interface.locust_rest_client import Singleton

class Mainpage(Page, metaclass=Singleton):

    __metaclass__ = Singleton

    def compose_mail(self):
        compose = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/header/div[2]/div/i')
        compose.click()
        time.sleep(5)

    def add_recipients(self, recipient_address=None):
        # email address of the recipient
        to_recipent = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[1]/span/input')
        to_recipent.send_keys(recipient_address)
        time.sleep(2)

    def add_content(self, mail_subject=None,mail_body=None):
        #subject of the mail to be sent
        subject_id = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/input')
        subject_id.send_keys(mail_subject)
        time.sleep(2)
        #mail content to be sent
        mail_content = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div[2]')
        mail_content.send_keys(mail_body)
        time.sleep(2)

    def send_mail(self):
        #send the composed mail
        send_button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/header/i[2]')
        send_button.submit()
