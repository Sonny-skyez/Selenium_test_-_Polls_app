from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test Login - second test suite, that tests all possible methods
of user login: login and no password, password but no login,
wrong password, wrong login etc.
This test suite contains 7 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_1_no_user_no_pass(unittest.TestCase):
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


class Test_2_login_pass_no_user(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("XXXXXX")
        driver.find_element_by_id("login-form").submit()
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


class Test_3_login_user_no_pass(unittest.TestCase):
    '''Test case with right username and wrong password
    typed in by user.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Sonny")
        driver.find_element_by_id("login-form").submit()
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


class Test_4_wrong_user_pass(unittest.TestCase):
    '''Test case with wrong username and right password
    typed in by user.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Admin").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("sonnny")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("XXXXXX")
        driver.find_element_by_id("login-form").submit()


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


class Test_5_user_wrong_pass(unittest.TestCase):
    '''Test case tests situation, when username is right,
    and password is wrong'''
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
        driver.find_element_by_id("id_password").send_keys("wrongpass")
        driver.find_element_by_id("login-form").submit()


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


class Test_6_wrong_user_wrong_pass(unittest.TestCase):
    '''Test case with wrong username and wrong password
    typed in by user.'''
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
        driver.find_element_by_id("id_password").send_keys("xxx")
        driver.find_element_by_id("login-form").submit()


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


class Test_7_login_logout(unittest.TestCase):
    '''Test case with proper username and password;
    successfull login attempt + logout.'''
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