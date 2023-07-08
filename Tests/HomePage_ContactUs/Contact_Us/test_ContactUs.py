import pytest
from Tests.test_Base import BaseTest
from Pages.HomePage_ContactUs.Contact_Us.ContactUs import ContactUs
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure


def get_contact_form_data_list(excel_file_path):
    
    df = pd.read_excel(excel_file_path)
    df = df.fillna('')
    listValue = df.values.tolist()
    listValue = [tuple(value) for value in listValue]
    
    return listValue

@allure.title("Home Page Test Cases")
class TestContactUs(BaseTest):
    global ContactUsObj
    contact_param = get_contact_form_data_list(TestData.contact_form_data_file_path)

    @allure.title("Test Case 21 : Validate the contact us icon is clickable or not")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the contact us icon is clickable or not
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Contact us icon should be clickable .
    
    """)
    def test_contact_us_icon_clickable(self):
        TestContactUs.ContactUsObj = ContactUs(self.driver,self.wait)
        try:
            contact_us_status = TestContactUs.ContactUsObj.get_contact_us_link_present_in_nav()

            assert contact_us_status
        except:
            allure.attach(self.ContactUsObj.driver.get_screenshot_as_png(),name="Contact Us Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Contact Us Is Failed"):
                assert False
    
    
    
    @allure.title("Test Case 22 - 26 : Contact Form Submission")
    @pytest.mark.parametrize("name,email,phone,subject,your_message",contact_param)
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>1. Validate the contact us form is showing the error in correct format while submitting the empty form like ("
Please fill out this field".)

    <br><br>2. Validate the contact us form while submitting the invalid details in all fields it is showing the please enter correct detials

    <br><br>3. Validate the contact us form while submitting the valid details in all fields

    <br><br>4. Validate the some field will show the error like" please fill out this fields" while skipping the any field

    <br><br>5. Validate the some fields showing the error message while entering the invalid details   
    
    <br><br><b>Expeceted Results:</b>
    <br><br>1.Contact us form should show the error in correct format like ("Please fill out this field. ")

    <br><br>2. It should show the Please enter valid details 

    <br><br>3. It should show the " Thank you  for contact "

    <br><br>4. It should show the "Please fill out this field.  

    <br><br>5. It should show inavlid details entered field like"please enter valid details like that".
    
    """)
    def test_contact_form_submission(self,name,email,phone,subject,your_message):
        try:
            
            contact_form_status = TestContactUs.ContactUsObj.get_submit_contact_form_status(name,email,phone,subject,your_message)
            assert contact_form_status
        except:
            allure.attach(self.ContactUsObj.driver.get_screenshot_as_png(),name="Contact Form Validation Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Contact Form Validation Is Failed"):
                assert False

