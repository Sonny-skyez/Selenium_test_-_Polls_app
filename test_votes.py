from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test Votes - test suite, that tests all possible methods
of casting votes by user in Polls web application.
This suite contains 7 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_vote_1(unittest.TestCase):
    '''Test case that tests proper casted vote,
    and going back to index page.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Czy w aplikacji znajdują się jakieś widoczne błędy?").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Czy w aplikacji znajdują się jakieś widoczne błędy?'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Nadal szukam!'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("Ankiety").click()


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
