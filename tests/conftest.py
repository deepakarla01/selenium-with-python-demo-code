import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from utilities.utils import Utils
from pytest_bdd import hooks


@pytest.fixture(scope="session", autouse=True)
def setup(request, browser, url, userid, password, download_path, env):
    # launch browser
    if browser == "chrome":
        options = Options()
        # options.add_argument("--headless=new")  # Use new headless mode
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--log-level=3")  # Suppress logs
        options.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )  # More suppression

        # Disable ads (experimental)
        prefs = {
            "profile.default_content_setting_values.ads": 2,  # block ads
            "profile.default_content_setting_values.popups": 2,
            "profile.managed_default_content_settings.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.disable_open_during_load", True)  # block popups
        options.set_preference(
            "dom.webnotifications.enabled", False
        )  # disable notifications
        options.set_preference("permissions.default.desktop-notification", 2)
        options.set_preference("dom.push.enabled", False)
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        try:
            # Auto download latest EdgeDriver
            service = EdgeService(EdgeChromiumDriverManager().install())
        except Exception as e:
            # Fallback: use previously downloaded driver
            print(f"Could not auto-download EdgeDriver. Exception: {e}")
            # Provide a manual path to cached driver
            service = EdgeService(r"C:\msedgedriver.exe")

        driver = webdriver.Edge(service=service, options=options)
    else:
        print("Invalid browser. Valid options are chrome, firefox, edge")

    request.config.driver = driver  # Assign the driver to the test session instance
    request.config.browser = browser
    request.config.download_path = download_path
    request.config.userid = userid
    request.config.password = password
    request.config.env = env
    driver.get(url)
    driver.maximize_window()

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demoqa.com/")
    parser.addoption("--env", action="store", default="prod")
    # Set a dynamic download path based on OS
    default_download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    parser.addoption("--download_path", action="store", default=default_download_path)
    parser.addoption("--userid", action="store", default=None)
    parser.addoption("--password", action="store", default=None)


@pytest.fixture(scope="session")
def browser(request):
    selected_browser = request.config.getoption("--browser")
    if selected_browser:
        log.info(f"selected browser is {selected_browser}")
        return selected_browser


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def download_path(request):
    return request.config.getoption("--download_path")


@pytest.fixture(scope="session")
def userid(request):
    return request.config.getoption("--userid")


@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")


log = Utils.custom_logger()  # Assuming Utils.custom_logger is defined


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    log = Utils.custom_logger()  # Assuming Utils.custom_logger is defined
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        extras.append(pytest_html.extras.url("https://demoqa.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_dir = os.path.dirname(item.config.option.htmlpath or "./reports")

            # Sanitize filename
            import re

            sanitized_name = re.sub(
                r"[^\w\-_\. ]", "_", report.nodeid.replace("::", "_")
            )
            file_name = f"{sanitized_name}.png"
            destinationFile = os.path.join(report_dir, file_name)

            try:
                driver = (
                    item.config.driver
                )  # Access session-scoped driver. Adjust this based on your driver setup
                if driver:
                    log.info(f"Saving screenshot to: {destinationFile}")
                    driver.save_screenshot(destinationFile)
                    log.info(f"Screenshot saved successfully at: {destinationFile}")

                    # Relative path for embedding
                    relative_path = os.path.relpath(
                        destinationFile, start=report_dir
                    ).replace("\\", "/")
                    log.info(
                        f"Embedding screenshot with relative path: {relative_path}\n"
                    )

                    html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>'
                        % relative_path
                    )
                    extras.append(pytest_html.extras.html(html))
                else:
                    log.error("Driver instance is None. Screenshot not captured.")
            except Exception as e:
                log.error("Error while taking screenshot or embedding it.", exc_info=e)

        if "caplog" in item.funcargs:
            captured_lines = item.funcargs["caplog"].records
            gherkin_keywords = ("Given", "When", "Then", "And", "But")
            gherkin_steps = [
                record.message
                for record in captured_lines
                if record.message.strip().startswith(gherkin_keywords)
            ]
            if gherkin_steps:
                step_html = "<div><pre>{}</pre></div>".format("\n".join(gherkin_steps))
                extras.append(pytest_html.extras.html(step_html))

    report.extras = extras


def pytest_html_report_title(report):
    report.title = "Demo QA Automation Report"


@pytest.hookimpl
def pytest_bdd_before_scenario(request, feature, scenario):
    # Log the feature and scenario name before each scenario runs
    log.info(f"Feature: {feature.name}")
    log.info(f"Scenario: {scenario.name}")
