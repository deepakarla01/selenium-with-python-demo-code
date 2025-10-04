from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Textbox(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.ut = Utils()

    log = Utils.custom_logger()

    def go_to_textbox(self, url):
        expected_url = url + "text-box"
        self.driver.get(expected_url)
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in go_to_textbox: {e}")
            return False

    def enter_full_name(self, full_name):
        fullname = self.wait_for_presence_of_element(By.ID, "userName")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fullname)
        fullname.send_keys(full_name)

        if fullname.get_attribute("value") == full_name:
            return True
        else:
            self.log.error("An unexpected error occurred in enter_full_name: {e}")
            return False

    def enter_email(self, e_mail):
        email = self.wait_for_presence_of_element(By.ID, "userEmail")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", email)
        email.send_keys(e_mail)

        if email.get_attribute("value") == e_mail:
            return True
        else:
            self.log.error("An unexpected error occurred in enter_email: {e}")

    def enter_current_address(self, current_address):
        curr_address = self.wait_for_presence_of_element(By.ID, "currentAddress")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", curr_address)
        curr_address.send_keys(current_address)

        if curr_address.get_attribute("value") == current_address:
            return True
        else:
            self.log.error("An unexpected error occurred in enter_current_address: {e}")
            return False

    def enter_permanent_address(self, permanent_address):
        perm_address = self.wait_for_presence_of_element(By.ID, "permanentAddress")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", perm_address)
        perm_address.send_keys(permanent_address)

        if perm_address.get_attribute("value") == permanent_address:
            return True
        else:
            self.log.error(
                "An unexpected error occurred in enter_permanent_address: {e}"
            )
            return False

    def click_submit(self):
        submit = self.wait_for_presence_of_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)

        try:
            submit.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_submit: {e}")
            return False

    def success_submit(self):
        name = self.wait_for_presence_of_element(By.ID, "name")
        email = self.wait_for_presence_of_element(By.ID, "email")

        if name and email:
            return True
        else:
            self.log.error("An unexpected error occurred in success_submit: {e}")
            return False
