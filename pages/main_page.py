import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"
    SCOOTER_IMG = (By.XPATH, ".//img[contains(@src,'scooter.png')]")
    HOME_PAGE_DIV = (By.XPATH, ".//div[contains(@class,'HomePage')]")
    FOOTER = (By.XPATH, ".//div[contains(@class,'FourPart')]")
    PAYMENT_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-0')]")
    PAYMENT_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-0')]")
    QUANTITY_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-1')]")
    QUANTITY_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-1')]")
    CALCULATION_RENTAL_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-2')]")
    CALCULATION_RENTAL_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-2')]")
    ORDER_FOR_TODAY_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-3')]")
    ORDER_FOR_TODAY_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-3')]")
    RENEW_OR_RETURN_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-4')]")
    RENEW_OR_RETURN_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-4')]")
    CHARGING_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-5')]")
    CHARGING_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-5')]")
    CANCEL_ORDER_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-6')]")
    CANCEL_ORDER_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-6')]")
    MKAD_QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-7')]")
    MKAD_ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-7')]")
    BUTTON_ORDER_IN_MIDDLE = (By.XPATH, ".//div[contains(@class,'FinishButton')]//button")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу сайта "Яндекс.Самокат"')
    def open_the_page(self):
        self._open_the_page()

    @allure.step('Скролл страницы к футеру')
    def go_to_the_footer(self):
        self._go_to_element(self.FOOTER)

    @allure.step('Открыть страницу "Яндекс.Самокат" и скролл к футору')
    def open_the_the_page_and_go_to_the_footer(self):
        self._open_the_page()
        self.go_to_the_footer()

    @allure.step('Проверка соответствия текста ответа')
    def check_text_answer_of_question(self, answer_locator, expected_answer):
        actual_answer = self._wait_and_find_element(answer_locator).text

        assert expected_answer == actual_answer, f'Ожидаемый ответ {expected_answer}, фактический — f{actual_answer}'

    @allure.step('Нажать на соответствующий вопрос')
    def click_on_question(self):
        self._wait_and_click_on_element(self.PAYMENT_QUESTION)
