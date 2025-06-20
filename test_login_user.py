from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTER_BUTTON, PASS_AREA, AVATAR_BUTTON, EMAIL_AREA, ENTER_BUTTON, TEXT_LOG_USER

def test_login_user(driver):

    email = "storozhenko_20@gmail.com"
    password = "gfhjkm"
    wait = WebDriverWait(driver, 10)

    #нажатие кнопки "Вход и регистрация"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    #Заполняем форму авторизации
    wait.until(EC.presence_of_element_located(EMAIL_AREA)).send_keys(email)

    # ввод email
    driver.find_element(*PASS_AREA).send_keys(password)

    #Нажимаем кнопку "Войти"
    driver.find_element(*ENTER_BUTTON).click()

    #проверка наличия аватара
    avatar = wait.until(EC.visibility_of_element_located(AVATAR_BUTTON))
    assert avatar.is_displayed()

    #проверка имени пользователя
    element = wait.until(EC.visibility_of_element_located(TEXT_LOG_USER))
    assert element.text == 'User.'

    #проверка текущего URL
    cureent_url = driver.current_url
    assert cureent_url == 'https://qa-desk.stand.praktikum-services.ru/login'
