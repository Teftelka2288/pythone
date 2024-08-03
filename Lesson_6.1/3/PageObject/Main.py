from selenium.webdriver.common.by import By

url = ""

class Shop_MainPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
    
    def find(self, select):
        finder = self.driver.find_element(By.CSS_SELECTOR, select)
        return finder
    
    # Авторизация
    def authorization(self, login, password):
        login_field = self.find("#user-name")
        password_field = self.find("#password")

        login_field.clear()
        login_field.send_keys(login)
        password_field.clear()
        password_field.send_keys(password)

        self.find("#login-button").click()

    #  Добавьте в корзину товары:
    def add_to(self):
        ## Sauce Labs Backpack
        self.find("#add-to-cart-sauce-labs-backpack").click()
        ## Sauce Labs Bolt T-Shirt
        self.find("#add-to-cart-sauce-labs-bolt-t-shirt").click()
        ## Sauce Labs Onesie
        self.find("#add-to-cart-sauce-labs-onesie").click()
    
    # Перейдите в корзину.
    def go_to(self):
        self.find(".shopping_cart_link").click()    