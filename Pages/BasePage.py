import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time



class BasePage:

    @allure.step("Initialiazing the webdriver")
    def __init__(self,driver,wait):
      
        self.driver = driver
        self.wait = wait
    
    @allure.step("Scroll To The Element")
    def do_scroll_to_element(self,by_locator):
        action = ActionChains(self.driver)
        
        element = element = self.wait.until(EC.visibility_of_element_located(by_locator))
        action.scroll_to_element(element).perform()

    @allure.step("Scroll To The Element")
    def do_scroll_to_element_only(self,element):
        action = ActionChains(self.driver)
        action.scroll_to_element(element).perform()
        # element_screenshot = element.screenshot_as_png
        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)

    @allure.step("Move To The Element")
    def do_click_to_element_by_offset(self,element,x,y):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element,x,y).click().perform()
        # action.click(element).perform()
    @allure.step("Move Cursor To The Element")
    def do_move_cursor_to_element_only(self,by_locator):
        action = ActionChains(self.driver)
        
        element = element = self.wait.until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(element).perform()
        # element_screenshot = element.screenshot_as_png
        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
    
    @allure.step("Move Cursor To The Element")
    def do_move_cursor_to_element(self,by_locator):
        action = ActionChains(self.driver)
        
        element = element = self.wait.until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(element).perform()
        # element_screenshot = element.screenshot_as_png
        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
    @allure.step("Clicked On Element")
    def do_click(self,by_locator):
        """
        This Function used to click on the selected web element 
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        element.click()
    
    def do_click_only(self,by_locator):
        """
        This Function used to click on the selected web element 
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        element.click()

    @allure.step("Checking Visibilty Of Element")
    def get_element_visibility(self,by_locator):
        """
        This Function used to check the visibility of a web Element and retured True/False
        """
        
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element_p = self.wait.until(EC.presence_of_element_located(by_locator))
        
        element_screenshot = element.screenshot_as_png

        allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        
        width = element_p.size['width']
        height = element_p.size['height']

        if width>0 and height>0:
            return True
        else:
            return False

    @allure.step("Checking Visibilty Of Element")
    def get_element_visibility_only(self,by_locator):
        """
        This Function used to check the visibility of a web Element and retured True/False
        """
        element_p = self.wait.until(EC.presence_of_element_located(by_locator))
        
        width = element_p.size['width']
        height = element_p.size['height']

        if width>0 and height>0:
            with allure.step("Visible"):
                return True
        else:
            with allure.step("Not Visible"):
                return False
    
    @allure.step("Checking Visibilty Of Element")
    def get_element_visibility_div(self,by_locator):
        """
        This Function used to check the visibility of a web Element and retured True/False
        """
        
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        
        return bool(element)
    
    @allure.step("Taking Text from element")
    def get_text_from_element(self,by_locator):
        """
        This Function used to get the text value from the web element and returned the value
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element_screenshot = element.screenshot_as_png

        allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        return element.text
    
    @allure.step("Taking Text from element")
    def get_text_from_element_only(self,by_locator):
        """
        This Function used to get the text value from the web element and returned the value
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    
    def get_text_from_element_only(self,by_locator):
        """
        This Function used to get the text value from the web element and returned the value
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        return element.text


    @allure.step("Sending Text To The Input Box")
    def do_send_keys(self,by_locator,text):
        """
        This function used to send text to the input box 
        """

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        element.send_keys(text)
    @allure.step("Clearing Input Field")
    def do_clear_input_field(self,by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
    @allure.step("Selecting Dropdown Option")
    def do_select_by_value(self,by_locator,value):
        """
        This function used to select the option from dropdown 
        """
        element = self.wait.until(EC.visibility_of_element_located(by_locator))

        dropdown = Select(element)
        dropdown.select_by_value(value)
    
    @allure.step("Selecting Dropdown Option")
    def do_select_by_text(self,by_locator,value):
        """
        This function used to select the option from dropdown 
        """
        element = self.wait.until(EC.visibility_of_element_located(by_locator))

        dropdown = Select(element)
        dropdown.select_by_visible_text(value)
        time.sleep(5)
    
    @allure.step("Taking Website Title")
    def get_title(self):
        """
        This function used to return the  website title
        """

        return self.driver.title
    
    @allure.step("Taking Current Url")
    def get_current_url(self):
        """
        This function return current url
        """

        return self.driver.current_url
    @allure.step("Taking All Elements")
    def get_elements(self,by_locator):
        elements = self.wait.until(EC.visibility_of_all_elements_located(by_locator))
        return elements
    
    @allure.step("Taking All Elements")
    def get_element(self,by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element
    
    @allure.step("Taking tag <a> scr")
    def get_tag_a_src(self,by_locator):

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        return element.get_attribute('href')
    
    @allure.step("Taking tag attributes")
    def get_tag_attribute(self,by_locator,attribues):

        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        # element_screenshot = element.screenshot_as_png

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        return element.get_attribute(attribues)
    
    @allure.step("Checking Element Clickable Status")
    def get_element_clickable_status(self,by_locator,options=0):

        if options == 1:
            element = by_locator
        else:   
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def get_element_background_visibility(self,by_locator,locator_image_url):
        """
        This Function used to check the visibility of a web Element and retured True/False
        """
        
        element = self.wait.until(EC.visibility_of_element_located(by_locator))

        background_image_property = element.value_of_css_property("background-image")
        image_url = background_image_property.replace('url("', '').replace('")', '')

        element_p = self.wait.until(EC.presence_of_element_located(by_locator))
        allure.attach('<img src="' + image_url + '" alt="Image" width="500"/>', "Element Screenshot", allure.attachment_type.HTML)

        # allure.attach(element_screenshot,name= "Element Screenshot", attachment_type= allure.attachment_type.PNG)
        
        width = element_p.size['width']
        height = element_p.size['height']

        if width>0 and height>0 and image_url == locator_image_url:
            return True
        else:
            return False
    

    

    
    
    
        
    
    