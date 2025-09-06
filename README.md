## Дипломный проект. Задание 2: API Stellar Burgers
<hr>

## Студент: Курохтин Дмитрий

## <h>Когорта: 26</h>
<hr>

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

api/
├── __init__.py          # делает директорию python пакетом
├── user_api.py          # методы API для работы с пользователем
├── order_api.py         # методы API для работы с заказами
data/
├── __init__.py          # делает директорию python пакетом  
├── user_data.py         # данные и генераторы для пользователей
├── order_data.py        # данные и генераторы для заказов
├── urls.py              # эндпоинты API Stellar Burgers
tests/
├── __init__.py          # делает директорию python пакетом
├── test_create_user.py  # 3 теста создания пользователя
├── test_create_order.py # 5 тестов создания заказа
├── test_login_user.py   # 2 теста логина пользователя
.gitignore               # игнорируемые файлы (логи, кэш и т.д.)
README.md               # документация проекта
conftest.py             # фикстуры pytest (создание/удаление пользователей)
pytest.ini              # конфигурация pytest и allure
requirements.txt        # зависимости: pytest, requests, allure-pytest

Перед началом работы с репозиторием требуется установить зависимости:

pip install -r requirements.txt
Запустить тесты:

pytest tests --alluredir=allure_results
Просмотреть отчет о тестировании:

allure serve allure_results