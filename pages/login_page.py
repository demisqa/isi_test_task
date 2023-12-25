import os
from dotenv import load_dotenv
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_in_as_authorized_user(self):
        load_dotenv()
        authorized_username = os.getenv("USERNAME")
        authorized_password = os.getenv("PASSWORD")
        
        self.open()
        self.is_element_present(*LoginPageLocators.FORM_INPUTS)
        
        login = self.browser.find_element(*LoginPageLocators.LOGIN)
        login.send_keys(authorized_username)

        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys(authorized_password)

        accept_terms_checkbox = self.browser.find_element(*LoginPageLocators.ACCEPT)
        accept_terms_checkbox.click()

        log_in_button = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in_button.click()
