from selenium import webdriver
from page_calculator import CalculatorPage

def test_calculator():
    browser = webdriver.Chrome()
    main_page = CalculatorPage(browser)

    main_page.set_delay('45')
    main_page.click_button('7')
    main_page.click_button('+')
    main_page.click_button('8')
    main_page.click_button('=')

    result = main_page.get_result()
    assert result == '15', 'Result is not 15'