import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    btn1 = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn1)

    time.sleep(30)

    assert btn1 is not None, "Кнопка добавления в корзину не найдена"