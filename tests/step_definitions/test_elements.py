import pytest
from pytest_bdd import scenarios, given, parsers, when, then

from pages.elements import Elements
from pages.homepage import Homepage
from utilities.utils import Utils

scenarios("C:\\Python-Selenium\\demoQASite\\tests\\features\\elements.feature")

@pytest.fixture
def elements_setup(setup):
    return Elements(setup),Homepage(setup)

log = Utils().custom_logger()

# @given(parsers.parse('I am on Elements page'))
# def i_am_on_elements_page(elements_setup,url):
#     if elements_setup[0].check_if_on_elements_page(url):
#         pass
#     else:
#         elements_setup[1].go_to_homepage(url)
#         elements_setup[1].click_on_elements_card()
#
#     log.info("Given I am on Elements page")

@when(parsers.parse('I click on "{menu_link}" menu'))
def i_click_on_menu_link(menu_link,elements_setup,url):
    navigation_map = {
        "Text Box": lambda: elements_setup[0].click_textbox(url),
        "Check Box": lambda: elements_setup[0].click_checkbox(url),
        "Radio Button": lambda: elements_setup[0].click_radiobutton(url),
        "Web Tables": lambda: elements_setup[0].click_webtables(url),
        "Buttons": lambda: elements_setup[0].click_buttons(url),
        "Links": lambda: elements_setup[0].click_links(url),
        "Broken Links - Images": lambda: elements_setup[0].click_broken_links_images(url),
        "Upload and Download": lambda: elements_setup[0].click_upload_and_download(url),
        "Dynamic Properties": lambda: elements_setup[0].click_dynamic_properties(url)
    }

    try:
        for key, value in navigation_map.items():
            if key == menu_link:
                assert value(), f"Failed to click on {menu_link} menu"
                log.info(f'When I click on "{menu_link}" menu')
                break
        else:
            log.error(f"When: No matching click function found for menu link: {menu_link}")
    except Exception as e:
        log.error(f"When: An unexpected error occurred in i_click_on_menu_link: {e}")
        raise

@then(parsers.parse('I should navigate to "{menu_link}" Page'))
def i_should_navigate_to_menu_link_page(menu_link,elements_setup,url):
    navigation_map = {
        "Text Box": lambda: elements_setup[0].navigate_to_textbox_page(url),
        "Check Box": lambda: elements_setup[0].navigate_to_checkbox_page(url),
        "Radio Button": lambda: elements_setup[0].navigate_to_radiobutton_page(url),
        "Web Tables": lambda: elements_setup[0].navigate_to_webtables_page(url),
        "Buttons": lambda: elements_setup[0].navigate_to_buttons_page(url),
        "Links": lambda: elements_setup[0].navigate_to_links_page(url),
        "Broken Links - Images": lambda: elements_setup[0].navigate_to_broken_links_images_page(url),
        "Upload and Download": lambda: elements_setup[0].navigate_to_upload_and_download_page(url),
        "Dynamic Properties": lambda: elements_setup[0].navigate_to_dynamic_properties_page(url)
    }

    try:
        for key, value in navigation_map.items():
            if key == menu_link:
                assert value(), f"Failed to navigate to {menu_link} Page"
                log.info(f'Then I should navigate to "{menu_link}" Page\n')
                break
        else:
            log.error(f"Then: No matching navigation function found for menu link: {menu_link}")
    except Exception as e:
        log.error(f"Then: An unexpected error occurred in i_should_navigate_to_menu_link_page: {e}")
        raise

