import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc


@pytest.fixture(scope= 'class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.page_load_strategy = 'eager'

    web_driver = uc.Chrome(use_subprocess= True, options= options, version_main= 113)
    web_wait = WebDriverWait(web_driver,10)

    request.cls.driver = web_driver
    request.cls.wait = web_wait

    yield
    web_driver.close()
