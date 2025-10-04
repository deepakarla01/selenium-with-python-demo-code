# Selenium with Python Demo Code

A collection of Python scripts demonstrating Selenium WebDriver functionalities with **BDD (Behavior Driven Development)** using `pytest-bdd`. 
This repository showcases browser automation, test automation, and cross-browser testing following best practices like the **Page Object Model (POM)**.

## Project Structure
- **base/**: Contains base classes for WebDriver initialization and configurations.  
- **pages/**: Implements Page Object Model for reusable and maintainable element locators and actions.  
- **features/**: Contains `.feature` files written in **Gherkin syntax** for BDD scenarios.  
- **step_definitions/**: Maps the steps in feature files to Python functions using `pytest-bdd`.  
- **utilities/**: Utility functions for logging, waits, browser management, etc.  
- **reports/**: Stores HTML or JSON reports generated from test runs.  

## Prerequisites
- Python 3.6+  
- Install required packages:

## Execution
pytest -vs --gherkin-terminal-reporter --capture=sys --browser edge --url https://demoqa.com/ --html=reports/demoqa_automation.html --self-contained-html

## Cross-Browser Execution
The project supports running tests on multiple browsers like Chrome, Firefox, and Edge.

## Page Object Model (POM)
This project follows POM design, where each page has a corresponding class in pages/ that:
- Defines element locators
- Encapsulates page actions
- Promotes reusability and maintainability

## BDD with Gherkin
- Feature files use Gherkin syntax (Given, When, Then) to describe test scenarios in plain English.
- Step definitions implement the actions corresponding to each Gherkin step using pytest-bdd.

## Demo Features
- Browser automation (open URLs, click buttons, fill forms)
- Interaction with web elements via locators and actions
- Automated tests with BDD scenarios
- Cross-browser testing with multiple WebDriver configurations
- Detailed test reports
