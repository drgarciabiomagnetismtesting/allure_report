from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
import pandas as pd
from Element_Locator.HomePage_ContactUs.Contact_Us.ContactUsElements import ContactUsElements
import time
import allure

class ContactUs(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)
    
    @allure.step("Checking Contact Us Link Present In Navigation Bar and Redirecting To Contact Us Page")
    def get_contact_us_link_present_in_nav(self):
        with allure.step("Clicked On Contact Us Link Present In Navigation Bar"):
            self.do_click(ContactUsElements.contact_us_button)
        
        with allure.step("Verifying Contact Us Page"):
            body_text = self.get_text_from_element(BasePageElements.body)

            if "CONTACT US" in body_text:
                with allure.step("Contact Us Page Is Opened"):
                    return True
            else:
                with allure.step("Contact Us Page Is Not Opened"):
                    return False
    
    @allure.step("Checking Contact Us Form Validation Error While Submitted Empty Fields")
    def get_contact_form_empty_submission_status(self):
        with allure.step("Clicked On Send Message Button"):
            self.do_click(ContactUsElements.send_message_button)
            formErrorElement = self.get_text_from_element(ContactUsElements.contact_form_error)
          
        
        with allure.step("Checking Validation Error While Submitted"):
            form_element_text = self.get_text_from_element(ContactUsElements.contact_form)
            if "Please fill out this field." in form_element_text:
                with allure.step("Validation Errors are showing"):
                    return True
            else:
                with allure.step("Validation Errors are not showing"):
                    return False
    def count_sentence_occurrences(self,sentence,string):
        count = string.count(sentence)
        return count
    

    @allure.step("Submitting Contact Form With Details")
    def get_submit_contact_form_status(self,name,email,phone,subject,your_message):
        with allure.step("Entering Name"):
            self.do_clear_input_field(ContactUsElements.name)
            self.do_send_keys(ContactUsElements.name,name)
        with allure.step("Entering Email"):
            self.do_clear_input_field(ContactUsElements.email)
            self.do_send_keys(ContactUsElements.email,email)
        with allure.step("Entering Mobile Number"):
            self.do_clear_input_field(ContactUsElements.phone)
            self.do_send_keys(ContactUsElements.phone,phone)
        with allure.step("Entering Subject"):
            self.do_clear_input_field(ContactUsElements.subject)
            self.do_send_keys(ContactUsElements.subject,subject)
        with allure.step("Entering Your Message"):
            self.do_clear_input_field(ContactUsElements.your_message)
            self.do_send_keys(ContactUsElements.your_message,your_message)
        with allure.step("Clicked On Send Message Button"):
            self.do_click(ContactUsElements.send_message_button)
        
        time.sleep(5)
        contact_form_body = self.get_text_from_element(ContactUsElements.contact_form)
        
        time.sleep(5)
       
        if "Thank you for your message. It has been sent." in contact_form_body:
            with allure.step("Form Is Submitted Successfully"):
                return True
        elif self.count_sentence_occurrences("Please fill out this field",contact_form_body)== 4:
            with allure.step("Form Is Not Submitted Successfully, All Field Are Empty"):
                return False
        elif self.count_sentence_occurrences("Please fill out this field.",contact_form_body) >= 1:
            with allure.step("Form Is Not Submitted Successfully, Some Field Are Empty"):
                return False
        elif self.count_sentence_occurrences("Please enter an email address.",contact_form_body) == 1 and self.count_sentence_occurrences("Please enter a telephone number.",contact_form_body) ==1:
            with allure.step("Form Is Not Submitted Successfully, Invalid Email Id and Phone Number"):
                return False
        elif self.count_sentence_occurrences("Please enter an email address.",contact_form_body) == 1:
            with allure.step("Form Is Not Submitted Successfully, Invalid Email Id"):
                return False
        elif self.count_sentence_occurrences("Please enter a telephone number.",contact_form_body) ==1:
            with allure.step("Form Is Not Submitted Successfully, Invalid Phone Number"):
                return False
                
        elif "One or more fields have an error. Please check and try again." in contact_form_body:
            with allure.step("Form Is Not Submitted Successfully, Some details are not correct"):
                return False

        else:
            with allure.step("Form Is Not Submitted Successfully"):
                return False

        



    
