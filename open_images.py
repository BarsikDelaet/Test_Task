from PageObject.locators import Locator
from selenium.webdriver.common.by import By
from PageObject.Page.driver import WebDriver
from time import sleep


class OpenImg(WebDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_img = driver.find_element(By.CSS_SELECTOR, Locator.window_img)
        self.next = driver.find_element(By.CSS_SELECTOR, Locator.next_button)
        self.back = driver.find_element(By.CSS_SELECTOR, Locator.back_button)

    def work_img(self):  # Переключение между картинками
        link = self.open_img.text
        self.next.click()
        sleep(1.5)
        assert link != self.open_img.text, 'Картинка не поменялась после нажатия кнопки "Вперед"'
        self.back.click()
        sleep(1.5)
        assert link == self.open_img.text, 'Вернулась не изначальная картинка после нажатия кнопки "Назад"'
