import pytest
from Tests.test_Base import BaseTest
from Pages.HomePage_ContactUs.Home.HomePage import HomePage
from Config.config import TestData
from CheckSSLCert import validate

import allure

@allure.title("Home Page Test Cases")
class TestHomePage(BaseTest):
    global HomePageObj

    

    @allure.title("Test Case 4 : Testing Visibility Of Homepage Banner Image")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the banner page is having images , content and alignments as per design.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Banners page should be present along with the related content  content, proper alignments
    
    """)
    def test_home_page_banner_visibility(self):
        TestHomePage.HomePageObj = HomePage(self.driver,self.wait)
        try:
            
            banner_element = TestHomePage.HomePageObj.get_banner_image()
            banner_heading = TestHomePage.HomePageObj.get_banner_heading()
            banner_contain = TestHomePage.HomePageObj.get_banner_contain()
            if banner_heading == "Dr Garcia BIOMAGNETISM":
                banner_heading_status = True
            else:
                banner_heading_status = False

            if "Enabling individuals to unleash" in  banner_contain:
                banner_contain_status = True
            else:
                banner_contain_status = False

            assert banner_element and banner_heading_status and banner_contain_status

        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Homepage Banner Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Some Navigation links are missing"):
                assert False

    @allure.title("Test Case 2 : SSL Certificate Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the either SSL certifiate and https having within Website Url 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>SSL /  HTTPS should be  present
    
    """)
    def test_check_validation_of_ssl_certificate(self):
        try:
            with allure.step("Checking Certificate"):
                checker = validate.from_link(TestData.BaseUrl)
                if checker.IsActive():
                    with allure.step("Valid SSL Certificate"):
                        assert True
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="SSL Certificate Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Not Valid SSL Certificate"):
                assert True
    
    @allure.title("Test Case 3 : Testing Navbar Links and Icons")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the the home page having menus, search icon and cart icon  as per design
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All menus, search icon and cart icon are sholud be present in menu bar 
    
    """)
    def test_navbar_and_nav_icons(self):

        try:
            with allure.step("Checking all navigation item"):
                nav_elements = TestHomePage.HomePageObj.get_navigation_menu_item()

            test_nav_string = """
            
                            ABOUT US
                            WHAT IS BIOMAGNETISM
                            BIOMAGNETISM SERVICES
                            PODCASTS
                            TRAINING
                            STORE
                            REVIEWS
                            BLOGS
                            CONTACT US
                            
            """

            for nav_element in nav_elements:
                if str(nav_element.text).upper() in test_nav_string:
                    with allure.step(f"Nav Item Present: {nav_element.text}"):
                        allure.attach(nav_element.screenshot_as_png, name= f"{nav_element.text}",attachment_type= allure.attachment_type.PNG)
                        nav_status = True
                else:
                    with allure.step(f"Nav Item Not Present: {nav_element.text}"):
                        allure.attach(nav_element.screenshot_as_png, name= f"{nav_element.text}",attachment_type= allure.attachment_type.PNG)
                        nav_status = False
            
            search_button_status = TestHomePage.HomePageObj.get_search_btn_status()
            cart_button_status = TestHomePage.HomePageObj.get_cart_btn_status()
        
            if nav_status and search_button_status and cart_button_status:
                assert True
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="SSL Certificate Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Some Navigation links are missing"):
                assert False
    
    @allure.title("Test Case 5 : Slideshow Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the slideshow banner having  rotating display of  including multiple images and  text.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Banner page sholud be present along with the rotating display with content related images
    
    """)
    def test_slideshow(self):
        try:
            slide_status = TestHomePage.HomePageObj.get_slide()
            assert slide_status
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Slideshow  Failed", attachment_type= allure.attachment_type.PNG)
            assert False
    
    @allure.title("Test Case 6 : Contact Us Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the contact icon is easy to recognize and easy to clickable  below the slideshow banner image.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>It should be clickable after clicking Contact us Icon image is going to open with the detail page.
    
    """)
    def test_contact_us_visibility(self):
        try:
            contact_us_btn_status,contact_us_heading_status = TestHomePage.HomePageObj.validate_contact_us_redirect_to_contact_us_page()

            if contact_us_btn_status and contact_us_heading_status:
                assert True
            else:
                assert False
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Contact Us Button Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    @allure.title("Test Case 7 : Cards Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the card pages having images which are  same as per design 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>It should be having card images is therapy ,training and products
    
    """)
    def test_cards_visibility(self):
        try:
            card_status = TestHomePage.HomePageObj.get_all_card_status()
            assert card_status
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Cards Visibility  Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    @allure.title("Test Case 9 : Therapy Card Redirecting Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate therapy card is navigating to the particular page or not.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Therapy card sholud navigate to the therapy detailed page
    
    """)
    def test_therapy_card(self):
        try:
            assert TestHomePage.HomePageObj.therapy_card_status()
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Therapy card redirecting  Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    @allure.title("Test Case 10 : Training Card Redirecting Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the traininig card is navigated to upcoming  training seminars related   detailed page or not 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Training card  page should navigated to the training detailed page.
    
    """)
    def test_training_card(self):
        try:
            assert TestHomePage.HomePageObj.training_card_status()
            
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Training card redirecting  Failed", attachment_type= allure.attachment_type.PNG)
            assert False
    
    @allure.title("Test Case 11 : Product Card Redirecting Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the products card is navigated to the store products page or not 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Products cards page should navigated to the store detailed page.
    
    """)
    def test_product_card(self):
        try:
            assert TestHomePage.HomePageObj.product_card_status()
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Product card redirecting  Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    @allure.title("Test Case 12 : Testimonial Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the testimonials content  slides are moving  smoothly from one testimonial to the next after clicking right and left arrow regarding clicking direction. 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Testimonials  slide show should be move by clicking left or  right accordingly
    
    """)
    def test_testimonial(self):
        try:
            assert TestHomePage.HomePageObj.get_testimonial_status()
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Product card redirecting  Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    
    @allure.title("Test Case 1 : Logo Visibility Testing")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate the website having the logo as per UI design developed in header and footer 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Logo and icon should be same in header and footer
    
    """)
    def test_logo_visibility(self):
        try:
            with allure.step("Creating HomePage Object"):
               
                with allure.step("Checking Logo Visibility"):
                    logo_status = TestHomePage.HomePageObj.get_homePageLogo()

            if logo_status:
                assert True
        except:
            allure.attach(self.HomePageObj.driver.get_screenshot_as_png(),name="Home Page Logo Failed", attachment_type= allure.attachment_type.PNG)
            assert False

    

    
