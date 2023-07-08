import pytest
from Tests.test_Base import BaseTest
from Pages.About_Us_Blogs.About_Us.About_Us import AboutUs
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("About Page Test Cases")
class TestAboutUs(BaseTest):

    global aboutUsObj

    @allure.title("Test Case 1 : Welcome Video Page Redirecting and Welcome Video Not Play Automatically")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that When click on About Us "Welcome Video" option, it should navigate to the respective page.<br>Welcom video screen should load, and below the page Articles and Working Papers, Interviews , Research and Experience options should be there.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should play welcome video when clicked.
    
    """)
    def test_welcome_video_page_redirecting(self):
        TestAboutUs.aboutUsObj = AboutUs(self.driver,self.wait)
        try:
           
                with allure.step("Checking Welcome Video Page"):
                    welcome_video_page_status = self.aboutUsObj.check_welcome_page_visibility()
                    assert welcome_video_page_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Welcome Video Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Welcome Video Page Is Failed"):
                assert False
    
    @allure.title("Test Case 2 : Articles and Working Papers Redirecting ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Articles and Working Paper it should open the page,below the page, Bio, Interviews , Research and Experience option should clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the content and below the page Bio, Interviews , Research and Experience options should be there.
    
    """)
    def test_articles_and_working_papers_redirecting(self):
        try:
            with allure.step("Checking Articles and Working Papers Redirecting Status"):
                articles_and_working_papers_status = self.aboutUsObj.get_articles_and_working_papers_visibility()
            assert articles_and_working_papers_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Articles and Working Papers Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Articles and Working Papers Redirecting Is Failed"):
                assert False

    
    @allure.title("Test Case 3 : Interview Redirecting ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Interviews option it should open the page,below the page Articles and Working Papers , Bio, Research and Experience option should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the interview links and should open respective page.
    
    """)
    def test_interviews_redirecting(self):
        try:
            with allure.step("Checking Interview Redirecting Status"):
                interviews_status = self.aboutUsObj.get_interviews_visibility()
            assert interviews_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Interview Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Interview Redirecting Is Failed"):
                assert False
    
    @allure.title("Test Case 4 : Research And Expriences Redirecting ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Research and Experience  option it should open the page,below the page Articles and Working Papers , Bio, Research and Experience option should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the Research and Experience links and should open respective page.
    
    """)
    def test_research_and_exprience_redirecting(self):
        try:
            with allure.step("Checking Research And Expriences Redirecting Status"):
                interviews_status = self.aboutUsObj.get_research_and_exprience_visibility()
            assert interviews_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Research And Expriences Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Research And Expriences Is Failed"):
                assert False

    @allure.title("Test Case 6 : Articles and Working Papers Redirecting from About Us Dropdown")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Articles and Working Paper it should open the page,below the page, Bio, Interviews , Research and Experience option should clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the content and below the page Bio, Interviews , Research and Experience options should be there.
    
    """)
    def test_articles_and_working_papers_redirecting_from_droupdown(self):
        try:
            with allure.step("Checking Articles and Working Papers Redirecting Status"):
                articles_and_working_papers_status = self.aboutUsObj.get_articles_and_working_papers_visibility(dropdown_status=1)
            assert articles_and_working_papers_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Articles and Working Papers Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Articles and Working Papers Redirecting Is Failed"):
                assert False
    
    @allure.title("Test Case 7 : Interview Redirecting from About Us Dropdown ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Interviews option it should open the page,below the page Articles and Working Papers , Bio, Research and Experience option should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the interview links and should open respective page.
    
    """)
    def test_interviews_redirecting_from_droupdown(self):
        try:
            with allure.step("Checking Interview Redirecting Status"):
                interviews_status = self.aboutUsObj.get_interviews_visibility(dropdown_status= 1)
            assert interviews_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Interview Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Interview Redirecting Is Failed"):
                assert False
    
    @allure.title("Test Case 8 : Research And Expriences Redirecting from About Us Dropdown ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when click on Research and Experience  option it should open the page,below the page Articles and Working Papers , Bio, Research and Experience option should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Should navigate to the respective page , Page should have the Research and Experience links and should open respective page.
    
    """)
    def test_research_and_exprience_redirecting_from_droupdown(self):
        try:
            with allure.step("Checking Research And Expriences Redirecting Status"):
                interviews_status = self.aboutUsObj.get_research_and_exprience_visibility(dropdown_status= 1)
            assert interviews_status
        except:
            allure.attach(TestAboutUs.aboutUsObj.driver.get_screenshot_as_png(),name="Research And Expriences Redirecting Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Research And Expriences Is Failed"):
                assert False




