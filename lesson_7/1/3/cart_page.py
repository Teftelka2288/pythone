from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        checkout_button = self.browser.find_element(By.ID, 'checkout')
        checkout_button.click()
        