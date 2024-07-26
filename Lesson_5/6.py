from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/login"
username_input_selector = "input#username"
password_input_selector = "input#password"
login_btn_selector = "button.radius"
#login > button
name = 'tomsmith'
password = 'SuperSecretPassword!'

driver_Ch = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_Ch.maximize_window()

# 1. Откройте страницу.
driver_Ch.get(url)
sleep(1)

# 2. В поле username введите значение `tomsmith`.
name_input = driver_Ch.find_element(By.CSS_SELECTOR, username_input_selector)
name_input.send_keys(name)
sleep(1)

# 3. В поле password введите значение `SuperSecretPassword!`.
password_input = driver_Ch.find_element(By.CSS_SELECTOR, password_input_selector)
password_input.send_keys(password)
sleep(1)

# 4. Нажмите кнопку `Login`.
login_btn = driver_Ch.find_element(By.CSS_SELECTOR, login_btn_selector)
login_btn.click()
sleep(4)