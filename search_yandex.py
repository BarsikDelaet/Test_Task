from PageObject.locators import Locator
from PageObject.Page.driver import WebDriver
from selenium.webdriver.common.by import By


class Yandex(WebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.link = driver.find_elements(By.CSS_SELECTOR, Locator.link)

    def check_link(self, tensor_link: str):  # Проверка первых 5 ссылок
        flag = False
        for i in range(5):
            print('Ссылка №{}: {}'.format(i+1, self.link[i].text))
            if self.link[i].text == tensor_link:
                flag = True
        assert flag, "В первых 5 ссылка не найдена искомая."
        print("\nВ списке есть ссылка 'tensor.ru'.\n")
