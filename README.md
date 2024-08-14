# Sprint_6
## Проект автоматизации тестирования сервиса «Яндекс.Самокат»
1. Основа для написания автотестов — фреймворк pytest и библиотека selenium.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v.
4. Команда для генерирования Allure-отчета  — pytest tests.py --alluredir=allure_results.
5. Команда для формирования отчёта в формате веб-страницы — allure serve allure_results