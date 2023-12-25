from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser : WebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.presence_of_element_located((by, value)))
        except (TimeoutException):
            print("Element not found")
            return False
        return True
    
    def is_not_element_present(self, by, value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            return True
        return False 
    
    # def is_disappeared(self, by, value, timeout=4):
    #     try:
    #         WebDriverWait(self.browser, timeout, 1, TimeoutException).\
    #             until_not(EC.presence_of_element_located((by, value)))
    #     except TimeoutException:
    #         return False
    #     return True
