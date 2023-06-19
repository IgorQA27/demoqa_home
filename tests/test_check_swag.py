from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    assert demo_qa_page.egual_url()
    assert demo_qa_page.exist_icon()


    # browser.get('https://www.saucedemo.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, 'div.login_logo')
    #
    # if icon is None:
    #     print("элемент не найдет")
    # else:
    #     print("элемент найден")
