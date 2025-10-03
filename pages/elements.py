from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Elements(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.ut=Utils()

    TEXTBOX = "//span[normalize-space()='Text Box']"
    CHECKBOX = "//span[normalize-space()='Check Box']"
    RADIOBUTTON = "//span[normalize-space()='Radio Button']"
    WEBTABLES = "//span[normalize-space()='Web Tables']"
    BUTTONS = "//span[normalize-space()='Buttons']"
    LINKS = "//span[normalize-space()='Links']"
    BROKEN_LINKS_IMAGES = "//span[normalize-space()='Broken Links - Images']"
    UPLOAD_AND_DOWNLOAD = "//span[normalize-space()='Upload and Download']"
    DYNAMIC_PROPERTIES = "//span[normalize-space()='Dynamic Properties']"

    def check_if_on_elements_page(self,url):
        expected_url = url + "elements"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("I am not on elements page: {e}")
            return False

    def click_textbox(self,url):
        expected_url = url + "elements"
        self.driver.get(expected_url)
        textbox = self.wait_for_presence_of_element(By.XPATH, self.TEXTBOX)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", textbox)
        try:
            textbox.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_textbox: {e}")
            return False

    def navigate_to_textbox_page(self,url):
        expected_url = url + "text-box"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_textbox_page: {e}")
            return False

    def click_checkbox(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        checkbox = self.wait_for_presence_of_element(By.XPATH, self.CHECKBOX)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        try:
            checkbox.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_checkbox: {e}")
            return False

    def navigate_to_checkbox_page(self,url):
        expected_url = url + "checkbox"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_checkbox_page: {e}")
            return False

    def click_radiobutton(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        radiobutton = self.wait_for_presence_of_element(By.XPATH, self.RADIOBUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", radiobutton)
        try:
            radiobutton.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_radiobutton: {e}")
            return False

    def navigate_to_radiobutton_page(self,url):
        expected_url = url + "radio-button"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_radiobutton_page: {e}")
            return False

    def click_webtables(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        webtables = self.wait_for_presence_of_element(By.XPATH, self.WEBTABLES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", webtables)
        try:
            webtables.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_webtables: {e}")
            return False

    def navigate_to_webtables_page(self,url):
        expected_url = url + "webtables"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_webtables_page: {e}")
            return False

    def click_buttons(self,url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        buttons = self.wait_for_presence_of_element(By.XPATH, self.BUTTONS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", buttons)
        try:
            buttons.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_buttons: {e}")
            return False

    def navigate_to_buttons_page(self,url):
        expected_url = url + "buttons"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_buttons_page: {e}")
            return False

    def click_links(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        links = self.wait_for_presence_of_element(By.XPATH, self.LINKS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", links)
        try:
            links.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_links: {e}")
            return False

    def navigate_to_links_page(self,url):
        expected_url = url + "links"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_links_page: {e}")
            return False

    def click_broken_links_images(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        broken_links_images = self.wait_for_presence_of_element(By.XPATH, self.BROKEN_LINKS_IMAGES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", broken_links_images)
        try:
            broken_links_images.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_broken_links_images: {e}")
            return False

    def navigate_to_broken_links_images_page(self,url):
        expected_url = url + "broken"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_broken_links_images_page: {e}")
            return False

    def click_upload_and_download(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        upload_and_download = self.wait_for_presence_of_element(By.XPATH, self.UPLOAD_AND_DOWNLOAD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", upload_and_download)
        try:
            upload_and_download.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_upload_and_download: {e}")
            return False

    def navigate_to_upload_and_download_page(self,url):
        expected_url = url + "upload-download"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_upload_and_download_page: {e}")
            return False

    def click_dynamic_properties(self, url):
        # expected_url = url + "elements"
        # self.driver.get(expected_url)

        dynamic_properties = self.wait_for_presence_of_element(By.XPATH, self.DYNAMIC_PROPERTIES)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dynamic_properties)
        try:
            dynamic_properties.click()
            return True
        except Exception as e:
            self.log.error("An unexpected error occurred in click_dynamic_properties: {e}")
            return False

    def navigate_to_dynamic_properties_page(self,url):
        expected_url = url + "dynamic-properties"
        if self.ut.check_expected_url(expected_url, self.driver.current_url):
            return True
        else:
            self.log.error("An unexpected error occurred in navigate_to_dynamic_properties_page: {e}")
            return False