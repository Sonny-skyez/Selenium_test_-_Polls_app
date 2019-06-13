from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test Login - second test suite, that tests all possible methods
of user login: login and no password, password but no login,
wrong password, wrong login etc.
This test suite contains 7 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_no_user_no_pass(unittest.TestCase):
    '''Test case when there is no user and no password
    in login attempt by user.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()


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
