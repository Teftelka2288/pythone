from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

url = "http://the-internet.herokuapp.com/add_remove_elements/"

driver_Ch = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_Ch.maximize_window()

# 1. Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver_Ch.get(url)

# 2. Пять раз кликните на кнопку `Add Element`. 
btn_add_locator = 'button[onclick="addElement()"]'
btn_add = driver_Ch.find_element(By.CSS_SELECTOR, btn_add_locator)
for i in range (0, 5):
    btn_add.click()

# 3. Соберите со страницы список кнопок `Delete`.
btn_dlt_locator = 'button[onclick="deleteElement()"]'
btn_dlt_list = driver_Ch.find_elements(By.CSS_SELECTOR, btn_dlt_locator)

# 4. Выведите на экран размер списка.
print(f'Колличество кнопок в Chrome -  {len(btn_dlt_list)}')

# 5. реализовать для Chrome и Firefox.
driver_Ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_Ff.maximize_window
driver_Ff.get(url)
btn_add = driver_Ff.find_element(By.CSS_SELECTOR ,btn_add_locator)
for i in range (1, 6):
    btn_add.click()
btn_dlt_list = driver_Ff.find_elements(By.CSS_SELECTOR, btn_dlt_locator)
driver_Ff.close()

print(f'Колличество кнопок в FireFox -  {len(btn_dlt_list)}')

# sleep(19)