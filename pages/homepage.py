from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Homepage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.ut=Utils()

    ELEMENTS_CARD = "//h5[normalize-space()='Elements']"
    FORMS_CARD = "//h5[normalize-space()='Forms']"
    ALERTS_FRAME_WINDOW_CARD = "//h5[normalize-space()='Alerts, Frame & Windows']"
    WIDGETS_CARD = "//h5[normalize-space()='Widgets']"
    INTERACTIONS_CARD = "//h5[normalize-space()='Interactions']"
    BOOK_STORE_APP_CARD = "//h5[normalize-space()='Book Store Application']"

    def go_to_homepage(self,url):
        self.driver.get(url)

    def check_if_on_homepage(self,url):
        if self.ut.check_expected_url(url, self.driver.current_url):
            return True
        else:
            self.log.error("I am not on homepage: {e}")
            return False

    def click_on_elements_card(self):
        elements_card = self.wait_for_presence_of_element(By.XPATH, self.ELEMENTS_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_card)
        try:
            elements_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_elements_card: {e}")
            return False

    def navigate_to_elements_page(self,url):
        expected_url = url + "elements"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_elements_page: {e}")
            return False

    def click_on_forms_card(self):
        forms_card = self.wait_for_presence_of_element(By.XPATH, self.FORMS_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", forms_card)
        try:
            forms_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_forms_card: {e}")
            return False

    def navigate_to_forms_page(self,url):
        expected_url = url + "forms"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_forms_page: {e}")
            return False

    def click_on_alerts_frame_window_card(self):
        alerts_frame_window_card = self.wait_for_presence_of_element(By.XPATH, self.ALERTS_FRAME_WINDOW_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", alerts_frame_window_card)
        try:
            alerts_frame_window_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_alerts_frame_window_card: {e}")
            return False

    def navigate_to_alerts_frame_window_page(self,url):
        expected_url = url + "alertsWindows"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_alerts_frame_window_page: {e}")
            return False

    def click_on_widgets_card(self):
        widgets_card = self.wait_for_presence_of_element(By.XPATH, self.WIDGETS_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", widgets_card)
        try:
            widgets_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_widgets_card: {e}")
            return False

    def navigate_to_widgets_page(self,url):
        expected_url = url + "widgets"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_widgets_page: {e}")
            return False

    def click_on_interactions_card(self):
        interactions_card = self.wait_for_presence_of_element(By.XPATH, self.INTERACTIONS_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", interactions_card)
        try:
            interactions_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_interactions_card: {e}")
            return False

    def navigate_to_interactions_page(self,url):
        expected_url = url + "interaction"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_interactions_page: {e}")
            return False

    def click_on_book_store_app_card(self):
        book_store_app_card = self.wait_for_presence_of_element(By.XPATH, self.BOOK_STORE_APP_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", book_store_app_card)
        try:
            book_store_app_card.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_on_book_store_app_card: {e}")
            return False

    def navigate_to_book_store_app_page(self,url):
        expected_url = url + "books"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_book_store_app_page: {e}")
            return False
