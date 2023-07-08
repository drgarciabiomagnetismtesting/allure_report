
import pytest
from Tests.test_Base import BaseTest
from Pages.HomePage_ContactUs.Footer.Footer import Footer
from Config.config import TestData
from CheckSSLCert import validate

import allure



@allure.title("Home Page Test Cases")
class TestFooter(BaseTest):
    global FooterObj


    @allure.title("Test Case 13 : Footer Element (Recent Posts, Subscribe, Update,Contact Details Visibility Testing)")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the footer page is having the recent posts , Subscribe,updates ,contact details 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Recent posts option should be with updated post.
    
    """)
    def test_footer_element(self):
        TestFooter.FooterObj = Footer(self.driver,self.wait)

        try:
            contact_element = TestFooter.FooterObj.get_contact_elements()
            recent_posts = TestFooter.FooterObj.get_recent_posts_elements()
            updates = TestFooter.FooterObj.get_update_and_subscribe_elements()

            if contact_element and recent_posts and updates:

                with allure.step("Contact Element, Recent Posts, Update & Subscribe Elements Are Visible"):
                    assert True
            else:
                with allure.step("Contact Element, Recent Posts, Update & Subscribe Elements Are Not Visible"):
                    assert False
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Footer Elements are not visible"):
                assert False

    @allure.title("Test Case 14 : News Latter Subscription Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the footer page is having subscribe filed  is taking the data and showing output like thank you message .
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Subcribe should be taking the data and gives with reply of thanks message.
    
    """)
    def test_news_latter_subscription(self):
        try:
            news_latter_subscription_status = TestFooter.FooterObj.get_news_latter_subscription_status()

            assert news_latter_subscription_status
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png,name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("News Latter Subscrition Failed"):
                assert False
    
    @allure.title("Test Case 15 : Recent Post Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the footer page is having updated posts 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Updated posts is should give the update regarding seminar related, blogs,notification 
    
    """)
    def test_recent_post(self):
        try:
            recent_post_visibility_status = TestFooter.FooterObj.get_recent_post_status()
            assert recent_post_visibility_status
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Recent Post Visibility Failed"):
                assert False
    
    @allure.title("Test Case 16 : Contact Details,Email Address,Location,Social Media Links Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the footer page is having  contact details , location ,contact number ,Socilal media links  is correct or not
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Contact us option should  be navigate to the detail page of contact. location icon is should open with google map
    
    """)
    def test_contact_details_and_social_media_link(self):
        try:
            contact_details_status = TestFooter.FooterObj.get_contact_details_status()
            social_media_link_status = TestFooter.FooterObj.get_social_media_links_status()
            
            if contact_details_status and social_media_link_status:
                with allure.step("Contact Details,Location,Email Address And Social Media Links Are Visible And Valid"):
                    assert True
            else:
                with allure.step("Contact Details,Location,Email Address And Social Media Links Are Not Visible And Valid"):
                    assert False
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Contact Details,Location,Email Address And Social Media Links Visibility Failed"):
                assert False
    
    @allure.title("Test Case 18 : Copyrights and Designed By Rights Testing ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the copyright is present or not designed by is present or not.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Copyright is should have the copyright protected material. 
    
    """)
    def test_copyrights_and_designed_by_rights(self):
        try:
            copyrights_designed_by_rights_status = TestFooter.FooterObj.get_copyright_and_design_by_status()
            
            assert copyrights_designed_by_rights_status
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Copyrights and Designed By Rights Failed"):
                assert False
    
    @allure.title("Test Case 19 : Privacy Policy Testing ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the privacy policy is present along with the related content or not .
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Privacy policy should have the policies and procedures.etc.
    
    """)
    def test_privacy_policy(self):
        try:
            privacy_policy = TestFooter.FooterObj.get_privacy_policy_status()
            assert privacy_policy
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="Footer Element Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Privacy Policy Failed"):
                assert False

    allure.title("Test Case 20 : DB Testing ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the DB is Clickable or not
    
    <br><br><b>Expeceted Results:</b>
    <br><br>DB should be open while entering the  validate credentilas 
    
    """)
    def test_DB(self):
        try:
            DB_status = TestFooter.FooterObj.get_DB_status()
            assert DB_status
        except:
            allure.attach(self.FooterObj.driver.get_screenshot_as_png(),name="DB Status Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("DB Status Failed"):
                assert False






        





