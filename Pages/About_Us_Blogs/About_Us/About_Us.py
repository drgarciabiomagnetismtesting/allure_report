from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.About_Us_Blogs.About_Us.About_Us_Elements import AboutUsElements
import time
import allure



class AboutUs(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)

    def check_visibility_of_element(self,checking_element,element_locator,element_value):
        with allure.step(f"Checking {checking_element}"):
                element_text = self.get_text_from_element(element_locator)
               
                if element_value.lower() in element_text.lower():
                    with allure.step(f"{checking_element} is visible"):
                        return True
                else:
                     with allure.step(f"{checking_element}  is not visible"):
                        return False

    def get_details_from_youtube_embed_video(self):
        with allure.step("Clicked On Play Button"):
            self.do_click_only(AboutUsElements.custom_play_button)
        
        

        with allure.step("Scroll to YouTube embed video"):
            self.do_scroll_to_element(AboutUsElements.youtube_screen)
        
        with allure.step("Switch to video embeded frame"):
            element = self.get_element(AboutUsElements.youtube_screen)
            self.driver.switch_to.frame(element)
        with allure.step("Clicked On Pause Button"):
            self.do_click_only(AboutUsElements.yt_play_pause_btn)
            self.do_move_cursor_to_element_only(AboutUsElements.yt_play_pause_btn)
            self.do_click_only(AboutUsElements.yt_play_pause_btn)
            time.sleep(5)
        
        
        
        # with allure.step("Move The Cursor To Play Button"):
        #     for i in range(0,30):
        #         time.sleep(0.5)
        #         self.do_move_cursor_to_element_only(AboutUsElements.youtube_screen2)
        
        with allure.step("Checking Video Is Play Or Not"):
            # time.sleep(5)
            current_time = self.get_text_from_element_only(AboutUsElements.video_current_progress)
            current_time = int(current_time.split(":")[-1])
            self.driver.switch_to.default_content()
            if current_time > 0:
                with allure.step("Video is playing...."):
                    return True
            else:
                with allure.step("Video is not playing...."):
                    return False


    def get_status_of_video(self):
        with allure.step("Checking video status before click on play button"):
            play_button_visibility_status = self.get_element_visibility_div(AboutUsElements.custom_play_button)
            if play_button_visibility_status:
                with allure.step("Video is not play automatically "):
                    with allure.step("Taking Video Playing Status"):
                        return self.get_details_from_youtube_embed_video()
                        

    @allure.step("Checking Welcome Video Page Visiblity")
    def check_welcome_page_visibility(self):

        try:

            with allure.step("Move Cursor To About Us Button"):
                self.do_move_cursor_to_element_only(AboutUsElements.about_us)
            
            with allure.step("Clicked On Welcome Video Button"):
                self.do_move_cursor_to_element_only(AboutUsElements.welcome_video_button)
                self.do_click_only(AboutUsElements.welcome_video_button)
            
            with allure.step("Taking Welcome Video Page Content"):
                welcome_video_page = self.get_element_visibility(BasePageElements.body)

                youtube_welcome_video_status = self.get_status_of_video()

                articles_and_working_papers_status = self.check_visibility_of_element("Articles and Working Papers",
                                                                    AboutUsElements.article_workpapper,
                                                                    "Articles & Working Papers"
                                                                    )
                
                interviews_status = self.check_visibility_of_element("Interviews",
                                                                    AboutUsElements.interviews,
                                                                    "Interviews"
                                                                    )

                research_status = self.check_visibility_of_element("Research Experiences",
                                                                    AboutUsElements.research,
                                                                    "Research Experiences"
                                                                    )
                
              


            if articles_and_working_papers_status and interviews_status and youtube_welcome_video_status and research_status:
                with allure.step("Video Play After Click Play Button"):
                    return True
            else:
                with allure.step("Video Play Automatically"):
                    return False
        except Exception as e:
            print(f"Error : {e}")
    
    # def get_articles_and_working_papers_element_status(self,element_locator,element_value):
    #     article_work_paper_body = self.get_text_from_element(BasePageElements.body)

    @allure.step("Check Visibility of Bio, Interviews and Research Expriences In Article And Work Paper Page")
    def get_articles_and_working_papers_visibility(self,dropdown_status=0):
        if dropdown_status == 1:
            with allure.step("Move Cursor To About Us Button"):
                self.do_move_cursor_to_element_only(AboutUsElements.about_us)
            with allure.step("Clicked On Article And Work Paper"):
                self.do_click(AboutUsElements.article_work_paper_dropdown)
        else:
            with allure.step("Clicked On Article And Work Paper"):
                self.do_click(AboutUsElements.article_workpapper)
        
        article_work_paper_body = self.get_text_from_element(BasePageElements.body)
        with allure.step("Checking Visibility Of Bio"):
            bio = self.check_visibility_of_element("Bio",
                                                AboutUsElements.bio,
                                                "BIO")
        with allure.step("Checking Visibility Of Interviews"):
            interview = self.check_visibility_of_element("Interviews",
                                                AboutUsElements.interviews,
                                              "INTERVIEWS")

        with allure.step("Checking Visibility Of Research Experiences"):                               
            research = self.check_visibility_of_element("Research Experiences",
                                                AboutUsElements.research,
                                                "Research Experiences".upper())

           
        if bio and interview and research:
            with allure.step("All Elements Are Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return True
        else:
            with allure.step("All Elements Are Not Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return False

    
    
    @allure.step("Check Visibility of  Articles and Working Papers , Bio, Research and Experience Interviews Page")
    def get_interviews_visibility(self,dropdown_status=0):

        if dropdown_status == 1:
           with allure.step("Move Cursor To About Us Button"):
               self.do_move_cursor_to_element_only(AboutUsElements.about_us)
           with allure.step("Clicked On Article And Work Paper"):
               self.do_click(AboutUsElements.interviews_dropdown)
        else:  
            with allure.step("Clicked On Interviews"):
                self.do_click(AboutUsElements.interviews)
        
        article_work_paper_body = self.get_text_from_element(BasePageElements.body)
        with allure.step("Checking Visibility Of Articles and Working Papers"):
            article = self.check_visibility_of_element("Articles and Working Papers",
                                                AboutUsElements.article_workpapper,
                                                "Articles & Working Papers".upper())
        with allure.step("Checking Visibility Of Bio"):
            bio = self.check_visibility_of_element("BIO",
                                                AboutUsElements.bio,
                                              "BIO".upper())

        with allure.step("Checking Visibility Of Research Experiences"):                               
            research = self.check_visibility_of_element("Research Experiences",
                                                AboutUsElements.research,
                                                "Research Experiences".upper())

           
        if article and bio and research:
            with allure.step("All Elements Are Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return True
        else:
            with allure.step("All Elements Are Not Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return False

    
    @allure.step("Check Visibility of  Articles and Working Papers , Bio, Interviews  In Research and Experience Page")
    def get_research_and_exprience_visibility(self,dropdown_status=0):

        if dropdown_status == 1:
           with allure.step("Move Cursor To About Us Button"):
               self.do_move_cursor_to_element_only(AboutUsElements.about_us)
           with allure.step("Clicked On Article And Work Paper"):
               self.do_click(AboutUsElements.research_dropdown)
        else:
            with allure.step("Clicked On Research and Experience"):
                self.do_click(AboutUsElements.research)
        
        research_body = self.get_text_from_element(BasePageElements.body)
        with allure.step("Checking Visibility Of Articles and Working Papers"):
            article = self.check_visibility_of_element("Articles and Working Papers",
                                                AboutUsElements.article_workpapper,
                                                "Articles & Working Papers".upper())
        with allure.step("Checking Visibility Of Bio"):
            bio = self.check_visibility_of_element("BIO",
                                                AboutUsElements.bio,
                                              "BIO".upper())

        with allure.step("Checking Visibility Of Interviews"):                               
            interviews = self.check_visibility_of_element("Interviews",
                                                AboutUsElements.interviews,
                                                "INTERVIEWS".upper())

           
        if article and bio and interviews:
            with allure.step("All Elements Are Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return True
        else:
            with allure.step("All Elements Are Not Showing "):
                with allure.step("redirecting to to About Us"):
                    self.driver.back()
                return False

    
    

        



        


