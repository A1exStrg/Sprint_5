from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    REGISTER_BUTTON, EMAIL_AREA, PASS_AREA, ENTER_BUTTON, NEW_ADVERTISMENT_BUTTON,
    PUBLIC_POST_BUTTON, AVATAR_BUTTON, MODAL_WINDOW, EMAIL_FORM_AREA, TEXT_ADV_FORM,
    COST_FORM, DROP_DOWN_MENU_CATEGORY, CHOOSE_CATEGORY, DROP_DOWN_MENU_CITY,
    CHOOSE_CTY, RADIO_BUTTON, PUBLIC_ADV_BUTTON, ADVERTISMENT_FORM,MODAL_WINDOW_REGISTRATION
)


class TestAdvertisement:

    def test_adv_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 10)

        # Нажатие кнопки "Разместить объявление" без авторизации
        wait.until(EC.element_to_be_clickable(NEW_ADVERTISMENT_BUTTON)).click()

        # Проверка появления модального окна
        modal_title = wait.until(EC.visibility_of_element_located(MODAL_WINDOW_REGISTRATION))
        assert modal_title.is_displayed()
        print("❗ Модальное окно с предупреждением появилось.")

    def test_adv_authorized_user(self, driver):
        wait = WebDriverWait(driver, 10)
        email = "storozhenko_20@gmail.com"
        password = "gfhjkm"

        # Авторизация
        wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(EMAIL_AREA)).send_keys(email)
        driver.find_element(*PASS_AREA).send_keys(password)
        driver.find_element(*ENTER_BUTTON).click()

        # Ждём, пока модалка исчезнет
        wait.until(EC.invisibility_of_element_located(MODAL_WINDOW))

        # Переход к созданию объявления
        wait.until(EC.element_to_be_clickable(NEW_ADVERTISMENT_BUTTON)).click()

        # Заполнение объявления
        wait.until(EC.presence_of_element_located(EMAIL_FORM_AREA)).send_keys("Тестовое объявление")
        driver.find_element(*TEXT_ADV_FORM).send_keys("Описание тестового товара")
        driver.find_element(*COST_FORM).send_keys("99999")

        driver.find_element(*DROP_DOWN_MENU_CATEGORY).click()
        wait.until(EC.element_to_be_clickable(CHOOSE_CATEGORY)).click()

        driver.find_element(*DROP_DOWN_MENU_CITY).click()
        wait.until(EC.element_to_be_clickable(CHOOSE_CTY)).click()

        driver.find_element(*RADIO_BUTTON).click()
        driver.find_element(*PUBLIC_ADV_BUTTON).click()
        print("опубликовано")

        # Переход в профиль
        wait.until(EC.element_to_be_clickable(AVATAR_BUTTON)).click()
        print("перешли в профиль")

        # Проверка объявления
        ad_title = WebDriverWait(driver, 40).until(EC.visibility_of_element_located(ADVERTISMENT_FORM))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ad_title)
        assert ad_title.is_displayed()
        print("✅ Объявление успешно размещено и отображается в 'Мои объявления'.")


