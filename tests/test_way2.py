from ..pages.Way2Page.FillForm import FillForm
import time

def test_way2page (selenium, variables):

    form_variables = {
        "url": variables["way2url"]
    }

    page = FillForm(selenium, variables=form_variables, open_url=True)
    # page.register()
    page.sign_in()
    time.sleep(2)
    page.open_date_picker()
    page.navigate_to_format_date()
    page.select_current_day()
    page.select_iso()
    selected_date = page.validate_date()

    assert selected_date == time.strftime('%Y-%m-%d')
