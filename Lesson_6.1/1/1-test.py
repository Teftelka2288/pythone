import pytest
from PageObject import DatatypesPage
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
    
@pytest.mark.parametrize("data", [
    {
        "First_name": "Иван",
        "Last_name": "Петров",
        "Address": "Ленина, 55-3",
        "Email": "test@skypro.com",
        "Phone_number": "+7985899998787",
        "Zip_code": "",
        "City": "Москва",
        "Country": "Россия",
        "Job_position": "QA",
        "Company": "SkyPro"
    }
])

def test_1(browser, data):

    page = DatatypesPage(browser, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


    for field_name, field_value in data.items():
        method = getattr(page, f"type_{field_name}")
        method(field_value)
    

    page.clk_Submit()
    
 
    colors = {}

    for field_name in data.keys():
        method = getattr(page, f"bkgr_{field_name}")
        colors[field_name] = method()


    expected_color_red = "rgba(248, 215, 218, 1)"

    expected_color_green = "rgba(209, 231, 221, 1)"

    for field_name, color in colors.items():
        expected_color = expected_color_red if field_name == "Zip_code" else expected_color_green
        assert color == expected_color, f"Некорректный цвет для поля {field_name}"