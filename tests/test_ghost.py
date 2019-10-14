from ..pages.GhostPage.LandingPage import LandingPage

def test_open_ghost_site(selenium, variables):

    landing_page = LandingPage(selenium, variables, open_url=True)
    assert True
