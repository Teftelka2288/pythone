from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

url = "http://uitestingplayground.com/classattr"

driver_Ch = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_Ch.maximize_window()

# 1. Откройте страницу.
driver_Ch.get(url)

# 2. Кликните на **синюю** кнопку.
btn_css = ('button.btn.btn-primary')
blue_btn = driver_Ch.find_element(By.CSS_SELECTOR, btn_css)
blue_btn.screenshot("look_at_this_T5_CHROME.png")
blue_btn.click()
print("Конец с Хромом")

# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.


driver_Ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_Ff.maximize_window
driver_Ff.get(url)
blue_btn = driver_Ff.find_element(By.CSS_SELECTOR, btn_css)
blue_btn.screenshot("look_at_this_T5_FF.png")
blue_btn.click()
driver_Ff.close()
print("Конец с ФайрФоксом")