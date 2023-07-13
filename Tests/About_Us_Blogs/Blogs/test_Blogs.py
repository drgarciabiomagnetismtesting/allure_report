import pytest
from Tests.test_Base import BaseTest
from Pages.About_Us_Blogs.Blogs.Blogs import Blogs
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Blog Page Test Cases")
class TestBlogs(BaseTest):

    global blogObj

    @allure.title("Test Case 9 : Blog Page Redirecting and Blog Visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that Blogs option on header part should be clickable and below on the page FAQ , PODCASTS and RESEARCH option should be there. 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Open the respective page there blogs related to diseases should load with images and when clicked on read more button should open particular blog page. Below Blogs page pagination should there when clicked  should take to next page and vice versa. 
    
    """)
    def test_blogs_visibility(self):
        TestBlogs.blogObj = Blogs(self.driver,self.wait)
        try:
            blog_page_redirect_status = self.blogObj.get_blog_page_redirecting_status()
            all_blogs_status = self.blogObj.get_blogs_visible_status()
            if blog_page_redirect_status and all_blogs_status:
                
                assert True
            else:
                
                assert False
        except:
            allure.attach(TestBlogs.blogObj.driver.get_screenshot_as_png(),name="Blog Page Redirecting and Blog Visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Blog Page Redirecting and Blog Visibility Is Failed"):
                assert False
    

    @allure.title("Test Case 10 : Read More Page Element Visibility And Form Working Status")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that when clicked on read more for any disease it should load the page and on top right side of the the page "Search" option should work , should have "Recent Posts" and Category and  on footer part "Leave a Comment" frame should be there which has *comment box , *Name , *Email , Website , fields.  Below "Post Comment" button should be there.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Navigate to detailed disease page, search box should show result related to disease name, and below the page when clicked on "Post a comment" after filling all the fields it should show "thank you" message.
    
    """)
    def test_read_more_page(self):
        try:
            read_more_elements_status = self.blogObj.check_read_more_page_element_visibility_status()
            search_option_working_status = self.blogObj.check_search_action_working_status("Biomagnetism")
            post_comment_status = self.blogObj.check_post_comments("Kishore","test@gmail.com","https://www.vmokshagroup.com/")
            
            if read_more_elements_status and search_option_working_status and post_comment_status:
                assert True
            else:
                assert False
        except:
            allure.attach(TestBlogs.blogObj.driver.get_screenshot_as_png(),name="Read More Page Element Visibility And Form Working Status Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Read More Page Element Visibility And Form Working Status Is Failed"):
                assert False
    
    @allure.title("Test Case 11 : FAQ Page Redirecting Status")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that on blogs page footer part "FAQ" link should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Navigate to page related to Biomagnetism FAQ and Links should there, once click on the link it should navigate the page to related query and answer.  
    
    """)
    def test_FAQ_page_is_redirecting(self):
        try:
            faq_status = self.blogObj.check_page_redirecting_status(page= "FAQ")
            assert faq_status
        except:
            allure.attach(TestBlogs.blogObj.driver.get_screenshot_as_png(),name="FAQ Visibility Status Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("FAQ Visibility Status Is Failed"):
                assert False
    @allure.title("Test Case 12 : PODCASTS Page Redirecting Status")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that on blogs page footer part "PODCASTS" link should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Navigate to page related to Biomagnetism PODCASTS and Links should there, once click on the link it should navigate the page to related query and answer.  
    
    """)
    def test_podcasts_page_is_redirecting(self):
        try:
            podcast_status = self.blogObj.check_page_redirecting_status(page= "PODCASTS")
            assert podcast_status
        except:
            allure.attach(TestBlogs.blogObj.driver.get_screenshot_as_png(),name="Podcasts Visibility Status Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Podcasts Visibility Status Is Failed"):
                assert False
    
    @allure.title("Test Case 13 : Research Page Redirecting Status")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Verify that on blogs page footer part "RESEARCH" link should be clickable
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Navigate to page related to Biomagnetism RESEARCH and should load content related to biomagnetism research. When clicked on link it should open page related to that research.
    
    """)
    def test_research_page_is_redirecting(self):
        try:
            research_status = self.blogObj.check_page_redirecting_status(page= "RESEARCH")
            assert research_status
        except:
            allure.attach(TestBlogs.blogObj.driver.get_screenshot_as_png(),name="RESEARCH Visibility Status Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("RESEARCH Visibility Status Is Failed"):
                assert False
            