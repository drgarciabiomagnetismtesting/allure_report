from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.About_Us_Blogs.Blogs.Blogs_Elements import BlogsElements
import time
import allure



class Blogs(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)


