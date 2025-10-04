import re

from selenium.common import (
    NoSuchElementException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
    NoSuchWindowException,
    WebDriverException,
    MoveTargetOutOfBoundsException,
)
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utils import Utils


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.log = Utils.custom_logger()

    def wait_for_presence_of_element(self, locator_type, locator_id):
        try:
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(
                expected_conditions.presence_of_element_located(
                    (locator_type, locator_id)
                )
            )
            return element
        except TimeoutException:
            self.log.error(
                f"Element with locator id '{locator_id}' could not be found within 20 seconds. Timeout exception."
            )
        except Exception:
            self.log.error(
                f"Element with locator id {locator_id} could not be found. An unexpected error occurred."
            )
        # Fallback if element not found
        self.log.error(f"Element {locator_id} not found")
        return None

    def multiple_windows_switch_check_page_url_part(self, expected_part):
        wait = WebDriverWait(self.driver, 30)
        current_window = self.driver.current_window_handle

        try:
            # Wait for a new window to open
            wait.until(lambda d: len(d.window_handles) > 1)
        except TimeoutException:
            self.log.warning("Timeout: No new window detected.")
            return False

        all_windows = self.driver.window_handles
        self.log.info(f"Total windows found: {len(all_windows)}")

        try:
            for window in all_windows:
                if window != current_window:
                    self.driver.switch_to.window(window)
                    current_url = self.driver.current_url
                    self.log.info(f"Switched to window with URL: {current_url}")

                    if expected_part in current_url:
                        self.log.info(f"URL contains expected part: '{expected_part}'")
                        self.driver.close()
                        self.log.info("Child window closed.")
                        return True  # Success: return immediately

                    self.log.warning(
                        f"URL does NOT contain expected part: {current_url}"
                    )
                    self.driver.close()
                    self.log.info("Child window closed.")
        finally:
            self.driver.switch_to.window(current_window)
            self.log.info(f"Switched back to parent window: {self.driver.current_url}")

        return False  # None of the windows matched
