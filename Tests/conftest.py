import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
import shutil
import time
import json




def replace_json_part(file_path):
   
    with open(file_path, 'r') as file:
        json_data = json.load(file)

   
    json_data["reportName"] = "Dr. Garciabiomagnetism Website Report"
    with open(file_path, 'w') as file:
        json.dump(json_data, file)

def replace_css_data(file_path, search_data, replace_data):
    print(file_path)
    with open(file_path, 'r') as file:
        css_content = file.read()
    
    
    updated_css_content = css_content.replace(search_data, replace_data)
    
    with open("test.txt", "w") as f:
        f.write(updated_css_content)
    f.close()
    
    with open(file_path, 'w') as file:
        file.write(updated_css_content)
    file.close()

def replace_title(file_path, old_title, new_title):
    
    with open(file_path, 'r') as file:
        html_content = file.read()
    file.close()
    
    updated_html_content = html_content.replace(old_title, new_title)

    
    with open(file_path, 'w') as file:
        file.write(updated_html_content)
    file.close()

def replace_file(delete_file_path,copy_file_path):
    os.remove(delete_file_path)
    os.system(f"cp {copy_file_path} docs")

def do_modification_on_report():
    file_path = "docs/widgets/summary.json"
    css_file = "docs/styles.css"
    html_file = "docs/index.html"



    logo_url = """margin-right: 10px;
    border-radius: 20px;
    height: 90px;
    background: url(https://biomag.s3.us-east-2.amazonaws.com/logo-min.jpg);
    background-size: contain;
    background-repeat: no-repeat;"""


    logo_name_hidden = """.side-nav__brand-text {
        visibility: hidden;
        padding-left: 16px
    }
    """

    new_title = "<title>Dr. Garciabiomagnetism Report</title>"
    old_title = "<title>Allure Report</title>"

    favicon_delete_file_path = "docs/favicon.ico"
    favicon_copy_file_path = "Report_Modifier/favicon.ico"

    style_sheet_delete_file_path = "docs/styles.css"
    style_sheet_copy_file_path = "Report_Modifier/styles.css"

    replace_json_part(file_path)
    # replace_css_data(css_file, logo1, logo_url)
    # replace_css_data(css_file, logo_name, logo_name_hidden)
    replace_title(html_file,old_title,new_title)
    replace_file(favicon_delete_file_path,favicon_copy_file_path)
    replace_file(style_sheet_delete_file_path,style_sheet_copy_file_path)


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
        time.sleep(3)
        do_modification_on_report()
        os.system(git_status)
        os.system(git_add)
        os.system(git_commit)
        os.system(git_push)

       
        
        print("Report Hosted : https://drgarciabiomagnetismtesting.github.io/allure_report/")

def pytest_configure(config):
    
    print("Initializing pytest...")
    delete_allure_report = "rm -rf Allure_Generated_Files"
    create_allure_report = "mkdir Allure_Generated_Files"
    copy_system_environment = "cp Data_Files/environment.properties Allure_Generated_Files"
    os.system(delete_allure_report)
    time.sleep(5)
    os.system(create_allure_report)
    os.system(copy_system_environment)
    

