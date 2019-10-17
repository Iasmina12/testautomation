from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..BasePage import BasePage

class CommunityForumPage(BasePage):

    _search_button_selector =(By.ID, 'search-button')
    _search_input_selector = (By.ID, 'search-term')
    _search_result_selector =(By.CSS_SELECTOR, 'div.search-results > div.ember-view > div:nth-child(2) > div.fps-topic > div.topic > a')

    def search_text(self, term):
        self.click(self._search_button_selector)
        self.type_text(self._search_input_selector, term)
        self.get_element(self._search_input_selector).send_keys(Keys.ENTER)

    def click_result(self):
        self.click(self._search_result_selector)




