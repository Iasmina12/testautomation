from ..pages.GhostPage.LandingPage import LandingPage
from ..pages.GhostPage.ComunityForumPage import ComunityForumPage
import time

def test_open_ghost_site(selenium, variables):

    landing_page = LandingPage(selenium, variables, open_url=True)
    landing_page.click_resources()
    time.sleep(1)
    landing_page.click_community()
    assert True
    comunity_forum_page = ComunityForumPage(selenium, variables)
    comunity_forum_page.search_text('create new blog')
    time.sleep(2)
    comunity_forum_page.click_result()
    time.sleep(2)
    assert True

