from selenium import webdriver
from PageObject.Page.home_yandex import Home
from PageObject.Page.search_yandex import Yandex
from PageObject.Page.yandex_list_img import YandexListImages
from PageObject.Page.yandex_images import YandexImg
from PageObject.Page.open_images import OpenImg
from PageObject.Page.driver import WebDriver
import unittest
from time import sleep


class TestTensor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://yandex.ru/')

    def test_01(self):
        driver = self.driver

        home = Home(driver)  # Пишем в поисковой text
        home.input_text("Тензор")
        home.check_suggest()
        sleep(0.5)
        home.search_text()  # Начинаем поиск по запросу

        yandex = Yandex(driver)  # Проверяем первые 5 ссылок
        yandex.check_link('tensor.ru')
        sleep(2)

    def test_02(self):
        driver = self.driver

        home = Home(driver)  # Открываем Яндекс картинки
        home.open_img()

        sleep(2)
        next_window = WebDriver(driver)  # Переключаемся на открывшееся окно
        next_window.open_new_window()

        yandex_img = YandexListImages(driver)  # Открываем первую категорию и проверяем url
        yandex_img.check_url('https://yandex.ru/images/?utm_source=main_stripe_big')
        name_img = yandex_img.open_img()
        sleep(2)

        first_img = YandexImg(driver)  # Открываем первую фотографию
        first_img.check_img(name_img)

        open_img = OpenImg(driver)  # Переключение фотографий и проверка на исполнительность
        open_img.work_img()
        sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
