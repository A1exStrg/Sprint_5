from selenium.webdriver.common.by import By


#кнопки
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход')]") #вход и регистрация
NO_ACC_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']") #нет аккаунта
EMAIL_AREA = (By.XPATH, "//input[@placeholder='Введите Email']")#поле ввода пароля
PASS_AREA = (By.XPATH, "//input[@placeholder='Пароль']")
PASS_AREA_REP = (By.XPATH, "//input[@placeholder='Повторите пароль']")
CREATE_ACC_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']") #кнопка создать аккаунт
AVATAR_BUTTON = (By.CLASS_NAME, "circleSmall")
ACC_USER_BUTTON = (By.XPATH, "//h3[text()='User.']")
ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
EXIT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
NEW_ADVERTISMENT_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
PUBLIC_POST_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
MODAL_WINDOW = (By.CLASS_NAME, "homePage_modal__zSdUB") #модельное окно
EMAIL_FORM_AREA = (By.XPATH, "//input[@placeholder='Название']") # форма ввода пароля
TEXT_ADV_FORM = (By.XPATH, "//textarea[@placeholder='Описание товара']") #форма описания товара
COST_FORM = (By.XPATH, "//input[@placeholder='Стоимость']")# форма ввода цены товара
DROP_DOWN_MENU_CATEGORY = (By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1 ")
CHOOSE_CATEGORY = (By.XPATH, "//span[text()='Книги']")
DROP_DOWN_MENU_CITY = (By.XPATH, '(//button[contains(@class, "dropDownMenu_arrowDown__pfGL1")])[2]')
CHOOSE_CTY = (By.XPATH, "//span[text()= 'Казань']")
RADIO_BUTTON = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")
PUBLIC_ADV_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
ADVERTISMENT_FORM = (By.XPATH, "//h2[contains(text(), 'Тестовое объявление')]")
MODAL_WINDOW_REGISTRATION = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
TEXT_ERROR = (By.XPATH, "//span[contains(text(), 'Ошибка')]")
LIST_ERRORS = (By.CLASS_NAME, "input_inputError__fLUP9")
TEXT_LOG_USER = (By.XPATH, "//h3[text()='User.']")