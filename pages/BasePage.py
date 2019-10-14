from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    IMPLICIT_WAIT_TIME = 10

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

