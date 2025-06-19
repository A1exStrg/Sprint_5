from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NEW_ADVERTISMENT_BUTTON


def test_adv_unauthorized_user(driver):

    wait = WebDriverWait(driver, 10)
    # Нажимаем кнопку "Разместить объявление"
    post_button = wait.until(EC.element_to_be_clickable(NEW_ADVERTISMENT_BUTTON))
    post_button.click()

    # Ожидание и проверка появления модального окна с заголовком
    modal_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")))
    #проверка модальное окно на экране
    assert modal_title.is_displayed()
