from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


'''Test Votes - first test suite, that tests all possible methods
of casting votes by user in Polls web application.
This test suite contains 7 test cases.

Tested URL:     https://polls-application.herokuapp.com/polls/'''


class Test_vote_1(unittest.TestCase):
    '''Test case that tests proper casted vote,
    and going back to index page.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
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


class Test_vote_2(unittest.TestCase):
    '''This test case tests how application
    will work, when user won't tast any vote.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Czy ta aplikacja powinna posiadać testy w Selenium?").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Nie wiem'])[1]/following::input[1]").click()
        driver.find_element_by_link_text(u"Powrót").click()


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


class Test_vote_3(unittest.TestCase):
    '''Test case that tests proper casted vote
    and get back to index by user clicking twice
    at -Back- button.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Bootstrap / obecna forma szablonów CSS?").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Bootstrap / obecna forma szablonów CSS?'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Obecne CSS'])[1]/following::input[1]").click()
        driver.find_element_by_link_text(u"Powrót").click()
        driver.find_element_by_link_text(u"Powrót").click()


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


class Test_vote_4(unittest.TestCase):
    '''Test case that tests situation, when user
    click 2. times at Vote button, without clicking
    at any given poll answer.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text("Najlepsza platforma streamingowa to:").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Chili'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Chili'])[1]/following::input[1]").click()
        driver.find_element_by_link_text(u"Powrót").click()


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


class Test_vote_5(unittest.TestCase):
    '''Test failed vote and next - proper casted
    vote by application user. Then Back to index page.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Bootstrap / obecna forma szablonów CSS?").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Obecne CSS'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Nie wybrałeś żadnej opcji.'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Obecne CSS'])[1]/following::input[1]").click()
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


class Test_vote_6(unittest.TestCase):
    '''Test case testig 2-times proper casted votes
    at the same answer by application user.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Czy ta aplikacja powinna posiadać testy w Selenium?").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Czy ta aplikacja powinna posiadać testy w Selenium?'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Nie wiem'])[1]/following::input[1]").click()
        driver.find_element_by_link_text(u"Powrót").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Tak'])[1]/following::label[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Nie wiem'])[1]/following::input[1]").click()
        driver.find_element_by_link_text(u"Powrót").click()
        driver.find_element_by_link_text(u"Powrót").click()


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


class Test_vote_7(unittest.TestCase):
    '''Test case that test situation in witch
    app user accessess 3 poll question from index pages
    and do not cast any vote.'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app(self):
        driver = self.driver
        driver.get("https://polls-application.herokuapp.com/polls/")
        driver.find_element_by_link_text(u"Jaka kolorystyka strony byłaby najlepsza?").click()
        driver.find_element_by_link_text(u"Powrót").click()
        driver.find_element_by_link_text(u"Bootstrap / obecna forma szablonów CSS?").click()
        driver.find_element_by_link_text(u"Powrót").click()
        driver.find_element_by_link_text(u"Czy w aplikacji znajdują się jakieś widoczne błędy?").click()
        driver.find_element_by_link_text(u"Powrót").click()


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