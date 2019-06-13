from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test admin site - test suite, testing admin site functionalities
This test suite contains 3 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_1_admin_filters(unittest.TestCase):
    '''Test case - test admin site filter questions
    by date.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Sonny")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("XXXXX")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_link_text("Questions").click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_link_text("Past 7 days").click()
        driver.find_element_by_link_text("Past 7 days").click()
        driver.find_element_by_link_text("This month").click()
        driver.find_element_by_link_text("This year").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


class Test_2_admin_search(unittest.TestCase):
    '''Test case testing admin site searching methods.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Sonny")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("XXXXXX")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_link_text("Questions").click()
        driver.find_element_by_id("searchbar").click()
        driver.find_element_by_id("searchbar").clear()
        driver.find_element_by_id("searchbar").send_keys("Czy")
        driver.find_element_by_id("changelist-search").submit()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


class Test_3_admin_users(unittest.TestCase):
    '''Test case that tests admin site groups
    and users sub-sites.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Sonny")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("XXXXX")
        driver.find_element_by_id("login-form").submit()
        driver.find_element_by_link_text("Groups").click()
        driver.find_element_by_link_text("Authentication and Authorization").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("Home").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()