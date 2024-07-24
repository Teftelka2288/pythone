from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/inputs"
input_selector = ("input[type=number]")
thousand = '1000'
one_before_thousand = '999'

driver_Ch = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_Ch.maximize_window()

# 1. Откройте страницу.
driver_Ch.get(url)

# 2. Введите в поле текст `1000`.
nom_input = driver_Ch.find_element(By.CSS_SELECTOR, input_selector)
nom_input.send_keys(thousand)
sleep(2)

# 3. Очистите это поле (метод `clear`).
nom_input.clear()
sleep(1)

# 4. Введите в это же поле текст `999`.
nom_input.send_keys(one_before_thousand)
sleep(1)