from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test suite: add edit & delete questions in admin panel.
This test suite contains 3 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_add_question(unittest.TestCase):
    '''Test case, that tests adding new poll question
    by the app user.'''
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
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Questions'])[1]/following::a[1]").click()
        driver.find_element_by_id("id_question_text").clear()
        driver.find_element_by_id("id_question_text").send_keys("Test")
        driver.find_element_by_id("question_form").submit()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_link_text("Now").click()
        driver.find_element_by_id("id_choice_set-0-choice_text").click()
        driver.find_element_by_id("id_choice_set-0-choice_text").clear()
        driver.find_element_by_id("id_choice_set-0-choice_text").send_keys("Test")
        driver.find_element_by_id("question_form").submit()


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