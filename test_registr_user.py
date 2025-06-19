from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from locators import REGISTER_BUTTON, NO_ACC_BUTTON, PASS_AREA, PASS_AREA_REP, CREATE_ACC_BUTTON, AVATAR_BUTTON, ACC_USER_BUTTON

def test_registr_new_user(driver):
    wait = WebDriverWait(driver, 10)

    #нажатие кнопки "Вход и регистрация"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # нажатие кнопки "Нет аккаунта"
    wait.until(EC.visibility_of_element_located(NO_ACC_BUTTON)).click()

    #генерация email
    timestamp = int(time.time())
    random_id = random.randint(1000, 9999)
    email = f"user{timestamp}{random_id}@example.com"

    #ввод email
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Введите Email']"))).send_keys(email)

    #ввод пароля
    driver.find_element(*PASS_AREA).send_keys('gfhjkm')
    #повтор ввод пароля
    driver.find_element(*PASS_AREA_REP).send_keys('gfhjkm')

    # Нажимаем кнопку "Создать аккаунт"
    driver.find_element(*CREATE_ACC_BUTTON).click()

    #проверка наличия аватара
    avatar = wait.until(EC.visibility_of_element_located(AVATAR_BUTTON))
    assert avatar.is_displayed()

    #проверка имени пользователя
    element = wait.until(EC.visibility_of_element_located(ACC_USER_BUTTON))
    assert element.text == 'User.'

    #проверка текущего URL
    cureent_url = driver.current_url
    assert cureent_url == 'https://qa-desk.stand.praktikum-services.ru/regiatration'
    print("текущий адрес соответсвтует URL")

