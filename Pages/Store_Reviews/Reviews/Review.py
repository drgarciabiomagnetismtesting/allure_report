from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.Store_Reviews.Reviews.ReviewElements import ReviewElements
import time
import allure



class Review(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)
    
    @allure.step("Checking Reviews Button Visibility")
    def check_review_button_visibility(self):
        reviews = self.get_text_from_element_only(ReviewElements.review_button)
        if "REVIEWS" in reviews:
            with allure.step("Reviews Button Visible"):
                return True
        else:
            with allure.step("Reviews Button Is Not Visible"):
                return False
    
    @allure.step("Checking Reviews Button Redirecting To Reviews Page")
    def check_review_button_redirecting_to_reviews_page(self):
        with allure.step("Clicked On Reviews"):
            self.do_click(ReviewElements.review_button)
        
        with allure.step("Checking Reviews Page Visibility"):
            review_body = self.get_text_from_element_only(BasePageElements.body)

            if "Client Reviews" in review_body:
                with allure.step("Reviews Page Is Visible"):
                    return True
            else:
                with allure.step("Reviews Page Is Not Visible"):
                    return False
    
    @allure.step("Checking Client Reviews visibility")
    def check_client_reviews_in_visible_in_reviews_page(self):
        with allure.step("Taking Body Of Reviews Page"):
            review_body = self.get_text_from_element_only(BasePageElements.body)

            if "Client Reviews" in review_body:
                with allure.step("Client Reviews Is Visible"):
                    return True
            else:
                with allure.step("Client Reviews Is Not Visible"):
                    return False
    
    @allure.step("Checking All Desises Visibility  ")
    def check_visibility_of_desises(self):
        desises = ["All",
        "Lyme Disease",
        "Thyroid Cancer",
        "Back Pain",
        "PANDAS Syndrome",
        "Autism Spectrum Disorder",
        "Depression",
        "Extreme Allergies",
        "Severe Insomnia",
        "Flu",
        "Sport Injuries",
        "Traumatic Brain Injuries",
        "Bronquitis",
        "Shattered Spine",
        "Foot Pain",
        "Yeast Infection",
        "Spine Injury",
        "Rhabdomyolysis",
        "Terrible Back Pain",
        "Ehlers Danlos Symdrome",
        "Meniere’s Disease",
        "T- cell Lymphoma",
        "Shoulder Pain",
        "Brachial Plexus Injury",
        "Significant Changes",
        "Chronic Illness",
        "Leg Pain",
        "Difficulty in Walking"
        ]

        with allure.step("Taking all desises"):
            desisesElements = self.get_elements(ReviewElements.all_disease)

        with allure.step("Checking all desises filter visibility"):
            for element in desisesElements:
                if element.text not in desises:
                    with allure.step("Some Desises Are Missing"):
                        return False

        with allure.step("Checking Disease Buttons Working Functionality"):
            for desise in desises:
                if desise == "All":
                    continue
                desise_button,desise_list = ReviewElements.get_each_disease_xpath(desise)

                with allure.step(f"Clicked On {desise}"):
                    self.do_click(desise_button)
                    time.sleep(2)
                    with allure.step("Checking Each Video Category"):
                        desise_heading_list = self.get_elements(desise_list)
                        for desise_heading in desise_heading_list:
                            if desise_heading.text != desise:
                                with allure.step("Some desises are not showing according to the desired filter"):
                                    return False
        with allure.step("Clicked On All"):
            desise_button,desise_list = ReviewElements.get_each_disease_xpath("All")
            self.do_click(desise_button)
            time.sleep(2)
            
        with allure.step("All Desises Are Visible And Showing According To The Selected Filter"):
            return True
        
    def get_details_from_youtube_embed_video(self,element,iframe_screen):
        with allure.step("Clicked On Play Button"):
            self.do_scroll_to_element_only(element)
            time.sleep(2)
            self.do_click_to_element_by_offset(element,100,0)
            
        with allure.step("Scroll to YouTube embed video"):
            self.do_scroll_to_element(iframe_screen)
        
        with allure.step("Switch to video embeded frame"):
            iframe_element = self.get_element(iframe_screen)
            self.driver.switch_to.frame(iframe_element)
        with allure.step("Clicked On Pause Button"):
            self.do_click_only(ReviewElements.yt_play_pause_btn)
            self.do_move_cursor_to_element_only(ReviewElements.yt_play_pause_btn)
            self.do_click_only(ReviewElements.yt_play_pause_btn)
            time.sleep(5)
            self.do_click_only(ReviewElements.yt_play_pause_btn)
        
        with allure.step("Checking Video Is Play Or Not"):
            # time.sleep(5)
            current_time = self.get_text_from_element_only(ReviewElements.video_current_progress)
            current_time = int(current_time.split(":")[-1])
            self.driver.switch_to.default_content()
            if current_time > 0:
                with allure.step("Video is playing...."):
                    return True
            else:
                with allure.step("Video is not playing...."):
                    return False

    def check_is_video_playing(self,video_index,element):
        video_iframe = ReviewElements.get_iframe_xpath(video_index)

        with allure.step(f"Checking Video {video_index} Is Play Or Not"):
            video_status = self.get_details_from_youtube_embed_video(element,video_iframe)
        return video_status

    def get_all_videos_status(self):

        with allure.step("Getting All Videos Elements"):
            all_videos = self.get_elements(ReviewElements.all_review_videos)
        
        with allure.step("Checking Each Video Is Play Or Not"):
            for index in range(len(all_videos)):
                video_element = all_videos[index]
                video_index = index + 1
                if not self.check_is_video_playing(video_index,video_element):
                    with allure.step("Some Videos Are Not Playing"):
                        return False
            with allure.step("All Videos Are Playing"):
                return True

        


