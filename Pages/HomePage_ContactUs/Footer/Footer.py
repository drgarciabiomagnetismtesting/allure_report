from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.HomePage_ContactUs.Footer.FooterElements import FooterElements
import time
import allure

class Footer(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)

    @allure.step("Taking Contact Elements")
    def get_contact_elements(self):

        contanct = self.get_text_from_element(FooterElements.contacts)

        if "info@drgarciabiomagnetism.com" in contanct:
            with allure.step("Contact Element is visible"):
                return True
        else:
            with allure.step("Contact Element is not visible"):
                return False
    
    @allure.step("Taking Recent Posts Elements")
    def get_recent_posts_elements(self):

        recent_posts = self.get_text_from_element(FooterElements.recent_posts)

        if "RECENT POSTS" in str(recent_posts).upper():
            with allure.step("Recent Posts Element is visible"):
                return True
        else:
            with allure.step("Recent Posts Element is not visible"):
                return False
    
    @allure.step("Taking Updates and Subscribe Elements")
    def get_update_and_subscribe_elements(self):

        update_subscribe = self.get_text_from_element(FooterElements.updates)

        if "UPDATES" in str(update_subscribe).upper():
            with allure.step("Updates and Subscribe Element is visible"):
                return True
        else:
            with allure.step("Updates and Subscribe Element is not visible"):
                return False
    
    @allure.step("Taking News Latter Subscription Elements")
    def get_news_latter_subscription_status(self):
        
        with allure.step("Entering Email Id For News Latter Subscription"):
            self.do_send_keys(FooterElements.email_input,TestData.test_email)
        
        with allure.step("Clicked On Subscribe Button"):
            self.do_click(FooterElements.subscribe_button)

        subscription_done_msg = self.get_text_from_element(FooterElements.subscription_success)

        if "Thanks for signing up for the newsletter! We'll be" in subscription_done_msg:
            with allure.step("News Latter Subscription Is Success"):
                return True
        else:
            with allure.step("News Latter Subscription Is Failed"):
                return False
    
    @allure.step("Taking Recent Posts Elements")
    def get_recent_post_status(self):

        with allure.step("Taking all recent posts elements"):
            recent_posts = self.get_elements(FooterElements.recent_post_elements)
        
        with allure.step("checking each recent post"):
            for post in recent_posts:
                if bool(post):
                    post_screenshot = post.screenshot_as_png
                    allure.attach(post_screenshot,name="recent_posts",attachment_type= allure.attachment_type.PNG)
                    continue
                else:
                    with allure.step("Some post are not visible"):
                        return False
        with allure.step("Recent posts are visible"):
            return True
    @allure.step("Verifying Details")
    def verify_element_details(self,title,value,value_locator,value_type):
        with allure.step(title):
            return_value = self.get_text_from_element(value_locator)
            if value in return_value:
                with allure.step(f"{value_type}  Checked"):
                    return True
            else:
                with allure.step(f"{value_type}  Checked"):
                    return False



    @allure.step("Taking Contact Details")
    def get_contact_details_status(self):


        locations_status = self.verify_element_details("Taking Location",
                                                        "138 Riverbend Drive, North Brunswick, NJ 08902",
                                                        FooterElements.location,
                                                        "Location Details"
                                                        )

        contact_number_status = self.verify_element_details("Taking Contact Number",
                                                        "732-983-8616",
                                                        FooterElements.contact_no,
                                                        "Contact Number"
                                                        )

        email_id_status = self.verify_element_details("Taking Email Address",
                                                        "info@drgarciabiomagnetism.com",
                                                        FooterElements.email_id,
                                                        "Email Id"
                                                        )

        if locations_status and contact_number_status and email_id_status:
            return True
        else:
            return False
       

    @allure.step("Checking Social Media Link")
    def check_social_media_link_status(self,social_media_link,social_media_locator,social_media_name):
        social_media = self.get_tag_a_src(social_media_locator)
        if social_media_link == social_media:
            with allure.step(f"{social_media_name} {social_media} Link Is Valid"):
                return True
        else:
            with allure.step(f"{social_media_name} {social_media} Link Is Not Valid"):
                return False


    @allure.step("Taking Social Media Link")
    def get_social_media_links_status(self):

        facebook_link ="https://www.facebook.com/AmericanBiomagnetism/"
        twitter_link = "https://twitter.com/thebiomagnetism"
        pinterest_link = "https://www.pinterest.com/DrGarciaBiomagnetism/"
        linkedin_link = "https://www.linkedin.com/company/luis-f-garcia/"
        instagram_link = "https://www.instagram.com/drgarciabiomagnetism/"
        youtube_link = "https://www.youtube.com/channel/UCFGfG5Wc9SGhbG-o5p6Xhag"

        
        facebook_link_status = self.check_social_media_link_status(facebook_link,FooterElements.facebook,"Facebook")
        
        twitter_link_status = self.check_social_media_link_status(twitter_link,FooterElements.twitter,"Twitter")

        pinterest_link_status = self.check_social_media_link_status(pinterest_link,FooterElements.pinterest,"Pinterest")

        linkedin_link_status = self.check_social_media_link_status(linkedin_link,FooterElements.linkedin,"Linkedin")

        instagram_link_status = self.check_social_media_link_status(instagram_link,FooterElements.instagram,"Instagram")

        youtube_link_status = self.check_social_media_link_status(youtube_link,FooterElements.youtube,"Youtube")
        
        if facebook_link_status and twitter_link_status and pinterest_link_status and linkedin_link_status and instagram_link_status and youtube_link_status:
            return True
        else: 
            return False
    
    @allure.step("Checking Copyright and Designed By Status")
    def get_copyright_and_design_by_status(self):

        copyright_element = self.get_text_from_element(FooterElements.copyright)
        if "Copyright © 2023 eGrow Plants | Designed by Helenzys Inc" in copyright_element:
            with allure.step("Copyrights And Design By Rights Is Valid"):
                return True
        else: 
            with allure.step("Copyrights And Design By Rights Is Not Valid"):
                return False
       
    @allure.step("Checking Privacy Policy")
    def get_privacy_policy_status(self):
        self.do_click(FooterElements.privacy_policy)
        privacy_policy_element = self.get_text_from_element(FooterElements.privacy_policy_heading)
        if "PRIVACY POLICY" in str(privacy_policy_element).upper():
            with allure.step("Privacy Policy Page Is Available"):
                return True
        else: 
            with allure.step("Privacy Policy Page Is Not Available"):
                return False
    
    @allure.step("Checking DB")
    def get_DB_status(self):
        with allure.step("Clicked on DB"):
            self.do_click(FooterElements.DB)
        with allure.step("Switch To New Tab"):
            self.driver.switch_to.window(self.driver.window_handles[1])
        title = self.get_title()
        self.driver.switch_to.window(self.driver.window_handles[0])
        if "Dr.Garcia backend" in title:
            with allure.step(f"DB Website Is Opened title : {title}"):
                return True
        else: 
            with allure.step("DB Website Is Not Opened"):
                return False

        

        


    

    

    
