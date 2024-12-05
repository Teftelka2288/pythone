from selenium.webdriver.common.by import By


class CatalogPage:
    def __init__(self, browser):
        self.browser = browser
    
    def add_product_to_cart(self):
        backpack_button = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        backpack_button.click()

        t_short_button = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        t_short_button.click()

        onesie_button = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
        onesie_button.click()

    def go_to_cart(self):
        cart_link = self.browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart_link.click()