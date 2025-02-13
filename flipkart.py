from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class FlipkartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Or use the appropriate WebDriver for your browser
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.flipkart.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_homepage_load(self):
        self.assertIn("Online Shopping Site", self.driver.title)

    def test_02_close_login_popup(self):
        try:
            close_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
            close_button.click()
        except:
            pass  # If the popup is not there, continue

    def test_03_search_product(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("iPhone 14 plus" + Keys.RETURN)

    def test_04_filter_results(self):
        try:
            filter_option = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div/div[2]/div/label")
            filter_option.click()
        except Exception as e:
            print(f"Exception occurred: {e}")
            pass  # If the filter is not found, continue

    def test_05_sort_low_to_high(self):
        sort_dropdown = self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[1]")
        sort_dropdown.click()

    def test_06_add_to_cart(self):
        product = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[1]")
        product.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        add_to_cart_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
        add_to_cart_button.click()
        time.sleep(5)



    def test_08_remove_from_cart(self):
        remove_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Remove')]")
        remove_button.click()
        time.sleep(5)
        confirm_remove = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div[1]")
        confirm_remove.click()
        time.sleep(5)

    def test_09_navigate_to_login(self):
        login_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
        login_button.click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//span[contains(text(), 'Login')]"))

    def test_10_enter_mobile_and_request_otp(self):
        # Enter the mobile number
        mobile_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div/form/div[1]/input"))
        )
        mobile_input.send_keys("8197221572")
        time.sleep(10)

        # Click on the 'Request OTP' button
        request_otp_button = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div[2]/div/form/div[3]/button")
        request_otp_button.click()
        time.sleep(30)
        print("Test case test_10_enter_mobile_and_request_otp passed")

    def test_11_check_user_account(self):
        account_link = self.driver.find_element(By.XPATH, "//div[contains(text(), 'My Account')]")
        ActionChains(self.driver).move_to_element(account_link).perform()


    def test_12_view_order_history(self):
        account_link = self.driver.find_element(By.XPATH, "//div[contains(text(), 'My Account')]")
        ActionChains(self.driver).move_to_element(account_link).perform()
        orders_link = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Orders')]")
        orders_link.click()
        time.sleep(10)


    def test_13_logout(self):
        account_link = self.driver.find_element(By.XPATH, "//div[contains(text(), 'My Account')]")
        ActionChains(self.driver).move_to_element(account_link).perform()
        logout_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Logout')]")
        logout_button.click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]"))


if __name__ == "_main_":
    unittest.main()