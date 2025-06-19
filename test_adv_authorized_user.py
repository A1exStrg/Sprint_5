from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators import REGISTER_BUTTON, EMAIL_AREA, PASS_AREA, ENTER_BUTTON, NEW_ADVERTISMENT_BUTTON, PUBLIC_POST_BUTTON, AVATAR_BUTTON

def test_adv_authorized_user(driver):

    wait = WebDriverWait(driver, 10)
    email = "storozhenko_20@gmail.com"
    password = "gfhjkm"

    #нажатие кнопки "Вход и регистрация"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    #Ввод email
    wait.until(EC.presence_of_element_located(EMAIL_AREA)).send_keys(email)

    #ввод пароля
    driver.find_element(*PASS_AREA).send_keys(password)

    #Нажимаем кнопку "Войти"
    driver.find_element(*ENTER_BUTTON).click()

    # Нажимаем кнопку "Разместить объявление"
    # Ждём, пока модальное окно исчезнет (если оно есть)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "homePage_modal__zSdUB")))

    # нажимаем кнопку "разместить объявление"
    post_button = wait.until(EC.element_to_be_clickable(NEW_ADVERTISMENT_BUTTON))
    post_button.click()

    # Заполнение формы объявления
    #название объявления
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Название']"))).send_keys("Тестовое объявление")
    #ввод описания объявления
    driver.find_element(By.XPATH, "//textarea[@placeholder='Описание товара']").send_keys("Описание тестового товара")
    #ввод цены
    driver.find_element(By.XPATH, "//input[@placeholder='Стоимость']").send_keys("99999")

    # выпадающий список категорий
    driver.find_element(By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1 ").click()

    #выбор категории
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Книги']"))).click()

    # выпадающий список городов
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[1]/button').click()

    #выбор города
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()= 'Казань']"))).click()

    # выбор состояния товара radiobutton
    driver.find_element(By.CLASS_NAME, "radioUnput_inputRegular__FbVbr").click()

    # нажаимаем опубликовать объявление
    driver.find_element(*PUBLIC_POST_BUTTON).click()

    # переход в профиль
    wait.until(EC.element_to_be_clickable(AVATAR_BUTTON)).click()

    # Проверка, что объявление появилось
    ad_title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Тестовое объявление')]")))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ad_title)
    assert ad_title.is_displayed()
    print("✅ Объявление успешно размещено и отображается в 'Мои объявления'.")

