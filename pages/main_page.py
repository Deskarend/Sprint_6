import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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

    def _check_text_answer_of_question(self, answer_locator, expected_answer):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))

        actual_answer = self.driver.find_element(*answer_locator).text

        assert expected_answer == actual_answer, f'Ожидаемый ответ {expected_answer}, фактический — f{actual_answer}'

    @allure.step('Нажать на вопрос "Сколько это стоит? И как оплатить?"')
    def click_on_payment_question(self):
        self._click_on_something(self.PAYMENT_QUESTION)

    @allure.step('Проверка соответствия текста — "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def check_text_answer_of_payment_question(self):
        expected_answer = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        self._check_text_answer_of_question(self.PAYMENT_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_on_quantity_question(self):
        self._click_on_something(self.QUANTITY_QUESTION)

    @allure.step('Проверка соответствия текста — "Пока что у нас так: один заказ — один самокат. Если хотите \
                                    покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    def check_text_answer_of_quantity_question(self):
        expected_answer = ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                           "можете просто сделать несколько заказов — один за другим.")
        self._check_text_answer_of_question(self.QUANTITY_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Как рассчитывается время аренды?"')
    def click_on_calculation_rental_question(self):
        self._click_on_something(self.CALCULATION_RENTAL_QUESTION)

    @allure.step('Проверка соответствия текста — "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат \
    8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли \
    самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    def check_text_answer_of_calculation_rental_question(self):
        expected_answer = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт "
                           "времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли "
                           "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")
        self._check_text_answer_of_question(self.CALCULATION_RENTAL_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def click_on_order_for_today_question(self):
        self._click_on_something(self.ORDER_FOR_TODAY_QUESTION)

    @allure.step('Проверка соответствия текста — "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')
    def check_text_answer_of_order_for_today_question(self):
        expected_answer = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        self._check_text_answer_of_question(self.ORDER_FOR_TODAY_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_on_renew_or_return_question(self):
        self._click_on_something(self.RENEW_OR_RETURN_QUESTION)

    @allure.step('Проверка соответствия текста — "Пока что нет! Но если что-то срочное — всегда можно позвонить '
                 'в поддержку по красивому номеру 1010."')
    def check_text_answer_of_renew_or_return_question(self):
        expected_answer = ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому "
                           "номеру 1010.")
        self._check_text_answer_of_question(self.RENEW_OR_RETURN_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_on_charging_question(self):
        self._click_on_something(self.CHARGING_QUESTION)

    @allure.step('Проверка соответствия текста — "Самокат приезжает к вам с полной зарядкой. Этого хватает на '
                 'восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    def check_text_answer_of_charging_question(self):
        expected_answer = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если "
                           "будете кататься без передышек и во сне. Зарядка не понадобится.")
        self._check_text_answer_of_question(self.CHARGING_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Можно ли отменить заказ?"')
    def click_on_cancel_order_question(self):
        self._click_on_something(self.CANCEL_ORDER_QUESTION)

    @allure.step('Проверка соответствия текста — "Да, пока самокат не привезли. Штрафа не будет, объяснительной '
                 'записки тоже не попросим. Все же свои."')
    def check_text_answer_of_cancel_order_question(self):
        expected_answer = ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
                           "Все же свои.")
        self._check_text_answer_of_question(self.CANCEL_ORDER_ANSWER, expected_answer)

    @allure.step('Нажать на вопрос "Я живу за МКАДом, привезёте?"')
    def click_on_mkad_question(self):
        self._click_on_something(self.MKAD_QUESTION)

    @allure.step('Проверка соответствия текста — "Да, обязательно. Всем самокатов! И Москве, и Московской '
                 'области."')
    def check_text_answer_of_mkad_question(self):
        expected_answer = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        self._check_text_answer_of_question(self.MKAD_ANSWER, expected_answer)

    @allure.step('Нажать на кнопку "Заказать" в центре')
    def click_on_order_button_in_middle(self):
        self._go_to_element(self.BUTTON_ORDER_IN_MIDDLE)
        self._click_on_something(self.BUTTON_ORDER_IN_MIDDLE)
