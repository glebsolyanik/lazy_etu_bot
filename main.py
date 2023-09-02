from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def mark_the_presence():
        login = "glebsolyanik03@gmail.com"
        password = "branordeli32"

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')   # Режим невидимки
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--remote-debugging-port=9222')

        driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=chrome_options)

        driver.get("https://lk.etu.ru/login")

        log_elements = driver.find_elements(By.CSS_SELECTOR,
                              'input.form-control.form-control-lg.form-control-login.mb-1')

        log_elements[0].send_keys(login)
        log_elements[1].send_keys(password)

        login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        login_button.click()

        attendance_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//h5[contains(text(),'Посещаемость')]")))

        attendance_button.click()

        driver.switch_to.window(driver.window_handles[1])

        login_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                        (By.XPATH, "//button[contains(text(), 'Авторизоваться')]")))
        login_button.click()

        try:
                check_in_button = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                                (By.XPATH, "//button[contains(text(), 'Отметиться')]")))

                check_in_button.click()
                driver.close()
                return 0
        except TimeoutException:
                driver.close()
                return 1





