from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.HomePage_ContactUs.Home.HomePageElements import HomePageElements
from Element_Locator.BasePageElements import BasePageElements
import time
import allure

class HomePage(BasePage):

    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)

    @allure.step("Taking Header and Footer Logo")
    def get_homePageLogo(self):
        header_logo_visibility = self.get_element_visibility(HomePageElements.header_logo)
        footer_logo_visibility = self.get_element_visibility(HomePageElements.footer_logo)
        if header_logo_visibility and footer_logo_visibility:
            return True
        else:
            return False
    
    @allure.step("Taking all navigation menu elements")
    def get_navigation_menu_item(self):

        nav_links = self.get_elements(HomePageElements.nav_links)
        nav_link_list = [link for link in nav_links]
        return nav_link_list
    
    @allure.step("Checking Search Button Visibility")
    def get_search_btn_status(self):
        search_btn = self.get_element_visibility(HomePageElements.search_btn)
        if search_btn:
            return True
        else:
            return False
        
    @allure.step("Checking Cart Button Visibility")
    def get_cart_btn_status(self):
        cart_btn = self.get_element_visibility(HomePageElements.cart_icon)
        if cart_btn:
            return True
        else:
            return False
    
    @allure.step("Checking Homepage Banner Image Visibility")
    def get_banner_image(self):
        banner_image = self.get_element_visibility(HomePageElements.banner_image)
        if banner_image:
            return True
        else:
            return False

    @allure.step("Checking Homepage Heading Visibility")
    def get_banner_heading(self):
        banner_heading = self.get_text_from_element(HomePageElements.banner_heading)
        return banner_heading
    
    @allure.step("Checking Homepage Contain Visibility")
    def get_banner_contain(self):
        banner_contain = self.get_text_from_element(HomePageElements.banner_contain)
        return banner_contain

    @allure.step("Checking slideshow heading")
    def get_slide_heading(self,slide_element):
        
        slide_heading = self.get_text_from_element(slide_element)
        return slide_heading
    
    @allure.step("Checking slideshow image")
    def get_slide_image(self,slide_element):
        
        slide_heading = self.get_element_visibility(slide_element)
        return slide_heading
    
    def slideshow_element(self,slide_number,slide_number_element,slide_heading,slide_heading_element,slide_image_element):

        with allure.step(f"Clicked on slide {slide_number}"):
            self.do_click(slide_number_element)
        

        slide_1_heading = self.get_slide_heading(slide_heading_element)
        if slide_heading in slide_1_heading:
            slide_heading_status = True
        else:
            slide_heading_status = False

        slide_image_status = self.get_slide_image(slide_image_element)
        
        return slide_heading_status,slide_image_status



    def get_slide(self):

        slide_heading_1 = "What Is Biomagnetism?"
        slide_heading_2 = "How Biomagnetism Is"
        slide_heading_3 = "Learning Biomagnetism"
        slide_heading_4 = "To Take Back Your Health"
        slide_heading_5 = "Getting to Know Dr. Garcia"

        slide_heading_status_1,slide_image_status_1 = self.slideshow_element(
                                                        1,
                                                        HomePageElements.slide_1,
                                                        slide_heading_1,
                                                        HomePageElements.slide_1_heading,
                                                        HomePageElements.slide_1_image
                                                    )
        
        slide_heading_status_2,slide_image_status_2 = self.slideshow_element(
                                                        2,
                                                        HomePageElements.slide_2,
                                                        slide_heading_2,
                                                        HomePageElements.slide_2_heading,
                                                        HomePageElements.slide_2_image
                                                    )
        
        slide_heading_status_3,slide_image_status_3 = self.slideshow_element(
                                                        3,
                                                        HomePageElements.slide_3,
                                                        slide_heading_3,
                                                        HomePageElements.slide_3_heading,
                                                        HomePageElements.slide_3_image
                                                    )

        slide_heading_status_4,slide_image_status_4 = self.slideshow_element(
                                                        4,
                                                        HomePageElements.slide_4,
                                                        slide_heading_4,
                                                        HomePageElements.slide_4_heading,
                                                        HomePageElements.slide_4_image
                                                    )

        slide_heading_status_5,slide_image_status_5 = self.slideshow_element(
                                                        5,
                                                        HomePageElements.slide_5,
                                                        slide_heading_5,
                                                        HomePageElements.slide_5_heading,
                                                        HomePageElements.slide_5_image
                                                    )
        


        if slide_heading_status_1 and slide_heading_status_2 and slide_heading_status_3 and slide_heading_status_4 and slide_heading_status_5 and slide_image_status_1 and slide_image_status_2 and slide_image_status_3 and slide_image_status_4 and slide_image_status_5:
            return True
        else:
            return False

    def get_contact_us_visibility_(self):
        contact_us = self.get_text_from_element(HomePageElements.contact_us)
        if "Contact Us" in contact_us:
            return True
        else:
            return False
    
    def validate_contact_us_redirect_to_contact_us_page(self):
        with allure.step("Checking Contact Us Visibility"):
            contact_us_btn_status = self.get_contact_us_visibility_()

        with allure.step("Clicked on Contact Us Button"):
            self.do_click(HomePageElements.contact_us)

        with allure.step("Taking Heading From Contact Us Page"):
            contact_us_heading = self.get_text_from_element(BasePageElements.body)

        if "CONTACT US" in str(contact_us_heading).upper():
            with allure.step("Contact Us Page is Open"):
                contact_us_heading_status = True
        else:
            with allure.step("Contact Us Page is not Open"):
                contact_us_heading_status = False

        with allure.step("Redirecting to Homepage"):
            self.driver.back()
        

        return contact_us_btn_status,contact_us_heading_status

    def get_card_status(self,card_locator,card_image,heading):

        card_heading = self.get_text_from_element(card_locator)
        if heading in card_heading:
            card_heading_status = True
        else:
            card_heading_status = False
        card_image = self.get_element_background_visibility(card_locator,card_image)
        return card_heading_status,card_image
    
    def get_all_card_status(self):
        card_heading_1 = "Therapy"
        card_image_1 = "https://dev.drgarciabiomagnetism.com/wp-content/uploads/2023/06/page-header_400-470.jpg"
        card_heading_2 = "Training"
        card_image_2= "https://dev.drgarciabiomagnetism.com/wp-content/uploads/2023/05/H-2.jpg"
        card_heading_3 = "Products"
        card_image_3 = "https://dev.drgarciabiomagnetism.com/wp-content/uploads/2023/05/H-3.jpg"

        card_heading_status_1,card_image_status_1 = self.get_card_status(HomePageElements.card_1,card_image_1,card_heading_1)
        card_heading_status_2,card_image_status_2 = self.get_card_status(HomePageElements.card_2,card_image_2,card_heading_2)
        card_heading_status_3,card_image_status_3 = self.get_card_status(HomePageElements.card_3,card_image_3,card_heading_3)

        if card_heading_status_1 and card_heading_status_2 and card_heading_status_3 and card_image_status_1 and card_image_status_2 and card_image_status_3:
            return True
        else:
            return False
    
    def therapy_card_status(self):
        with allure.step("Clicked on Therapy Card"):
            self.do_click(HomePageElements.card_1)

        with allure.step("Redirecting to Therapy Page"):
            therapy_page_heading = self.get_text_from_element(BasePageElements.body)

   
        
        if "What is Biomagnetism?" in therapy_page_heading:
            with allure.step("Therapy Page Is Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return True
        else:
            with allure.step("Therapy Page Is Not Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return False
    
    def training_card_status(self):
        with allure.step("Clicked on Training Card"):
            self.do_click(HomePageElements.card_2)

        with allure.step("Redirecting to Training Page"):
            therapy_page_heading = self.get_text_from_element(BasePageElements.body)

        
        
        if "Training" in therapy_page_heading:
            with allure.step("Training Page Is Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return True
        else:
            with allure.step("Training Page Is Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return False
    
    def product_card_status(self):
        with allure.step("Clicked on Product Card"):
            self.do_click(HomePageElements.card_3)

        with allure.step("Redirecting to Product Page"):
            therapy_page_heading = self.get_text_from_element(BasePageElements.body)

        
       
        if "Biomagnetism Supplies" in therapy_page_heading:
            with allure.step("Product Page Is Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return True
        else:
            with allure.step("Product Page Is Not Opened"):
                with allure.step("Redirecting to Homepage"):
                    self.driver.back()
                return False

    def get_testimonial_status(self):

        with allure.step("Taking Current Testimonial"):
            current_testimonial = self.get_text_from_element(HomePageElements.current_testimonial)
        
        with allure.step("Clicked On Next Testimonial Button"):
            self.do_click(HomePageElements.next_testimonial_button)
        
        with allure.step("Taking Next Testimonial"):
            next_testimonial = self.get_text_from_element(HomePageElements.current_testimonial)
        
        with allure.step("Clicked On Previous Testimonial Button"):
            self.do_click(HomePageElements.prev_testimonial_button)
        
        with allure.step("Taking Previous Testimonial"):
            prev_testimonial = self.get_text_from_element(HomePageElements.current_testimonial)

        with allure.step("Start While Loop For Searching Previous Testimonial"):
            while True:
                with allure.step("Clicked On Previous Testimonial Button"):
                    self.do_click(HomePageElements.prev_testimonial_button)
                    with allure.step("Taking Previous Testimonial"):
                        prev_testimonial = self.get_text_from_element(HomePageElements.current_testimonial)
                if prev_testimonial == current_testimonial:
                    break

        
        with allure.step("Comaparing next and previous testimonial content"):
            if current_testimonial != next_testimonial and current_testimonial == prev_testimonial:
                with allure.step("Both Contents Are Matching"):
                    return True
            else:
                with allure.step("Both Contents Are Not Matching"):
                    return False

    




        





    
       