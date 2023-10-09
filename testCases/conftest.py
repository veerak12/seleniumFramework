import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("**** Launching Chrome Browser ****")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("**** Launching Firefox Browser ****")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("**** Launching Edge Browser ****")
    else: #no browser specified it will take default browser
        driver = webdriver.Chrome()
        print("**** Launching Default Browser ****")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request: pytest.FixtureRequest):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#### pytest HTML REPORTS ######

#It is the hook that is to be added in the HTML report

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Veera'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Python Home", None)
#     metadata.pop("Plugins", None)


# def pytest_configure(config):
#     if not hasattr(config, 'metadata'):
#         config.metadata = {}
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Veera'

# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("Python Home", None)
#     metadata.pop("Plugins", None)



