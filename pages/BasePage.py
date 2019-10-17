from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    _IMPLICIT_WAIT_TIME = 10

    def __init__(self, driver, variables, open_url=False):
        self.variables = variables
        self.url = self.variables['url']
        self.driver = driver
        self.driver.maximize_window()
        if open_url:
            self.driver.get(self.url)
        self.confirm_page()

    def confirm_page(self):
        pass

    def click(self, selector):
        element = WebDriverWait(self.driver, self._IMPLICIT_WAIT_TIME
                                ).until(
            ec.element_to_be_clickable(selector)
        )
        element.click()

    def get_element(self, selector):
        element = WebDriverWait(
            self.driver,
            self._IMPLICIT_WAIT_TIME
        ).until(
            ec.presence_of_element_located(selector)
        )
        return element

    def type_text(self, selector, text):
        element = self.get_element(selector)
        element.click()
        element.clear()
        element.send_keys(text)
        WebDriverWait(
            self.driver,
            self._IMPLICIT_WAIT_TIME
        ).until(
            ec.text_to_be_present_in_element_value(selector, text)
        )

    def hover(self, selector):
        element = self.get_element(selector)
        ac = ActionChains(self.driver)
        ac.move_to_element(element)
        ac.perform()
