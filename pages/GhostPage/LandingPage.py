from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class LandingPage(BasePage):

    _resource_selector = (By.CSS_SELECTOR, '#gatsby-focus-wrapper > div > header.gh-head.false > nav > div.gh-navbar-left > div:nth-child(4) > div > button')
    _comunity_forum_selector = (By.CSS_SELECTOR, '#gatsby-focus-wrapper > div > header.gh-head.false > nav > div.gh-navbar-left > div:nth-child(4) > div > div > ul > li:nth-child(3) > a')

    def click_resources(self):
        self.click(self._resource_selector)

    def click_community(self):
        self.click(self._comunity_forum_selector)
