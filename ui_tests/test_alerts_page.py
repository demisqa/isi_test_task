import time
from selenium.webdriver.remote.webdriver import WebDriver
from pages.alerts_page import AlertsPage

class TestAlertsPage:
    
    def test_add_alert_with_valid_data(self, browser : WebDriver, teardown_new_alert):
        alerts_page = AlertsPage(browser, browser.current_url)
        alerts_page.go_to_alert_tab()
        alerts_page.add_alert(valid_data=True)
        alerts_page.should_be_success_add_message()
        alerts_page.check_alert(isChanged=False)

    def test_add_alert_with_invalid_data(self, browser : WebDriver):
        alerts_page = AlertsPage(browser, browser.current_url)
        alerts_page.go_to_alert_tab()
        alerts_page.add_alert(valid_data=False)
        alerts_page.check_empty_alert_table(valid_data=False)

    def test_update_existed_alert_with_valid_data(self, browser : WebDriver, teardown_existing_alert):
        alerts_page = AlertsPage(browser, browser.current_url)
        alerts_page.go_to_alert_tab()
        alerts_page.add_alert(valid_data=True)
        alerts_page.update_alert()
        alerts_page.should_be_success_update_message()
        alerts_page.check_empty_alert_table(valid_data=True)
        alerts_page.check_alert(isChanged=True)
