import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    browser.implicitly_wait(5)
    button = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert button > 0, 'Button does not found'
