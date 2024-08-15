import allure
from pages.main_page import MainPage


class TestFooter:
    @allure.title('Проверка вопроса "Сколько это стоит? И как оплатить?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Сутки — 400 рублей. Оплата курьеру \
                                                                                            — наличными или картой."')
    def test_payment_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_question()

        base_page.check_text_answer_of_payment_question()

    @allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Пока что у нас так: один заказ \
        — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    def test_quantity_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_quantity_question()

        base_page.check_text_answer_of_quantity_question()

    @allure.title('Проверка вопроса "Как рассчитывается время аренды?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Допустим, вы оформляете заказ на '
                        '8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, '
                        'когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда '
                        'закончится 9 мая в 20:30."')
    def test_calculation_rental_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_calculation_rental_question()

        base_page.check_text_answer_of_calculation_rental_question()

    @allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Только начиная с завтрашнего дня. \
                                                                                        Но скоро станем расторопнее."')
    def test_order_for_today_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_order_for_today_question()

        base_page.check_text_answer_of_order_for_today_question()

    @allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Пока что нет! Но если что-то '
                        'срочное — всегда можно позвонить в поддержку по красивому номеру 1010."')
    def test_renew_or_return_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_renew_or_return_question()

        base_page.check_text_answer_of_renew_or_return_question()

    @allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Самокат приезжает к вам с полной '
                        'зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                        'Зарядка не понадобится."')
    def test_charging_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_charging_question()

        base_page.check_text_answer_of_charging_question()

    @allure.title('Проверка вопроса "Можно ли отменить заказ?"')
    @allure.description('При нажатии на вопрос открывается соответствующий текст — "Да, пока самокат не привезли. '
                        'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."')
    def test_cancel_order_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_cancel_order_question()

        base_page.check_text_answer_of_cancel_order_question()

    @allure.title('Проверка вопроса "Я жизу за МКАДом, привезёте?"')
    @allure.description('Да, обязательно. Всем самокатов! И Москве, и Московской области."')
    def test_mkad_question(self, driver):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_mkad_question()

        base_page.check_text_answer_of_mkad_question()
