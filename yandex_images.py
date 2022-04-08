from PageObject.locators import Locator
from selenium.webdriver.common.by import By
from PageObject.Page.driver import WebDriver


class YandexImg(WebDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_line = driver.find_element(By.CSS_SELECTOR, Locator.search_line)
        self.search_img = driver.find_element(By.CSS_SELECTOR, Locator.search_img)

    def check_img(self, name_img: str):  # Проверка на название категории и открытие перой фотографии
        assert self.search_line.get_attribute('value') == name_img, 'В поиске не верный текст.'
        print("Открылась выбранная категория.{}".format(self.search_line.text))
        self.search_img.click()
