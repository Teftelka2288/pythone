import pytest
from PageObject.Main import Shop_MainPage
from PageObject.Cart import Shop_CardPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

   
    driver.quit()
    
@pytest.mark.parametrize("url, login, password, f_name, l_name, zip_code", [
    ("https://www.saucedemo.com/", "standard_user", "secret_sauce", "Анатолий", "Киселёв", "236022")
    ])
def test_total(browser, url, login, password, f_name, l_name, zip_code):
    
    shp = Shop_MainPage(browser, url)
    
    shp.authorization(login, password)
   
    shp.add_to()
   
    shp.go_to()
    crd = Shop_CardPage(browser)
    
    crd.clk_check()
    
    crd.input_form(f_name, l_name, zip_code)
   
    crd.clk_cnt()
    
    total_coast = crd.rd_total()
    
    assert "$58.29" in total_coast
