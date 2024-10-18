from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_page_contains_add_cart_button(browser):
    browser.get(link)
    
    time.sleep(30)
    
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    assert add_to_cart_button is not None