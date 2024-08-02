from selenium.webdriver.common.by import By

url = ""

class Shop_CardPage():
    def __init__(self, browser):
        self.driver = browser
    
    def find(self, select):
        finder = self.driver.find_element(By.CSS_SELECTOR, select)
        return finder
          
    # Нажмите Checkout.
    def clk_check(self):
        self.find("#checkout").click()

    # Заполните форму своими данными:
    def input_form(self, f_name, l_name, zip_code):
        ## имя,
        self.find("#first-name").send_keys(f_name)
        ## фамилия,
        self.find("#last-name").send_keys(l_name)
        ## почтовый индекс.
        self.find("#postal-code").send_keys(zip_code)

    def clk_cnt(self):
        self.find("#continue").click()

    # Прочтите со страницы итоговую стоимость ( `Total` ).
    def rd_total(self):
        return self.find('[class="summary_total_label"]').text
    # .summary_info_label.summary_total_label