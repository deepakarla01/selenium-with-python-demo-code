import logging
import re
import time

from pytest_assume.plugin import assume
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, \
    StaleElementReferenceException, TimeoutException, NoSuchWindowException, WebDriverException, \
    MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utils import Utils


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.log = Utils.custom_logger()


    def wait_for_presence_of_all_elements(self,locator_type,locator_id):
        try:
            wait = WebDriverWait(self.driver, 20)
            list_of_elements = wait.until(expected_conditions.presence_of_all_elements_located((locator_type, locator_id)))
            return list_of_elements
        except TimeoutException:
            self.log.error(f"Elements with locator id '{locator_id}' could not be found within 20 seconds. Timeout exception.")
        except Exception:
            self.log.error(f"Elements with locator id {locator_id} could not be found. An unexpected error occurred.")
        # Fallback if element not found
        self.log.error(f"Element {locator_id} not found")
        return None

    def wait_for_visibility_of_element(self,locator_type,locator_id):
        try:
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(expected_conditions.visibility_of_element_located((locator_type, locator_id)))
            return element
        except TimeoutException:
            self.log.error(f"Element with locator id '{locator_id}' could not be found within 20 seconds. Timeout exception.")
        except Exception:
            self.log.error(f"Element with locator id {locator_id} could not be found. An unexpected error occurred.")
        # Fallback if element not found
        self.log.error(f"Element {locator_id} not found")
        return None


    def wait_for_presence_of_element(self,locator_type,locator_id):
        try:
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(expected_conditions.presence_of_element_located((locator_type, locator_id)))
            return element
        except TimeoutException:
            self.log.error(f"Element with locator id '{locator_id}' could not be found within 20 seconds. Timeout exception.")
        except Exception:
            self.log.error(f"Element with locator id {locator_id} could not be found. An unexpected error occurred.")
        # Fallback if element not found
        self.log.error(f"Element {locator_id} not found")
        return None

    def scroll_to_element_with_action_chains(self, driver, element):
        log = Utils.custom_logger()
        try:
            log.info("Attempting to scroll to the element using ActionChains.")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            # log.info(f"Successfully scrolled to the element {element.get_attribute('outerHTML')}.")
            log.info(f"Successfully scrolled to the element {element}.")

        except StaleElementReferenceException:
            log.error("Element is no longer attached to the DOM. Retrying to find the element.")
            # Optionally retry to locate and interact with the element here

        except ElementNotInteractableException:
            log.error("Element is not interactable at the moment. Check visibility and state.")

        except MoveTargetOutOfBoundsException:
            log.error("Target element is out of bounds and cannot be scrolled to.")

        except NoSuchElementException:
            log.error("Element not found on the page. Check the locator or page state.")

        except TimeoutException:
            log.error("Timed out while attempting to scroll to the element.")

        except Exception as e:
            log.error(f"An unexpected error occurred: {str(e)}")
            raise

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

                    self.log.warning(f"URL does NOT contain expected part: {current_url}")
                    self.driver.close()
                    self.log.info("Child window closed.")
        finally:
            self.driver.switch_to.window(current_window)
            self.log.info(f"Switched back to parent window: {self.driver.current_url}")

        return False  # None of the windows matched

    @staticmethod
    def find_shortcode(driver, url):
        log = Utils.custom_logger()
        shortcodes = set()  # Use a set to avoid duplicates
        shortcode_pattern = r"\[[a-zA-Z0-9_-]+\]"  # Adjust pattern as needed

        # Find elements with text content
        elements = driver.find_elements(By.XPATH, "//*[text()]")
        for element in elements:
            text = element.text.strip()
            if text and re.search(shortcode_pattern, text):
                shortcodes.add(text)

        # Find elements with attributes containing shortcodes
        all_elements = driver.find_elements(By.XPATH, "//*")
        for element in all_elements:
            for attr_name in ["class", "id", "data-*", "title", "aria-label"]:
                attr_value = element.get_attribute(attr_name)
                if attr_value and re.search(shortcode_pattern, attr_value):
                    shortcodes.add(attr_value)
        if shortcodes:
            log.error(f"Found shortcodes on: {url} {', '.join(shortcodes)}")  # Log deduplicated shortcodes
        else:
            log.info(f"No shortcodes found on: {url}")
        #return list(shortcodes)  # Return a deduplicated list

    def check_layout_shift_issues(self, driver):
        """
        Detects layout shift issues likely caused by missing styles or scripts:
        - Visible elements with 0 width or height
        - Within the main content area
        """
        issues = []

        # Try common main content selectors
        possible_main_selectors = [
            "//main", "//*[@id='main']", "//*[@class='main']",
            "//*[@id='content']", "//*[@class='content']"
        ]
        main_container = None
        for xpath in possible_main_selectors:
            elements = self.driver.find_elements(By.XPATH, xpath)
            if elements:
                main_container = elements[0]
                break

        if not main_container:
            issues.append("Main content area not found.")
            return issues

        # Elements to skip (not expected to be visually sized)
        ignore_tags = {"script", "style", "meta", "link", "title", "head", "option"}

        elements = main_container.find_elements(By.XPATH, ".//*")
        for elem in elements:
            try:
                if not elem.is_displayed():
                    continue

                tag = elem.tag_name.lower()
                if tag in ignore_tags:
                    continue

                size = elem.size
                if size["width"] == 0 or size["height"] == 0:
                    id_attr = elem.get_attribute("id") or ""
                    class_attr = elem.get_attribute("class") or ""
                    identifier = f"<{tag} id='{id_attr}' class='{class_attr}'>"
                    issues.append(f"{identifier} is visible but has zero size (possible layout shift)")
            except:
                continue

        return issues

    def are_all_clickable_elements_clickable(self, clickable_elements):
        non_clickable_list = []

        for name, xpath in clickable_elements.items():
            try:
                element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, xpath))
                )

                tag = element.tag_name.lower()
                has_onclick = element.get_attribute("onclick")
                role = element.get_attribute("role")
                cls = element.get_attribute("class")

                if not (element.is_displayed() and element.is_enabled()):
                    self.log.error(f'Element "{name}" is not visible or enabled.')
                    non_clickable_list.append(name)
                    continue

                # Only consider certain tags as truly clickable
                if tag in ['a', 'button', 'input'] or has_onclick or role == 'button' or 'clickable' in cls:
                    self.log.debug(
                        f'Element "{name}" is clickable (tag: {tag}, onclick: {bool(has_onclick)}, role: {role}, class: {cls}).')
                else:
                    self.log.error(
                        f'Element "{name}" is visible & enabled but not truly clickable (tag: {tag}, no onclick/role).')
                    non_clickable_list.append(name)

            except TimeoutException:
                self.log.error(f'Element "{name}" was not found in time.')
                non_clickable_list.append(name)

        return True if not non_clickable_list else non_clickable_list

    def remove_ads_modals(self,driver):
        selectors = [
            "//div[contains(@class,'banner') or contains(@class,'advertisement')]",  # banners/ads
            "//div[contains(@class,'modal-content')]",  # modals
            "//iframe[contains(@src,'ads')]"  # iframes containing ads
        ]

        for selector in selectors:
            try:
                elements = self.wait_for_presence_of_all_elements(By.XPATH, selector)

                for elem in elements:
                    # For iframes, switch and hide inner content
                    if elem.tag_name.lower() == 'iframe':
                        driver.switch_to.frame(elem)
                        driver.execute_script("document.body.style.display='none';")
                        driver.switch_to.default_content()
                    else:
                        driver.execute_script("arguments[0].style.display='none';", elem)
            except NoSuchElementException:
                continue
