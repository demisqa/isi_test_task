from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    ACCEPT = (By.XPATH, "//input[@type='checkbox']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "button.login-button")
    FORM_INPUTS = (By.CSS_SELECTOR, "div.form-inputs")

class AlertsPageLocators:
    ALERT_TAB = (By.XPATH, "//a[@ui-sref='app.alert']")
    ADD_ALERT_BUTTON = (By.CSS_SELECTOR, "div.flex > div")
    ADD_FORM = (By.CSS_SELECTOR, "ng-form.form-style")
    ADD_FORM_NAME_INPUT = (By.XPATH, "//ng-form//input[@name='name']")
    ADD_FORM_FROM_INPUT = (By.XPATH, "//ng-form//input[@name='alert_from']")
    ADD_FORM_TO_INPUT = (By.XPATH, "//ng-form//input[@name='alert_to']")
    ADD_SEND_SMS_INPUT = (By.XPATH, "//ng-form//input[@name='send_sms' and @type='checkbox']")
    ADD_SEND_EMAIL_INPUT = (By.XPATH, "//ng-form//input[@name='send_email' and @type='checkbox']")
    ADD_CHOOSE_LOCATIONS = (By.XPATH, "//div[@ng-click='ensureAddOffice(officeItem)']")
    SAVE_BUTTON = (By.XPATH, "//button[@ng-click='saveAlert()']")
    SEARCH_INPUT = (By.XPATH, "//input[@ng-model='search.alert']")
    ALERT_TABLE_ROWS = (By.XPATH, "//tbody//tr[@ng-click='showInfo(alert.id)']")
    ALERT_TABLE_COLUMNS = (By.XPATH, "//tbody//tr[@ng-click='showInfo(alert.id)']//td")
    EMPTY_TABLE = (By.XPATH, "//tbody//tr//td")
    DELETE_BUTTON = (By.XPATH, "//button[@ng-click='deleteAlert(alertDetail.id)']")

class NotificationMessageLocators:
    ERROR_BLOCK = (By.XPATH, "//div[@id='summary']")
    NOTIFY_MESSAGE = (By.CSS_SELECTOR, "div.ui-notification > div.message")
