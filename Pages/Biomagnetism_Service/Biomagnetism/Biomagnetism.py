from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.Biomagnetism_Service.Biomagnetism.BiomagnetismElements import BiomagnetismElements
import time
import allure



class Biomagnetism(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)
    
    def check_visibility_and_clickable_of_element(self,checking_element,element_locator,element_value):
      with allure.step(f"Checking {checking_element}"):
              element_text = self.get_text_from_element(element_locator)
              with allure.step("Is Clickable"):
                element_status = self.get_element_clickable_status(element_locator)
                
             
              if element_value.lower() in element_text.lower() and element_status:
                  with allure.step(f"{checking_element} is visible and clickable"):
                      return True
              else:
                   with allure.step(f"{checking_element}  is not visible and clickable"):
                      return False
    def check_visibility_of_element(self,checking_element,element_locator,element_value):
      with allure.step(f"Checking {checking_element}"):
              element_text = self.get_text_from_element(element_locator)
             
              if element_value.lower() in element_text.lower():
                  with allure.step(f"{checking_element} is visible "):
                      return True
              else:
                   with allure.step(f"{checking_element}  is not visible "):
                      return False


    @allure.step("Checking What is biomagnetism button is clickable or not")
    def is_what_is_biomagnetism_button_clickable(self):

        button_status = self.get_element_clickable_status(BiomagnetismElements.biomagnetism)
        if button_status:
            with allure.step("What is biomagnetism button is clickable"):
                return True
        else:
            with allure.step("What is biomagnetism button is not clickable"):
                return False

    @allure.step("Checking Submodules Visibility")
    def is_4_submodules_are_visible(self):
        
        faq = self.check_visibility_and_clickable_of_element("FAQS",BiomagnetismElements.faq,"FAQS")
        blogs = self.check_visibility_and_clickable_of_element("BLOGS",BiomagnetismElements.blogs,"BLOGS")
        podcast = self.check_visibility_and_clickable_of_element("PODCASTS",BiomagnetismElements.podcast,"PODCASTS")
        research = self.check_visibility_and_clickable_of_element("RESEARCH",BiomagnetismElements.research,"RESEARCH")

        if faq and blogs and podcast and research:
            with allure.step("All Submodules are visible and clickable"):
                return True
        else:
            with allure.step("All Submodules are not visible and clickable"):
                return False
    



    def is_what_is_biomagnetism_redirected_to_related_page(self):

        with allure.step("Clicked On 'What is biomagnetism' button"):
            self.do_click(BiomagnetismElements.biomagnetism)
        
        with allure.step("Checking Content"):
            body_content = self.get_text_from_element(BasePageElements.body)
            if "What is Biomagnetism?" in body_content:
                with allure.step("What is Biomagnetism page is redirected and content also loaded"):
                    return True
            else:
                with allure.step("What is Biomagnetism page is not redirected and content also not loaded"):
                    return False
    
    def get_page_status(self,page,page_button_element,page_assert_value):
        with allure.step(f"Checking Page {page}"):
            with allure.step(f"Clicked On {page}"):
                self.do_click(page_button_element)
            
            with allure.step("Checking Content"):
                page = self.check_visibility_of_element(page,BasePageElements.body,page_assert_value)

            with allure.step("Back to What is biomagnetism page" ):
                self.driver.back()
            return page
    
    def get_submodule_status(self,page,page_button_element,element_1,element_1_value,element_2,element_2_value,element_3,element_3_value):
        with allure.step(f"Checking Page {page}"):
            with allure.step(f"Clicked On {page}"):
                self.do_click(page_button_element)
            
            with allure.step("Checking Submodules"):
                module_1 =  self.check_visibility_and_clickable_of_element(element_1_value,element_1,element_1_value)
                module_2 =  self.check_visibility_and_clickable_of_element(element_2_value,element_2,element_2_value)
                module_3 =  self.check_visibility_and_clickable_of_element(element_3_value,element_3,element_3_value)

            with allure.step("Back to What is biomagnetism page" ):
                self.driver.back()
            if module_1 and module_2 and module_3:
                with allure.step("All 3 submodules are visible and clickable" ):
                    return True
            else:
                with allure.step("Some submodules are not visible and clickable" ):
                    return False


    def is_4_submodules_redirected_to_related_pages(self):
        with allure.step("Clicked On What is biomagnetism button"):
            self.do_click(BiomagnetismElements.biomagnetism)
        faq = self.get_page_status("FAQs",BiomagnetismElements.faq,"FAQs")
        blogs = self.get_page_status("Blogs",BiomagnetismElements.blogs,"Blogs")
        podcast = self.get_page_status("Podcast",BiomagnetismElements.podcast,"Podcast video")
        research = self.get_page_status("Research",BiomagnetismElements.research,"Research")

        if faq and blogs and podcast and research:
            with allure.step("All pages are redirected to related pages"):
                return True
        else:
            with allure.step("All pages are not redirected to related pages"):
                return False

    @allure.step("Checking 3 submodules are present in each submodule")
    def is_submodules_present_in_each_page(self):

        faq = self.get_submodule_status("FAQS",
                                    BiomagnetismElements.faq,
                                    BiomagnetismElements.blogs,
                                    "BLOGS",
                                    BiomagnetismElements.podcast,
                                    "PODCASTS",
                                    BiomagnetismElements.research,
                                    "RESEARCH"
        )

        blogs = self.get_submodule_status("Blogs",
                                    BiomagnetismElements.blogs,
                                    BiomagnetismElements.faq2,
                                    "FAQ",
                                    BiomagnetismElements.podcast,
                                    "PODCASTS",
                                    BiomagnetismElements.research,
                                    "RESEARCH"
        )

        research = self.get_submodule_status("Research",
                                    BiomagnetismElements.research,
                                    BiomagnetismElements.faq2,
                                    "FAQ",
                                    BiomagnetismElements.blogs,
                                    "BLOGS",
                                    BiomagnetismElements.podcast,
                                    "PODCASTS",
        )

        podcast = self.get_submodule_status("Podcasts",
                                    BiomagnetismElements.blogs,
                                    BiomagnetismElements.faq2,
                                    "FAQ",
                                    BiomagnetismElements.blogs,
                                    "BLOGS",
                                    BiomagnetismElements.research,
                                    "RESEARCH"
        )

        if faq and blogs and research and podcast:
            with allure.step("All 3 submodules are visible and clickable in each submodule"):
                return True
        else:
            with allure.step("All 3 submodules are not visible and clickable in each submodule"):
                return False
    
    def is_biomagnestism_dropdown_visible_and_clickable(self):
        dropdown_assert_element = ["FAQ","Research","Biomagnetism Therapy session","Biomagnetism vs Magnet Therapy"]
        dropdown_assert_element = [d_element.upper() for d_element in dropdown_assert_element]
        with allure.step("Move to what is biomagnestism dropdown"):
            self.do_move_cursor_to_element_only(BiomagnetismElements.biomagnetism)
        
        with allure.step("Taking all dropdown elements"):
            dropdown_elements = self.get_elements(BiomagnetismElements.biomagnetism_dropdown)

        with allure.step("Checking visibility and clickability of dropdown elements"):
            for element in dropdown_elements:

                if not element.text in dropdown_assert_element:
                    with allure.step(f"{element.text} is not visible"):
                        return False
                
                if not self.get_element_clickable_status(element,1):
                    with allure.step(f"{element.text} is not clickable"):
                        return False
            with allure.step("All Dropdown Elements are visible and clickable"):
                return True
    

    def is_faq_banner_and_content_visible(self):
        with allure.step("Clicked On What is biomagnetism buttom"):
            self.do_click(BiomagnetismElements.biomagnetism)
        with allure.step("Clicked On FAQs"):
            self.do_click(BiomagnetismElements.faq)
        
        with allure.step("Checking Banner Image and Content Visibility"):
            image = self.get_element_visibility(BiomagnetismElements.background_image)
            heading_content = self.get_text_from_element(BiomagnetismElements.background_heading)
            if "FAQs" == heading_content and image:
                with allure.step("Background image and background content are visible"):
                    return True
            else:
                with allure.step("Background image and background content are not visible"):
                    return False
    
    def check_each_faq_module(self,element,element_locator,element_value):
        
        module = self.check_visibility_and_clickable_of_element(element,element_locator,element_value)
        with allure.step(f"Click On {element}"):
            self.do_click(element_locator)
        with allure.step("Checking Question and Answer "):
            with allure.step("Taking All Questions"):
                questions = self.get_elements(BiomagnetismElements.question)
            with allure.step("Taking All Answer"):
                answare = self.get_elements(BiomagnetismElements.answare)
            print("==============================================================")
            print(len(questions))
            print(len(answare))
            print(module)
            if len(questions)>0 and len(answare)>0 and module:
                with allure.step("Question and Answer are visible"):
                    return True
            else:
                with allure.step("Question and Answer are not visible"):
                    return False
                

    
    def is_3_submodule_of_faq_visible_and_clickable(self):
        with allure.step("Clicked On What is biomagnetism buttom"):
            self.do_click(BiomagnetismElements.biomagnetism)
        with allure.step("Clicked On FAQs"):
            self.do_click(BiomagnetismElements.faq)
        
        with allure.step("Checking 3 Faqs Modules are visible and clickable"):
            module_1 = self.check_each_faq_module("BIOMAGNETISM FAQs",BiomagnetismElements.biomagnetism_faq,"FAQs")
            module_2 = self.check_each_faq_module("BIOMAGNETISM SESSIONS FAQs",BiomagnetismElements.biomagnetism_faq_session,"SESSIONS FAQs")
            module_3 = self.check_each_faq_module("LEARNING BIOMAGNETISM FAQs",BiomagnetismElements.biomagnetism_faq_learner,"LEARNING")

            if module_1 and module_2 and module_3:
                with allure.step("All Faqs Submodules are visible and clickable"):
                    return True
            else:
                with allure.step("All Faqs Submodules are not visible and clickable"):
                    return False
    
    def is_research_contains_related_content(self):

        research_content = ["Peer-Reviewed Research Articles ",
                            "Dissertations",
                            "Magazine and Self-Published Articles",
                            "Clinical Case Studies",
                            "Research addressing Magnetic Fields, but not Biomagnetic Pairs specifically",
                            "Magnetized Water"]

        with allure.step("Clicked On What is biomagnetism buttom"):
            self.do_move_cursor_to_element_only(BiomagnetismElements.biomagnetism)
        with allure.step("Clicked On Research"):
            self.do_click(BiomagnetismElements.research)
        
        with allure.step("Checking Content"):
            research_body = self.get_text_from_element(BasePageElements.body)

            for research_heading_element in research_content:
                if not research_heading_element in research_body:
                    with allure.step("Some Content are not related to the research page"):
                        return False
        with allure.step("All Content are related to the research page"):
            return True

    def is_biomagnetism_therapy_session_contains_related_content(self):

        research_content = ["Biomagnetism Therapy Session",
                            "How long is each session?",
                            "How many sessions are needed for one’s health issue?",
                            "Are there any instances when BM is not recommended?",
                            "What are the side effects of BM therapy?",
                            "Is Biomagnetic pair therapy costly?",
                            "How can Biomagnetic therapy help with emotional or psychological problems?"]

        with allure.step("Clicked On What is biomagnetism buttom"):
            self.do_move_cursor_to_element_only(BiomagnetismElements.biomagnetism)
        with allure.step("Clicked On Biomagnetism Therapy Session"):
            self.do_click(BiomagnetismElements.biomagnetism_therapy_session)
        
        with allure.step("Checking Content"):
            research_body = self.get_text_from_element(BasePageElements.body)

            for research_heading_element in research_content:
                if not research_heading_element in research_body:
                    with allure.step("Some Content are not related to the Biomagnetism Therapy page"):
                        return False
        with allure.step("All Content are related to the Biomagnetism Therapy page"):
            return True
    

    def is_biomagnetism_vs_magnet_therapy_contains_related_content(self):

        research_content = ["Is Biomagnetism similar to magnet therapy?"]

        with allure.step("Clicked On What is biomagnetism buttom"):
            self.do_move_cursor_to_element_only(BiomagnetismElements.biomagnetism)
        with allure.step("Clicked On Biomagnetism Vs Magnet Therapy"):
            self.do_click(BiomagnetismElements.biomagnetism_vs_magnet_therapy)
        
        with allure.step("Checking Content"):
            research_body = self.get_text_from_element(BasePageElements.body)

            for research_heading_element in research_content:
                if not research_heading_element in research_body:
                    with allure.step("Some Content are not related to the Biomagnetsim vs magnet therapy page"):
                        return False
        with allure.step("All Content are related to the Biomagnetsim vs magnet therapy page"):
            return True






                    



        


    

        

    