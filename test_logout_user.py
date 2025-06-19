from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTER_BUTTON, ENTER_BUTTON, EXIT_BUTTON, EMAIL_AREA, PASS_AREA, AVATAR_BUTTON

def test_logout_user(driver):

    email = "storozhenko_20@gmail.com"
    password = "gfhjkm"
    wait = WebDriverWait(driver, 10)

    #нажатие кнопки "Вход и регистрация"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    #Ввод email
    wait.until(EC.presence_of_element_located(EMAIL_AREA)).send_keys(email)
    #ввод пароля
    driver.find_element(*PASS_AREA).send_keys(password)
    #Нажимаем кнопку "Войти"
    driver.find_element(*ENTER_BUTTON).click()

    #нажимаем на кнопку "Выйти"
    wait.until(EC.element_to_be_clickable(EXIT_BUTTON)).click()

    #ждем появления кнопки "Вход и регистрация"
    login_button = wait.until(EC.visibility_of_element_located(REGISTER_BUTTON))

    #Убеждаемся, что кнопка "Вход и регистрация" видна, а аватар исчез
    assert login_button.is_displayed()
    avatar_present = driver.find_elements(*AVATAR_BUTTON)
    assert len(avatar_present) == 0