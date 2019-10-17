from ..pages.GhostPage.LandingPage import LandingPage
from ..pages.GhostPage.CommunityForumPage import CommunityForumPage
import time

def test_open_ghost_site(selenium, variables):

    ghost_variables = {
        "url": variables["ghosturl"]
    }
    landing_page = LandingPage(selenium, variables=ghost_variables, open_url=True)
    landing_page.click_resources()
    time.sleep(1)

    landing_page.click_community()
    community_forum_page = CommunityForumPage(selenium, variables=ghost_variables)
    community_forum_page.search_text('create new blog')
    time.sleep(2)

    community_forum_page.click_result()
    time.sleep(2)
