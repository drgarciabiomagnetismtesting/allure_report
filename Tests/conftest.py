import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
import shutil
import time

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
        report_dir = "Allure_Generated_Files"
        allure_dir = "docs"
        # shutil.rmtree(allure_dir, ignore_errors=True)
        allure_cmd = f"allure generate {report_dir} --clean"
        remove_docs_cmd = f"rm -rf docs"
        rename_allure_report = f"mv allure-report {allure_dir}"

        git_status = "git status"
        git_add = "git add ."
        git_commit = "git commit -m 'auto commit by pytest' "
        git_push = "git push origin2 master"
      
        os.system(allure_cmd)
        
        os.system(remove_docs_cmd)
        time.sleep(5)
        os.system(rename_allure_report)
        os.system(git_status)
        os.system(git_add)
        os.system(git_commit)
        os.system(git_push)

       
        
        print("Report Hosted : https://drgarciabiomagnetismtesting.github.io/allure_report/")

def pytest_configure(config):
    
    print("Initializing pytest...")
    delete_allure_report = "rm -rf Allure_Generated_Files"
    create_allure_report = "mkdir Allure_Generated_Files"
    os.system(delete_allure_report)
    time.sleep(5)
    os.system(create_allure_report)
    

