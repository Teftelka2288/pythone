from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.1)

try:
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_frome_content = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".bg-success")))
    sleep(2)
    print(text_frome_content)

except Exception as ex:
    print(ex)
finally:
    driver.quit()