import pytest
from Tests.test_Base import BaseTest
from Pages.Store_Reviews.Store.Store import Store
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Blog Page Test Cases")
class TestStore(BaseTest):

    global storeObj

    @allure.title("Test Case 1 : Store Button Visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Once open the DrGarciaBiomagnetism website in the header Stores module is present or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Store module should be present in the home page.
    
    """)
    def test_store_button_visibility(self):
        TestStore.storeObj = Store(self.driver,self.wait)
        try:
            assert TestStore.storeObj.get_store_button_visibility()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Store Button Visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Store Button  Visibility Is Failed"):
                assert False

    @allure.title("Test Case 2 : Store Dropdown Menu Visibility")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that once we mouse overing to the stores module in the home page all the dropdown options are opening or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All the dropdown options should show once we mouse hovering to stores module in the home page.
    
    """)
    def test_store_dropdown_menu_visibility(self):
        TestStore.storeObj = Store(self.driver,self.wait)
        try:
            assert TestStore.storeObj.check_visibility_of_store_dropdown()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Store Dropdown Menu Visibility Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Store Dropdown Menu  Visibility Is Failed"):
                assert False
    

    @allure.title("Test Case 3 : Store Redirect To Related Page ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Stores link should be clickable and once we click on that it is navigating to stores list page? 
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Once we click on Stores link in the home page it should navigate to stores list page where all the items are presented.
    
    """)
    def test_store_redirect_to_related_page(self):
        try:
            assert self.storeObj.get_store_page_redirecting_status()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Store Redirect To Related Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Store Redirect To Related Page Is Failed"):
                assert False

    @allure.title("Test Case 4 : Store Dropdown Menu Redirect To Related Page ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that if we click on any dropdown list in the stores(Ex - click on Nutritional health, it is navigating to Nutritional detail products page, here Product image, Product price, Product name and Add to Cart button is present or not check?) and check same scenario for other list in the
    
    <br><br><b>Expeceted Results:</b>
    <br><br>After click on Nutritional link below the stores dropdown it should navigate to Nutritional products detail page, here product name , product image, product cost and Add to cart button should be present in the Nutritional products list page. 
    
    """)
    def test_store_dropdown_menu_redirect_to_related_page(self):
        try:
            assert self.storeObj.check_each_menu_of_store_dropdown()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Store Dropdown Menu Redirect To Related Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Store Dropdown Menu Redirect To Related Page Is Failed"):
                assert False
    


    @allure.title("Test Case 5 : Sorting Product Functionality Check ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Stores product list page Sorting dropdown options are present or not?(Sort by Popularity, Sort by latest, Sort by price low to high and Sort by price high to low) all the options should be present and it should work accordingly.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Sort by options should be present in the stores product detail page and all the sorting options should be work as expected.
    
    """)
    def test_sorting_product_functionality(self):
        try:
            sorting_status =  self.storeObj.get_sorting_functionality_status()
            if sorting_status:
                with allure.step("Sorting Functionality is visible and working properly"):
                    assert sorting_status
            else:
                with allure.step("Sorting Functionality is not visible and not working properly"):
                    assert sorting_status
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Sorting Product Functionality Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Sorting Product Functionality Is Failed"):
                assert False

    
    @allure.title("Test Case 6 : Add To Cart Functionality ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that we click on Add to cart button in the Stores products detail page product is added to cart or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>User click on Add to cart button in the stores products list page, Perticular product should be added to cart.
    
    """)
    
    def test_add_to_cart_functionality(self):
        try:
            assert self.storeObj.add_product_to_cart_status()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Add To Cart Functionality Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Add To Cart Functionality Is Failed"):
                assert False
    

    @allure.title("Test Case 7 : Product Count Updated To Cart Icon Or Not ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that After adding the product to cart quantiity should be show above cart icon in the home page.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Product quantity should be show in the home page above the cart icon.
    
    """)
    def test_product_count_updated_to_cart_icon(self):
        try:
            
            assert self.storeObj.check_add_to_cart_total_product_count()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Product Count Updated To Cart Icon or Not Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Product Count Updated To Cart Icon or Not Is Failed"):
                assert False

    @allure.title("Test Case 8 : Visibility Of Cart Elements ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that Once added the product to cart click on cart icon in the home page it should navigate to shooping cart page, here product image, product name, product cost and incresing and decresing the quantity option, check out button , view cart button and page closing button should be there.
    
    <br><br><b>Expeceted Results:</b>
    <br><br>Once click on Cart icon in the home page it should navigate to shooping cart page, here all the options should be present whatever we mention in the scenarios.
    
    """)
    def test_visibility_of_cart_element(self):
        try:
            
            assert self.storeObj.check_cart_visibility()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Visibility Of Cart Elements Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Visibility Of Cart Elements Is Failed"):
                assert False
    

    @allure.title("Test Case 9 : Visibility Of Shopping Cart Elements ")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate If we click on view cart button in the shooping cart page it is navigating to Shooping cart detail page here we can able to increse or decrease the quantity as per that product amount should be cahange and proceed to checkout button is present or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>User click on View cart button in the shooping cart page it should navigate to shooping cart detail page and here product amount should be changed as per the increase or decrease the product.
    
    """)
    def test_visibility_of_shopping_cart_element(self):
        try:
            
            assert self.storeObj.get_cart_page_redirecting_status()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Visibility Of Cart Checkout Elements Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Visibility Of Cart Checkout Elements Is Failed"):
                assert False
    

    @allure.title("Test Case 10 : Visibility Of Checkout Page")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that click on checkout button in the shooping cart page it is navigating to check out detail form filling page or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>User click on checkout button in the shooping cart page it should navigate to checkout detail form filling page.
    
    """)
    def test_visibility_of_checkout_page(self):
        try:
            
            assert self.storeObj.get_checkout_page_visibility()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Visibility Of Checkout Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Visibility Of Checkout Page Is Failed"):
                assert False
    

    @allure.title("Test Case 11 : Visibility Of Mandatory Fields")
    @allure.description_html("""
    <br><b>Test Case Description:</b>
    <br><br>Validate that in the check out detail form page all the mandatory fields having star * mark or not?
    
    <br><br><b>Expeceted Results:</b>
    <br><br>All the mandatory fields should have star mark in the check out form detail page.
    
    """)
    def test_visibility_mandatory(self):
        try:
            
            assert self.storeObj.get_mandatory_fields()
        except:
            allure.attach(TestStore.storeObj.driver.get_screenshot_as_png(),name="Visibility Of Checkout Page Error", attachment_type= allure.attachment_type.PNG)
            with allure.step("Visibility Of Checkout Page Is Failed"):
                assert False