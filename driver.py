class WebDriver (object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def open_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
