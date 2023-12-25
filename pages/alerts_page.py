import json
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import AlertsPageLocators
from .locators import NotificationMessageLocators

class AlertsPage(BasePage):

    def go_to_alert_tab(self):
        alert_tab = self.browser.find_element(*AlertsPageLocators.ALERT_TAB)
        alert_tab.click()
    
    def fills_load_data(self, valid_data = True):
        if valid_data:
            f = open('data/valid_add_form_data.json')
        else:
            f = open('data/invalid_add_form_data.json')
        data = json.load(f)
        f.close()
        return data[0]
    
    def fills_load_update_data(self):
        f = open("data/update_alert_data.json")
        data = json.load(f)
        f.close()
        return data[0]

    def should_not_be_error_block(self):
        assert self.is_not_element_present(*NotificationMessageLocators.ERROR_BLOCK),\
            "Block with error is presented, but should not be"
        
    def should_not_be_server_error_message(self):
        notify_messages = self.browser.find_elements(*NotificationMessageLocators.NOTIFY_MESSAGE)
        for message in notify_messages:
            assert "500 server error" not in message.text.lower(), f"Error with text {message.text}" \
                " is on the screen"
            
    def check_errors(self):
        self.should_not_be_error_block()
        self.should_not_be_server_error_message()

    def should_be_success_add_message(self):
        self.is_element_present(*NotificationMessageLocators.NOTIFY_MESSAGE)
        data = self.fills_load_data()
        success_add_message = self.browser.find_element(*NotificationMessageLocators.NOTIFY_MESSAGE)
        expected_success_add_message_text = str(data["name"] + " was created.").lower()
        actual_success_add_message_text = success_add_message.text.lower() 
        assert expected_success_add_message_text in actual_success_add_message_text, \
            f"Should be message with text '{expected_success_add_message_text}', " \
            f"but now text is '{actual_success_add_message_text}'"
        
    def should_be_unsuccess_add_message(self):
        self.is_element_present(*NotificationMessageLocators.NOTIFY_MESSAGE)
        notify_message = self.browser.find_element(*NotificationMessageLocators.NOTIFY_MESSAGE)
        expected_notify_message_text = "ensure this value is less than or equal to 212.0."
        actual_notify_message_text = notify_message.text.lower()
        assert expected_notify_message_text in actual_notify_message_text, \
            f"Should be message with text '{expected_notify_message_text}', " \
            f"but now text is '{actual_notify_message_text}'"
        
        
    def should_be_success_update_message(self):
        self.is_element_present(*NotificationMessageLocators.NOTIFY_MESSAGE)
        data = self.fills_load_update_data()
        success_update_message = self.browser.find_element(*NotificationMessageLocators.NOTIFY_MESSAGE)
        expected_success_update_message_text = str(data["name"] + " was updated.").lower()
        actual_success_update_message_text = success_update_message.text.lower() 
        assert expected_success_update_message_text in actual_success_update_message_text, \
            f"Should be message with text '{expected_success_update_message_text}', " \
            f"but now text is '{actual_success_update_message_text}'"

    def add_alert(self, valid_data : bool):
        add_allert_button = self.browser.find_element(*AlertsPageLocators.ADD_ALERT_BUTTON)
        add_allert_button.click()
        self.is_element_present(*AlertsPageLocators.ADD_FORM)
        
        if valid_data:
            data = self.fills_load_data()
        else:
            data = self.fills_load_data(valid_data=False)
        
        name_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_NAME_INPUT)
        name_input.send_keys(data['name'])

        temprature_from_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_FROM_INPUT)
        temprature_from_input.send_keys(data["from"])

        temprature_to_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_TO_INPUT)
        temprature_to_input.send_keys(data["to"])

        send_sms_input = self.browser.find_element(*AlertsPageLocators.ADD_SEND_SMS_INPUT)
        if data["sms"] == "Yes":
            self.browser.execute_script("arguments[0].click();", send_sms_input)

        send_email_input = self.browser.find_element(*AlertsPageLocators.ADD_SEND_EMAIL_INPUT)
        if data["email"] == "Yes":
            self.browser.execute_script("arguments[0].click();", send_email_input)
        
        self.is_element_present(*AlertsPageLocators.ADD_CHOOSE_LOCATIONS)
        choose_locations_input = self.browser.find_element(*AlertsPageLocators.ADD_CHOOSE_LOCATIONS)
        choose_locations_input.click()

        # self.is_disappeared(*NotificationMessageLocators.ERROR_BLOCK, timeout=5)
        self.check_errors()

        self.is_element_present(*AlertsPageLocators.SAVE_BUTTON)
        save_button = self.browser.find_element(*AlertsPageLocators.SAVE_BUTTON)
        save_button.click()

    def update_alert(self):
        data = self.fills_load_data()
        data_update = self.fills_load_update_data()

        search_input = self.browser.find_element(*AlertsPageLocators.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(data["name"])
        search_input.send_keys(Keys.ENTER)
        
        alert_table_columns = self.browser.find_elements(*AlertsPageLocators.ALERT_TABLE_COLUMNS)
        alert_table_columns[1].click()

        name_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(data_update['name'])

        temprature_from_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_FROM_INPUT)
        temprature_from_input.clear()
        temprature_from_input.send_keys(data_update["from"])

        temprature_to_input = self.browser.find_element(*AlertsPageLocators.ADD_FORM_TO_INPUT)
        temprature_to_input.clear()
        temprature_to_input.send_keys(data_update["to"])

        if data["sms"] != data_update["sms"]:
            send_sms_input = self.browser.find_element(*AlertsPageLocators.ADD_SEND_SMS_INPUT)
            self.browser.execute_script("arguments[0].click();", send_sms_input)
        
        if  data["email"] != data_update["email"]:
            send_email_input = self.browser.find_element(*AlertsPageLocators.ADD_SEND_EMAIL_INPUT)
            self.browser.execute_script("arguments[0].click();", send_email_input)
        
        # self.is_disappeared(*NotificationMessageLocators.ERROR_BLOCK, timeout=5)
        self.check_errors()

        self.is_element_present(*AlertsPageLocators.SAVE_BUTTON)
        save_button = self.browser.find_element(*AlertsPageLocators.SAVE_BUTTON)
        save_button.click()

    def check_alert(self, isChanged : bool):
        search_input = self.browser.find_element(*AlertsPageLocators.SEARCH_INPUT)
        if isChanged:
            data = self.fills_load_update_data()
        else:
            data = self.fills_load_data()
        search_input.clear()
        search_input.send_keys(data["name"])
        search_input.send_keys(Keys.ENTER)

        # self.is_disappeared(*NotificationMessageLocators.ERROR_BLOCK, timeout=5)
        self.check_errors()
        
        alert_table_rows = self.browser.find_elements(*AlertsPageLocators.ALERT_TABLE_ROWS)
        assert len(alert_table_rows) == 1, f"Count of table's rows should be 1,"\
                f"but not {len(alert_table_rows)}"
        
        alert_table_columns = self.browser.find_elements(*AlertsPageLocators.ALERT_TABLE_COLUMNS)
        alert_table_columns = alert_table_columns[1:-1]
        
        for value, column in zip(data, alert_table_columns):
            assert data[value] == column.text, f"Actual record in column {column.text},"\
                f" but should be {data[value]}"
            
    def check_empty_alert_table(self, valid_data : bool):
        if valid_data:
            data = self.fills_load_data()
        else:
            data=self.fills_load_data(valid_data=False)
        
        self.go_to_alert_tab()
        search_input = self.browser.find_element(*AlertsPageLocators.SEARCH_INPUT)
        search_input.clear()
        
        # self.is_disappeared(*NotificationMessageLocators.ERROR_BLOCK, timeout=5)
        self.check_errors()

        search_input.send_keys(data["name"])
        search_input.send_keys(Keys.ENTER)

        empty_table = self.browser.find_element(*AlertsPageLocators.EMPTY_TABLE)
        assert empty_table.is_displayed(), f"Element with text 'No result founds'" \
                " is not display"
        assert "no results found." in empty_table.text.lower(), "Table is not empty"
        
    def remove_alert(self, isChanged : bool):
        if isChanged:
            data = self.fills_load_update_data()
        else:
            data = self.fills_load_data()
        
        search_input = self.browser.find_element(*AlertsPageLocators.SEARCH_INPUT)
        search_input.clear()

        search_input.send_keys(data["name"])
        search_input.send_keys(Keys.ENTER)

        alert_table_columns = self.browser.find_elements(*AlertsPageLocators.ALERT_TABLE_COLUMNS)
        alert_table_columns[1].click()

        delete_button = self.browser.find_element(*AlertsPageLocators.DELETE_BUTTON)
        delete_button.click()
