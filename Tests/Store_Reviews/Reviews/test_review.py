import pytest
from Tests.test_Base import BaseTest
from Pages.Store_Reviews.Reviews.Review import Review
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Blog Page Test Cases")
class TestReview(BaseTest):

    global reviewObj

    @allure.title("Test Case 14 : Reviews Button Visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Reviews link is present in the header or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Reviews text should be present in the header.
    
    """)
    def test_reviews_button_visibility(self):
        TestReview.reviewObj = Review(self.driver,self.wait)
        try:
            assert self.reviewObj.check_review_button_visibility()
        except:
            allure.attach(TestReview.reviewObj.driver.get_screenshot_as_png(),name="Reviews Button Visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Reviews Button Visibility Is Failed"):
                assert False
    

    @allure.title("Test Case 15 : Reviews Page Redirecting Or Not")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that if we click on Reviews link in the header it is navigating to reviews list page or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>User click on reviews link in the header it should navigate to list of reviews page.
    
    """)
    def test_reviews_page_redirection(self):
        
        try:
            assert self.reviewObj.check_review_button_redirecting_to_reviews_page()
        except:
            allure.attach(TestReview.reviewObj.driver.get_screenshot_as_png(),name="Reviews Page Redirecting Or Not Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Reviews Page Redirecting Or Not Is Failed"):
                assert False
    
    @allure.title("Test Case 16 : Client Review Visibility In Reviews Page")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Reviews list page in the banner "Clinte Review" text is present or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>"Clinte Review " text should be present in the banner of reviews list page.
    
    """)
    def test_client_reviews_visibility(self):
 
        try:
            assert self.reviewObj.check_client_reviews_in_visible_in_reviews_page()
        except:
            allure.attach(TestReview.reviewObj.driver.get_screenshot_as_png(),name="Client Review Visibility In Reviews Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Client Review Visibility In Reviews Page Is Failed"):
                assert False
    

    @allure.title("Test Case 17 : All Desises Button Visibility And Working Functionality")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Clinte review page all desises button are present and it is working as expected?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All the desises button should be present in the clinte review page and it should clickable and navigate to corresponding detail page.
    
    """)
    def test_all_desises_button_visibility(self):
 
        try:
            assert self.reviewObj.check_visibility_of_desises()
        except:
            allure.attach(TestReview.reviewObj.driver.get_screenshot_as_png(),name="All Desises Button Visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("All Desises Button Visibility Is Failed"):
                assert False
    
    @allure.title("Test Case 18 : All Review Videos Playing Or Not")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that all the clinte review videos are present and it is playing in the clinte review page?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All the clinte reviews videos should be present and if we click on that it should play in the clinte reviews page.
    
    """)
    def test_all_review_videos_playing_or_not(self):
 
        try:
            assert self.reviewObj.get_all_videos_status()
        except:
            allure.attach(TestReview.reviewObj.driver.get_screenshot_as_png(),name="All Review Videos Playing Or Not Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("All Review Videos Playing Or Not Is Failed"):
                assert False
