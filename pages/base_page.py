import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = None
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class,'LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class,'LogoYandex')]")
    BUTTON_ORDER_IN_HEADER = (By.XPATH, ".//div[contains(@class,'Header')]//button[contains(text(),'Заказать')]")

    def __init__(self, driver):
        self.driver = driver

    def _open_the_page(self):
        self.driver.get(self.URL)

    def _go_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _click_on_something(self, something_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(something_locator))
        self.driver.find_element(*something_locator).click()

    @allure.step('Нажать на кнопку "Заказать" в футоре')
    def click_on_order_button_in_header(self):
        self._click_on_something(self.BUTTON_ORDER_IN_HEADER)

    @allure.step('Нажать на лого "Самокат" ')
    def click_on_logo_scooter(self):
        self._click_on_something(self.LOGO_SCOOTER)

    @allure.step('Нажать на лого "Яндекс" ')
    def click_on_logo_yandex(self):
        self._click_on_something(self.LOGO_YANDEX)

    @allure.step('Проверка перехода на страницу оформления заказа')
    def check_is_it_order_page(self):
        assert EC.url_contains('order'), f'Переход не на страницу оформления заказа'

    @allure.step('Проверка перехода на страницу оформления заказа')
    def check_is_it_main_page(self):
        from pages.main_page import MainPage
        assert EC.url_to_be(MainPage.URL), f'Переход не на главную страницу'

    @allure.step('Проверка перехода на страницу Дзена')
    def check_is_it_dzen_page(self):
        current_url = self.driver.current_url
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert WebDriverWait(self.driver, 5).until(EC.url_changes(current_url))
        assert EC.url_contains('dzen.ru'), "Переход не на страницу дзена"
