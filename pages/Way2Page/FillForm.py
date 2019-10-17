from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ..BasePage import BasePage

class FillForm(BasePage):

    def register(self):
        _name_selector = (By.NAME, "name")
        _phone_selector = (By.NAME, "phone")
        _email_selector = (By.NAME, "email")
        _country_selector = (By.NAME, "country")
        _city_selector = (By.NAME, "city")
        _username_selector = (By.CSS_SELECTOR, "#load_form > fieldset:nth-child(10) > input[type=text")
        _password_selector = (By.CSS_SELECTOR, "#load_form > fieldset:nth-child(11) > input[type=password]")
        _submit_selector = (By.CSS_SELECTOR, "#load_box #load_form > div > div.span_1_of_4 > input")

        self.type_text(_name_selector, "TesterName")
        self.type_text(_phone_selector, "0722222222")
        self.type_text(_email_selector, "testiasmina-iasmina@mailinator.com")
        select_element = Select(self.get_element(_country_selector))
        select_element.select_by_visible_text("Romania")
        self.type_text(_city_selector, "Timisoara")
        self.type_text(_username_selector, "ztester12345")
        self.type_text(_password_selector, "1qazxsw2")
        self.click(_submit_selector)

    def sign_in(self):
        _signin_selector = (By.CSS_SELECTOR, "#load_box #load_form > div > div.span_3_of_4 > p > a")
        _username_selector = (By.CSS_SELECTOR, "#login #load_form > fieldset:nth-child(5) > input[type=text]")
        _password_selector = (By.CSS_SELECTOR, "#login #load_form > fieldset:nth-child(6) > input[type=password]")
        _login_selector = (By.CSS_SELECTOR, "#login  #load_form > div > div.span_1_of_4 > input")

        self.click(_signin_selector)
        self.type_text(_username_selector, "ztester12345")
        self.type_text(_password_selector, "1qazxsw2")
        self.click(_login_selector)

    def open_date_picker(self):
        _widget_selector = (By.CSS_SELECTOR, "#toggleNav > li:nth-child(3) > a")
        _datepicker_selector = (By.CSS_SELECTOR, "#toggleNav > li:nth-child(3) > ul > li:nth-child(3) > a")

        self.hover(_widget_selector)
        self.click(_datepicker_selector)

    def navigate_to_format_date(self):
        _format_date = (By.CSS_SELECTOR, "#wrapper > div > div.container.responsive-tabs-default > div.internal_navi > ul > li:nth-child(4) > a")

        self.click(_format_date)

    def select_current_day(self):
        _datepicker_selector = (By.CSS_SELECTOR,  "#datepicker")
        _current_day_selector = (By.CSS_SELECTOR, "#ui-datepicker-div > table > tbody > tr:nth-child(3) > td.ui-datepicker-days-cell-over.ui-datepicker-today > a")

        self.driver.switch_to.frame(3)
        self.click(_datepicker_selector)
        self.click(_current_day_selector)

    def select_iso(self):
        _iso_format_selector = (By.CSS_SELECTOR, "#format")

        select_element = Select(self.get_element(_iso_format_selector))
        select_element.select_by_visible_text("ISO 8601 - yy-mm-dd")

    def validate_date(self):
        _datepicker_selector = (By.CSS_SELECTOR, "#datepicker")

        date_picker = self.get_element(_datepicker_selector)
        return date_picker.get_attribute('value')
