from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/entry_ad"

driver_Ch = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_Ch.maximize_window()

# 1. Откройте страницу.
driver_Ch.get(url)

# 2. В модальном окне нажмите на кнопку `Сlose`.
btn_close_selector = ("div.modal-footer > p")
close_modal_btn = driver_Ch.find_element(By.CSS_SELECTOR, btn_close_selector)
sleep(3)

close_modal_btn.click()
sleep(2)