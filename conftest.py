import pytest
from selenium import webdriver

@pytest.fixture
def open_browser():
    driver=webdriver.Chrome()
    yield driver
    driver.close()
