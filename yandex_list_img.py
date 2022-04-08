from PageObject.locators import Locator
from selenium.webdriver.common.by import By
from PageObject.Page.driver import WebDriver


class YandexListImages(WebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.link_img = driver.find_element(By.CSS_SELECTOR, Locator.link_img)
        self.name_img = driver.find_element(By.CSS_SELECTOR, Locator.name_img)

    def check_url(self, img_url: str):#Проверка url Яндекс Картинки
        url = self.driver.current_url
        assert url == img_url, 'Вход на неверную стр.'
        print('Открылось окно Яндекс картинки.\n')

    def open_img(self) -> str:  # Запоминаем название первой категории картинок
        name = self.name_img.text
        self.link_img.click()
        print('Название категории: {}\n'.format(name))
        return name
