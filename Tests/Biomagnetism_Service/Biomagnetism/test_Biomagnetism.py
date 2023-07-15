import pytest
from Tests.test_Base import BaseTest
from Pages.Biomagnetism_Service.Biomagnetism.Biomagnetism import Biomagnetism
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Biomagnetism Tests")
class TestBiomagnetism(BaseTest):

    global biomagnetismObj

    @allure.title("Test Case 1 : Is 'What is biomagnetism' button  clickable")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate, What is biomagnetism is clickable  
    
    <br><br><b>Expeceted Results:</b>
    <br><br>what is biomagnetism should be clicked
    
    """)
    def test_what_is_biomagnetism_clickable(self):
        TestBiomagnetism.biomagnetismObj = Biomagnetism(self.driver,self.wait)
        try:
            assert self.biomagnetismObj.is_what_is_biomagnetism_button_clickable()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Is 'What is biomagnetism' button  clickable Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Is 'What is biomagnetism' button  clickable Is Failed"):
                assert False
    
    @allure.title("Test Case 2 : Is 'What is biomagnetism' button redirecting to the related page")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, clicking on what is biomagnetism  displays the content of it and 4 submodules in button  and should be clickable  
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Contents should be viewed and submodules should be in button format and should be clickable
    
    """)
    def test_is_what_is_biomagnetism_redirected(self):
        try:
            page_redirect_status = self.biomagnetismObj.is_what_is_biomagnetism_redirected_to_related_page()
            submodule_status = self.biomagnetismObj.is_4_submodules_are_visible()

            if page_redirect_status and submodule_status:
                assert True
            else:
                assert False
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="What is biomagnetism' button redirecting to the related page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("What is biomagnetism' button redirecting to the related page Is Failed"):
                assert False
    

    @allure.title("Test Case 3 : Check Submodules pages are redirecting to related page")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, detailed page of what is biomagnetism contains 4 submodules in form of button are naviagting to its respective page or not 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>submodules are clickable and navigating to respective page
    
    """)
    def test_submodules_redirecting_to_related_page(self):
        
        try:
            assert self.biomagnetismObj.is_4_submodules_redirected_to_related_pages()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Check Submodules pages are redirecting to related page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Check Submodules pages are redirecting to related page Is Failed"):
                assert False
    

    @allure.title("Test Case 4 : Check 3 submodules are present in each submodule")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, in submodule detail page, except current page other 3 submodules are present in every submodule in button form
    
    <br><br><b>Expeceted Results:</b>
    <br><br>when clicked on any submodule, it details page should be displayed and in the bottom of the page other 3 modules should be displayed and should be clickable
    
    """)
    def test_3_submodules_present_in_each_submodule(self):
        
        try:
            assert self.biomagnetismObj.is_submodules_present_in_each_page()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Check 3 submodules are present in each submodule Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Check 3 submodules are present in each submodule Is Failed"):
                assert False


    @allure.title("Test Case 5 : What is biomagnetism dropdown element visibility and clickability")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, if mouse hovered on what is biomagnetism, submodules should be diplayed in the form of dropdown and should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>When mouse hovered on what is biomagnetsim, dropdown should happen and submodules should be displayed and should be clickable
    
    """)
    def test_dropdown_of_what_is_biomagnetism(self):
        
        try:
            assert self.biomagnetismObj.is_biomagnestism_dropdown_visible_and_clickable()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="what is biomagnetism dropdown element visibility and clickability Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("what is biomagnetism dropdown element visibility and clickability Is Failed"):
                assert False
    
    @allure.title("Test Case 6 : FAQs Banner and Banner Content visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, page consists of banner image and banner text as per requirement
    
    <br><br><b>Expeceted Results:</b>
    <br><br>banner image and banner text should be placed on top of the page
    
    """)
    def test_faq_banner_and_content_visible(self):
        
        try:
            assert self.biomagnetismObj.is_faq_banner_and_content_visible()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="FAQs Banner and Banner Content visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("FAQs Banner and Banner Content visibility Is Failed"):
                assert False
    
    @allure.title("Test Case 7 : 3 FAQs Submodule visibility and clickability")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, there are four sections called biomagnetsim, biomagnetsim sessions, learning biomagnetsim and products with some questions
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In FAQ page, there should be with 4 sections and all sections should contains few questions
    
    """)
    def test_submodule_of_faq_visible_and_clickable(self):
        
        try:
            assert self.biomagnetismObj.is_3_submodule_of_faq_visible_and_clickable()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="3 FAQs Submodule visibility and clickability Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("3 FAQs Submodule visibility and clickability Is Failed"):
                assert False
    

    @allure.title("Test Case 8 : Research Page and It's Content")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, detailed page contains about the research published, magzines published and clinical case studies
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All about the research's done by the scholars with their name and date of publications are found
    
    """)
    def test_research_contains_related_content(self):
        
        try:
            assert self.biomagnetismObj.is_research_contains_related_content()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Research Page and It's Content Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Research Page and It's Content Is Failed"):
                assert False
    

    @allure.title("Test Case 9 : Biomagnetism therapy session Page and It's Content")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, contents are added all about the biomagnetism therapy session 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In biomagnetism therapy sessions contents are related to biomagnetism therapy should be displayed
    
    """)
    def test_biomagnetism_therapy_session_contains_related_content(self):
        
        try:
            assert self.biomagnetismObj.is_biomagnetism_therapy_session_contains_related_content()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Biomagnetism therapy session Page and It's Content Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Biomagnetism therapy session Page and It's Content Is Failed"):
                assert False
    

    @allure.title("Test Case 10 : Biomagnetsim vs magnet therapy Page and It's Content")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>validate, contents are added all about the biomagnetism vs manegt therapy 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>In biomagnetism vs magnet therapy, all contents should be related to biomagnetism and magnet therapy
    
    """)
    def test_biomagnetism_vs_magnet_therapy_contains_related_content(self):
        
        try:
            assert self.biomagnetismObj.is_biomagnetism_vs_magnet_therapy_contains_related_content()
        except:
            allure.attach(self.biomagnetismObj.driver.get_screenshot_as_png(),name="Biomagnetsim vs magnet therapy Page and It's Content Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Biomagnetsim vs magnet therapy Page and It's Content Is Failed"):
                assert False




