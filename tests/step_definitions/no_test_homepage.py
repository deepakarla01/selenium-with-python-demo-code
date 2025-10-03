import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.homepage import Homepage
from utilities.utils import Utils

scenarios("C:\\Python-Selenium\\demoQASite\\tests\\features\\homepage.feature")

@pytest.fixture
def homepage_setup(setup):
    return Homepage(setup)

log=Utils.custom_logger()

@given("I am on Demo QA Homepage")
def on_homepage_is_successful(homepage_setup,url):
    homepage_setup.go_to_homepage(url)
    log.info("Given I am on Demo QA Homepage")

@when(parsers.parse('I click on "{card_name}" Card'))
def click_on_elements_card_is_successful(card_name,homepage_setup):
    navigation_map = {
        "Elements": homepage_setup.click_on_elements_card,
        "Forms": homepage_setup.click_on_forms_card,
        "Alerts_Frame_Windows": homepage_setup.click_on_alerts_frame_window_card,
        "Widgets": homepage_setup.click_on_widgets_card,
        "Interactions": homepage_setup.click_on_interactions_card,
        "Books": homepage_setup.click_on_book_store_app_card
    }

    try:
        for key, value in navigation_map.items():
            if key == card_name:
                assert value(), f"Failed to click on {card_name} Card"
                log.info(f'When I click on "{card_name}" Card')
                break
        else:
            log.error(f"Then: No matching click function found for card link: {card_name}\n")
    except Exception as e:
        log.error(f"Then: An unexpected error occurred in click_on_elements_card_is_successful: {e}\n")
        raise

@then(parsers.parse('I should navigate to "{card_name}" Page'))
def navigate_to_elements_page_is_successful(card_name,homepage_setup,url):
    navigation_map = {
        "Elements": lambda: homepage_setup.navigate_to_elements_page(url),
        "Forms": lambda: homepage_setup.navigate_to_forms_page(url),
        "Alerts_Frame_Windows": lambda: homepage_setup.navigate_to_alerts_frame_window_page(url),
        "Widgets": lambda: homepage_setup.navigate_to_widgets_page(url),
        "Interactions": lambda: homepage_setup.navigate_to_interactions_page(url),
        "Books": lambda: homepage_setup.navigate_to_book_store_app_page(url)
    }

    try:
        for key, value in navigation_map.items():
            if key == card_name:
                assert value(), f"Failed to navigate to {card_name} Page"
                log.info(f'Then I should navigate to "{card_name}" Page\n')
                break
        else:
            log.error(f"Then: No matching navigation function found for card link: {card_name}\n")
    except Exception as e:
        log.error(f"Then: An unexpected error occurred in navigate_to_elements_page_is_successful: {e}\n")
        raise