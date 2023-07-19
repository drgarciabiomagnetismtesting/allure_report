import pytest
from Tests.test_Base import BaseTest
from Pages.Biomagnetism_Service.Biomagnetism_Service.BiomagnetismService import BiomagnetismService
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Biomagnetism Tests")
class TestBiomagnetismService(BaseTest):

    global biomagnetisServicemObj

    @allure.title("Test Case 12 : Biomagnetism Service and it's dropdown option are visible and clickable")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, mouse hovered on biomagnetism services submodules to be displayed in the form of dropdown and should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>When mouse hovered on biomagnetism services, dropdown should be displayed with the 2 submodules and try to click on that
    
    """)
    def test_biomagnetism_service_is_visible_and_clickable(self):
        TestBiomagnetismService.biomagnetisServicemObj = BiomagnetismService(self.driver,self.wait)
        try:
            assert self.biomagnetisServicemObj.is_biomagnetism_service_and_dropdown_visible_and_clickable()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Biomagnetism Service and it's dropdown option are visible and clickable Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Biomagnetism Service and it's dropdown option are visible and clickable Is Failed"):
                assert False
    

    @allure.title("Test Case 13 : Cities Filter Buttons are visible and clickable")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, all the cities are added as per the requirement
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In find a therpist detail page, therapists from over the cities should be displayed and should be clickble
    
    """)
    def test_all_cities_filter_visible_and_clickable(self):
        
        try:
            assert self.biomagnetisServicemObj.is_all_cities_filter_visible_and_clickable()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Cities Filter Buttons are visible and clickable Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Cities Filter Buttons are visible and clickable Is Failed"):
                assert False
    

    @allure.title("Test Case 14 : Sorting Functionality")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, filter by selecting all the types like newest, older, alphetical order in ascending and desceding order
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In find a new therapist if any filter is selected, result should be produced according to it
    
    """)
    def test_sorting_filter_is_working(self):
        
        try:
            assert self.biomagnetisServicemObj.is_sorting_filter_is_working()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Sorting Functionality Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Sorting Functionality Is Failed"):
                assert False

    @allure.title("Test Case 16 : Doctors showing according to city")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, clicking on cities, repective doctor will be dipslayed
    
    <br><br><b>Expeceted Results:</b>
    <br><br>if clicked on cities viewed on the screen, respective doctor should be displayed 
    
    """)
    def test_dr_showing_according_to_city_selected(self):
        
        try:
            assert self.biomagnetisServicemObj.is_dr_showing_according_to_city_selected()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Doctors showing according to city Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Doctors showing according to city Is Failed"):
                assert False

    @allure.title("Test Case 17 : Load More Functionality")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, load more is a button and by clicking it, it should display remaining doctors defaultly
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Clicking on loadmore button should load some more images with address
    
    """)
    def test_load_more(self):
        
        
        try:
            assert self.biomagnetisServicemObj.is_load_more_button_working()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Load More Functionality Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Load More Functionality Is Failed"):
                assert False
    
    @allure.title("Test Case 15 : Doctor's Email Address, Phone Number, Website visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, each therapist image is displayed and below address, email and website is added
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In find a new therapist, doctors image and their address should be displayed
    
    """)
    def test_all_doctors_details_are_correct(self):
        
        
        try:
            assert self.biomagnetisServicemObj.is_all_doctors_details_are_correct()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Doctor's Email Address, Phone Number, Website visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Doctor's Email Address, Phone Number, Website visibility Is Failed"):
                assert False

    
    @allure.title("Test Case 18 : Therapy With Dr. Garcia Button is clickable and redirecting to related page") 
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, in dropdown, therapy with dr garcia is clickable and navigate to respective page
    
    <br><br><b>Expeceted Results:</b>
    <br><br>when mouse hovered on biomagnetism services, dropdown will be displayed clicking on therapy with dr garcia should navigate top respective page  
    
    """)
    def test_therepy_with_dr_garcia_clickable_and_redirected(self):
        
        try:
            assert self.biomagnetisServicemObj.is_therepy_with_dr_garcia_clickable_and_redirected()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Load More Functionality Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Load More Functionality Is Failed"):
                assert False
    
    @allure.title("Test Case 19 : Appointment Contact Information") 
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, address with other cities and appointment dates and hours
    
    <br><br><b>Expeceted Results:</b>
    <br><br>address and contact deatils with appropriate appointment date and hours to be viewed
    
    """)
    def test_appointment_details_correct(self):
        
        try:
            assert self.biomagnetisServicemObj.is_appointment_details_correct()
        except:
            allure.attach(self.biomagnetisServicemObj.driver.get_screenshot_as_png(),name="Appointment Contact Information Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Appointment Contact Information Is Failed"):
                assert False

        