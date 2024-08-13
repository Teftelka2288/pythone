from selenium.webdriver.common.by import By


class Checkout2Page:
    def __init__(self, browser):
        self.browser = browser

    def get_total(self):
        total_element = self.browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]')
        total = total_element.text
        return total[-6:]