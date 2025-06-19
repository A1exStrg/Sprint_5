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