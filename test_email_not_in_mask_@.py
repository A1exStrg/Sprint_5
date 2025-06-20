from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTER_BUTTON, NO_ACC_BUTTON, CREATE_ACC_BUTTON, EMAIL_AREA, TEXT_ERROR, LIST_ERRORS

def test_email_not_in_mask(driver):

    wait = WebDriverWait(driver, 10)
    # нажатие кнопки "Вход и регистрация"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # нажатие кнопки "Нет аккаунта"
    wait.until(EC.visibility_of_element_located(NO_ACC_BUTTON)).click()

    #ввод email
    wait.until(EC.visibility_of_element_located(EMAIL_AREA)).send_keys('storozhenko_20@gmail.com')

    # Нажимаем кнопку "Создать аккаунт"
    driver.find_element(*CREATE_ACC_BUTTON).click()

    #проверка текст ошибки "ошибка"
    message = wait.until(EC.visibility_of_element_located(TEXT_ERROR))
    assert message.text == 'Ошибка'

    # Ждём появления ошибок (div с классом ошибки)
    wait.until(EC.presence_of_all_elements_located(LIST_ERRORS))

    # Проверяем количество подсвеченных красным полей
    error_fields = driver.find_elements(*LIST_ERRORS)
    assert len(error_fields) == 3, f"Ожидалось 3 поля с ошибкой, получено: {len(error_fields)}"
