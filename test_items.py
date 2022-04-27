
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button(browser):
    browser.get(link)
    find_btn = browser.find_elements_by_css_selector('form[id="add_to_basket_form"] .btn-primary')
    assert len(find_btn) > 0, "Такой кнопки нет на странице"