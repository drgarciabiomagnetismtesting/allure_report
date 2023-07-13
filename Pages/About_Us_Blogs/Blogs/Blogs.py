from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.About_Us_Blogs.Blogs.Blogs_Elements import BlogsElements
import time
import allure
import requests



class Blogs(BasePage):
    
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
    
    def check_each_blog_visibility(self,image_locator,read_more_locator,heading_locator):
        with allure.step("Checking Image Visibility"):
            image_status = self.get_element_visibility(image_locator)
            if image_status:
                with allure.step("Image Is Visible"):
                    print("Image Is Visible")
            else:
                with allure.step("Image Is Not Visible"):
                    print("Image Is Not Visible")

        with allure.step("Checking Read More Button Visibility"):
            read_more_status = self.get_element_visibility(read_more_locator)
            if image_status:
                with allure.step("Read More Button Is Visible"):
                    print("Read More Button Is Visible")
            else:
                with allure.step("Read More Button Is Not Visible"):
                    print("Read More Button Is Not Visible")


        heading = self.get_text_from_element(heading_locator)
        with allure.step("Clicked On Read More Button"):
            self.do_click(read_more_locator)
        time.sleep(2)
        with allure.step("Checking Blog Page Heading on the page"):
            blog_body = self.get_text_from_element(BasePageElements.body)
        self.driver.back()
        if heading in blog_body:
            with allure.step("Blog Is Visible"):
                blog_visible_status = True
        else:
            with allure.step("Blog Is  Not Visible"):
                blog_visible_status = False
        
        if image_status and read_more_status and blog_visible_status:
            return True
        else:
            return False
    @allure.step("Checking Each Blog Pages")
    def get_blogs_visible_status(self):
        with allure.step("Taking All Blog Pages"):
            all_blogs = self.get_elements(BlogsElements.all_blogs)
        for blog_index in range(len(all_blogs)):
            blog_index = blog_index + 1
            blog_image_locator,read_more_locator,heading_locator = BlogsElements.get_each_blog_xpath(index_number= blog_index)
            with allure.step(f"Checking Blog {blog_index} Redirecting associate blog page or not"):
                blog_status = self.check_each_blog_visibility(blog_image_locator,read_more_locator,heading_locator)
                if not blog_status:
                    return False
        return True





    @allure.step("Checking Blog Page Redirecting")
    def get_blog_page_redirecting_status(self):
        with allure.step("Clicked On Blog Navigation Button"):
            self.do_click(BlogsElements.blog)
        
        with allure.step("Checking Blog Page Elements"):
            blog_page = self.get_text_from_element(BasePageElements.body)

        
        faq_visibility_status = self.check_visibility_of_element("FAQ",BlogsElements.faq,"FAQ")
        podcast_visibility_status = self.check_visibility_of_element("Podcasts",BlogsElements.podcast,"PODCASTS")
        research_visibility_status = self.check_visibility_of_element("Research",BlogsElements.reasearch,"RESEARCH")
        

        if faq_visibility_status and podcast_visibility_status and research_visibility_status:
            return True
        else:
            return False

    @allure.step("Check Working Status Of Search Option")
    def check_search_action_working_status(self,search_value):
        with allure.step(f"Typing {search_value} in Search Box"):
            self.do_send_keys(BlogsElements.search_input,search_value)
        
        with allure.step("Clicked On Search Button"):
            self.do_click(BlogsElements.search_button)
        search_heading = self.check_visibility_of_element(f"Search result of {search_value}",BlogsElements.search_heading,search_value)
        with allure.step("Redirecting to Read More Page"):
            self.driver.back()
        return search_heading
    
    def generate_random_sentence(self):
        url = "https://loripsum.net/api/1/short"

        # Send GET request to the loripsum API
        response = requests.get(url)

        if response.status_code == 200:
            # Extract the sentence from the response
            sentence = response.text.strip().removeprefix('<p>').removesuffix('</p>')

            return sentence

        return None
    @allure.step("Checking Post Comments Option")
    def check_post_comments(self,name,email,website):
        comment = self.generate_random_sentence()
        with allure.step(f"Typing {comment} in Comment Box"):
            self.do_click_only(BlogsElements.comment_text_area)
            time.sleep(0.3)
            self.do_send_keys(BlogsElements.comment_text_area,comment)
        
        with allure.step(f"Typing {name} in name field"):
            self.do_click_only(BlogsElements.name)
            time.sleep(0.3)
            self.do_send_keys(BlogsElements.name,name)
        
        with allure.step(f"Typing {email} in email field"):
            self.do_click_only(BlogsElements.email)
            time.sleep(0.3)
            self.do_send_keys(BlogsElements.email,email)
        
        with allure.step(f"Typing {website} in website field"):
            self.do_click_only(BlogsElements.website)
            time.sleep(0.3)
            self.do_send_keys(BlogsElements.website,website)

        with allure.step(f"Clicked On Post Comment Button"):
            self.do_click(BlogsElements.post_comment)
        with allure.step("Checking Post Response"):
            time.sleep(5)
            
            response = self.get_text_from_element(BlogsElements.response)
            self.driver.back()
            if "Thanks for your comment. We appreciate your response." in response:
                with allure.step("Comment Posted Success"):
                    return True
            elif "You might have left one of the fields blank." in response:
                with allure.step("Comment Posted Not Success, You might have left one of the fields blank "):
                    return False
            elif "Processing" in response:
                with allure.step("Comment Posted Not Success, Unble to send request"):
                    return False

            else:
                with allure.step("Comment Posted Not Success"):
                    return False


    @allure.step("Checking Read More Page Elements Visibility")
    def check_read_more_page_element_visibility_status(self):

        blog_image_locator,read_more_locator,heading_locator = BlogsElements.get_each_blog_xpath(index_number= 1)
        with allure.step("Clicked On Blog 1"):
            self.do_click(read_more_locator)
        search_visibility_status = self.check_visibility_of_element("Search",BlogsElements.search,"Search")
        recent_posts_visibility_status = self.check_visibility_of_element("Recent Posts",BlogsElements.recent_post,"Recent Posts")
        categories_visibility_status = self.check_visibility_of_element("Categories",BlogsElements.categories,"Categories")
        post_comments_visibility_status = self.check_visibility_of_element("Post Comment Form",BlogsElements.comment_form,"Leave a Comment")
        
        if search_visibility_status and recent_posts_visibility_status and categories_visibility_status and post_comments_visibility_status:
            return True
        else:
            return False
    
    def check_page_redirecting_status(self,page):
        if page == 'FAQ':
            click_element = BlogsElements.faq
            visible_text = "FAQs"
        elif page == 'PODCASTS':
            click_element = BlogsElements.podcast
            visible_text = "Podcast video"
        elif page == 'RESEARCH':
            click_element = BlogsElements.reasearch
            visible_text = "Research"

        with allure.step(f"Clicked On {page} button"):
            self.do_click(click_element)
        with allure.step(f"Checking {page} visibility status"):
            faq_heading_status = self.check_visibility_of_element(page,BasePageElements.body,visible_text)
        self.driver.back()
        if faq_heading_status:
            with allure.step(f"{page} is visible"):
                return True
        else:
            with allure.step(f"{page} is visible"):
                return False
    


        



        

