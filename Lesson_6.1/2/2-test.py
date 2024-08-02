import time
import pytest
from PageObject import CalculatorPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture

def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    # Закройте браузер.
    driver.quit()
    
@pytest.mark.parametrize("delay", [
    (45)
])

def test_Calk15(browser, delay):

    page = CalculatorPage (browser, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")



    page.type_Delay(delay)
    

    page.btn_seven()
    
    page.btn_plus()
    
    page.btn_eight()
    
    page.btn_equally()



    time.sleep(delay)
   
    assert page.btn_screen(delay).get_attribute("textContent") == "15"