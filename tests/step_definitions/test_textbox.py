import pytest
from pytest_bdd import scenarios, when, parsers, then, given

from pages.textbox import Textbox
from utilities.utils import Utils

scenarios("C:\\Python-Selenium\\demoQASite\\tests\\features\\textbox.feature")

@pytest.fixture
def textbox_setup(setup):
    return Textbox(setup)

log=Utils.custom_logger()

@given('I am on "Text Box" Page')
def on_textbox_page_is_successful(textbox_setup,url):
    assert textbox_setup.go_to_textbox(url), 'An unexpected error occurred in go_to_textbox'
    log.info(f'Given I am on "Text Box" Page')

@when(parsers.parse('I enter a value "{full_name}" in the Full Name field'))
def entering_full_name(textbox_setup, full_name):
    assert textbox_setup.enter_full_name(full_name), 'An unexpected error occurred in enter_full_name'
    log.info(f'When I enter a value "{full_name}" in the Full Name field')

@when(parsers.parse('I enter a value "{e_mail}" in the E-mail field'))
def entering_e_mail(textbox_setup, e_mail):
    assert textbox_setup.enter_email(e_mail), 'An unexpected error occurred in enter_e_mail'
    log.info(f'When I enter a value "{e_mail}" in the E-mail field')

@when(parsers.parse('I enter a value "{current_address}" in the Current Address field'))
def entering_current_address(textbox_setup, current_address):
    assert textbox_setup.enter_current_address(current_address), 'An unexpected error occurred in enter_current_address'
    log.info(f'When I enter a value "{current_address}" in the Current Address field')

@when(parsers.parse('I enter a value "{permanent_address}" in the Permanent Address field'))
def entering_permanent_address(textbox_setup, permanent_address):
    assert textbox_setup.enter_permanent_address(permanent_address), 'An unexpected error occurred in enter_permanent_address'
    log.info(f'When I enter a value "{permanent_address}" in the Permanent Address field')

@when('I click on Submit button')
def clicking_submit_button(textbox_setup):
    assert textbox_setup.click_submit(), 'An unexpected error occurred in click_submit_button'
    log.info(f'When I click on Submit button')

@then('I should see the success information')
def successful_submit(textbox_setup):
    assert textbox_setup.success_submit(), 'An unexpected error occurred in success_submit'
    log.info(f'Then I should see the success information\n')