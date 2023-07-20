import os
import json
from logo_data import *

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

def replace_fav_icon():
    os.remove("docs/favicon.ico")
    os.system("cp Report_Modifier/favicon.ico docs")

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


    replace_json_part(file_path)
    replace_css_data(css_file, logo1, logo_url)
    # replace_css_data(css_file, logo_name, logo_name_hidden)
    replace_title(html_file,old_title,new_title)
    replace_fav_icon()

if __name__ == "__main__":
    do_modification_on_report()