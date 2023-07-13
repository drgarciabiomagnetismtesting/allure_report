import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
import shutil

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


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == pytest.ExitCode.OK:
        # Test session passed
        print("Test session passed. Uploading report...")
        # Implement your report upload logic here
    else:
        report_dir = "Allure_Generated_Files"
        allure_dir = "allure-report"
        # shutil.rmtree(allure_dir, ignore_errors=True)
        # allure_cmd = f"allure generate {report_dir} --clean"
        # open_browser = "xdg-open http://127.0.0.1:5500/allure-report/"
        # os.system(allure_cmd)
        # os.system(open_browser)
        
        print("Test session failed. Report not uploaded.")

def pytest_configure(config):
    # Perform initialization or setup actions here
    print("Initializing pytest...")
    # Additional setup logic goes here

