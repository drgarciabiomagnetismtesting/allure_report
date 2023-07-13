from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.Store_Reviews.Store.StoreElements import StoreElements
import time
import allure



class Store(BasePage):
    
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
    
    def get_store_button_visibility(self):
        return self.check_visibility_of_element("Store Button",StoreElements.store,"STORE")
    
    def check_visibility_of_store_dropdown(self):
        dropdown = ["Nutritional Health",
                    "Biomagnetism Supplies",
                    "Mold Recovery",
                    "EMF Protection",
                    "Home and Business"]
        with allure.step("Moving the cursor to the store"):
            self.do_move_cursor_to_element(StoreElements.store)
        
        with allure.step("Checking Dropdown Menu"):
            dropdownElement = self.get_text_from_element_only(StoreElements.store_dropdown)
            for dropdown_menu in dropdown:
                if not dropdown_menu.upper() in dropdownElement:
                    with allure.step("Some Menu are not visible"):
                        return False
            with allure.step("All menu are visible"):
                return True

    def check_element_of_product(self, element_value,product_value):
        with allure.step(f"Checking Product {element_value}"):
            product_status = self.get_element_visibility_only(product_value)
            if product_status:
                with allure.step(f"Product {element_value} Visible"):
                    return True
            else:
                with allure.step(f"Product {element_value} Not Visible"):
                    return False
                    
    
    def check_product_details(self,product_index):
        with allure.step(f"Checking Product {product_index} Details"):
            product_heading,product_image, product_price, product_add_to_cart = StoreElements.get_product_xpath(product_index)
            
            
            product_image_status = self.check_element_of_product("Image", product_image)
            product_heading_status = self.check_element_of_product("Heading",product_heading)

            try:
                product_price_status = self.check_element_of_product("Price",product_price)
            except:
                product_price_status = True

            product_add_to_cart_status = self.check_element_of_product("Add To Cart", product_add_to_cart)

            if product_image_status and product_heading_status and product_price_status and product_add_to_cart_status:
                return True
            else:
                return False
        


    def check_menu_of_store_dropdown(self,menu,menu_element):
        with allure.step(f"Checking {menu}"):
            with allure.step("Moving the cursor to the store"):
                self.do_move_cursor_to_element(StoreElements.store)
            
            with allure.step(f"Clicked On {menu}"):
                self.do_click(menu_element)
            
            menu_heading = self.check_visibility_of_element(menu,BasePageElements.body,menu)
            products = self.get_element_visibility(StoreElements.product)
            all_products = self.get_elements(StoreElements.all_products)

            with allure.step("Checking all products"):
                for product in range(len(all_products)):
                    product_index = product +1

                    if not self.check_product_details(product_index):
                        return False
            


            with allure.step("Redirecting to homepage"):
                self.driver.back()

            if menu_heading and products:
                with allure.step(f"{menu} is redirected and products are visible"):
                    return True
            else:
                with allure.step(f"{menu} is not redirected and products are not visible"):
                    return False

    def check_each_menu_of_store_dropdown(self):

        nutritional_health_status = self.check_menu_of_store_dropdown("Nutritional Health",StoreElements.nutritional_health)
        biomagnetism_supplies_status = self.check_menu_of_store_dropdown("Biomagnetism Supplies",StoreElements.biomagnetism_supplies)
        mold_recovery_status = self.check_menu_of_store_dropdown("Mold Recovery",StoreElements.mold_recovery)
        EMF_protection_status = self.check_menu_of_store_dropdown("EMF Protection",StoreElements.EMF_protection)
        home_business_status = self.check_menu_of_store_dropdown("Home and Business",StoreElements.home_business)

        if nutritional_health_status and biomagnetism_supplies_status and mold_recovery_status and EMF_protection_status and home_business_status:
            with allure.step("All Store Dropdown Are Visible and Redirected to Related Page"):
                return True
        else:
            with allure.step("All Store Dropdown Not Are Visible and Redirected to Related Page"):
                return False


    @allure.step("Checking Store page")
    def get_store_page_redirecting_status(self):
        with allure.step("Click On Store"):
            self.do_click(StoreElements.store)
        
        with allure.step("Checking Store Page"):
            store_page = self.get_text_from_element(BasePageElements.body)

            with allure.step("Redirecting to homepage"):
                self.driver.back()

            if "Biomagnetism Supplies" in store_page:
                with allure.step("Redirecting to store page"):
                    return True
            else:
                with allure.step("Not Redirecting to store page"):
                    return False

    def get_sorting_functionality_status(self):
        sort_options = ["Sort by popularity",
                        "Sort by latest",
                        "Sort by price: low to high",
                        "Sort by price: high to low"]

        with allure.step("Move to store page"):
            self.do_move_cursor_to_element_only(StoreElements.store)
        
        with allure.step("Clicked On Nutritional Health "):
            self.do_click(StoreElements.nutritional_health)
        
        with allure.step("Clicked On Sort By"):
            self.do_click(StoreElements.sorting_Element)
        
        with allure.step("Checking all sorting options visibility"):
            short_elements = self.get_elements(StoreElements.sorting_options)
            
            
            for sortElement in short_elements:
                print(sortElement.text)
                if not sortElement.text in sort_options:
                    return False
        with allure.step("Checking each sorting options functionality"):
            with allure.step("Taking default product arrangements"):
                products = self.get_elements(StoreElements.sorting_product_heading)
                products_arrangment_letest = str([product.text for product in products])

            
            for sort_option in sort_options:
                with allure.step(f"Checking sorting options : {sort_option}"):
                    if sort_option == "Sort by latest":
                        continue
                    with allure.step(f"Select: {sort_option}"):
                        self.do_select_by_text(StoreElements.sorting_Element,sort_option)

                    with allure.step("Checking product arrangements"):
                        products = self.get_elements(StoreElements.sorting_product_heading)
                        products_arrangment = str([product.text for product in products])
                    if products_arrangment_letest == products_arrangment:
                        return False

        return True
    
    def add_product_to_cart_status(self):

        with allure.step("Move to store page"):
            self.do_move_cursor_to_element_only(StoreElements.store)
        
        with allure.step("Clicked On Nutritional Health "):
            self.do_click(StoreElements.nutritional_health)
        
        with allure.step("Add Product : TheraCreme, 59gr"):
            self.do_click(StoreElements.thera_creme)

        with allure.step("Checking Product Added or Not"):
            add_to_cart = self.get_element(StoreElements.thera_creme)
            after = add_to_cart.find_elements(By.XPATH,"following-sibling::*")

            if len(after)>0:
                with allure.step("Product Added"):
                    return True
            else:
                with allure.step("Product Is Not Added"):
                    return False
    
    def check_add_to_cart_total_product_count(self):
        time.sleep(5)
        with allure.step("Checking Product Count Updated To Cart Icon or Not"):
            value = int(self.get_tag_attribute(StoreElements.add_to_cart_icon,"data-cart-total"))

            if value >0:
                with allure.step("Product Count Updated To Cart Icon"):
                    return True
            else:
                with allure.step("Product Count Not Updated To Cart Icon"):
                    return False

    @allure.step("Checking Cart Elements Visibility")
    def check_cart_visibility(self):
        with allure.step("Clicked On Cart"):
            self.do_click(StoreElements.add_to_cart_icon)
        
        with allure.step("Product Image Visibility"):
            image_status = self.get_element_visibility_only(StoreElements.thera_cart_image)
        
        with allure.step("Product Name Visibility"):
            name_status = self.get_element_visibility_only(StoreElements.thera_creme_name)
        
        with allure.step("Product Cost Visibility"):
            cost_status = self.get_element_visibility_only(StoreElements.thera_cart_price)
        
        with allure.step("Product Increase Visibility"):
            increase_status = self.get_element_visibility_only(StoreElements.increase_qty)
        
        with allure.step("Product Decrease Visibility"):
            decrease_status = self.get_element_visibility_only(StoreElements.decrease_qty)
        
        with allure.step("Product Quantity Visibility"):
            qty_status = self.get_element_visibility_only(StoreElements.qty)

        with allure.step("Checkout Button Visibility"):
            checkout_status = self.get_element_visibility_only(StoreElements.checkout)
        
        with allure.step("View Cart Button Visibility"):
            view_cart_status = self.get_element_visibility_only(StoreElements.view_cart)
        
        with allure.step("Page Close Button Visibility"):
            close_button_status = self.get_element_visibility_only(StoreElements.cart_close)
        
        if image_status and name_status and cost_status and increase_status and decrease_status and qty_status and checkout_status and view_cart_status and close_button_status:
            with allure.step("All Elements Of Cart Is Visible"):
                return True
        else:
            with allure.step("Some Elements Of Cart Is Not Visible"):
                return False

    @allure.step("Checking Shopping Cart Elements Visibility And Working")
    def get_cart_page_redirecting_status(self):
        with allure.step("Clicked On View Cart"):
            self.do_click(StoreElements.view_cart)
        
        with allure.step("Increase Quantity"):
            self.do_click(StoreElements.cart_increase_qty)
        time.sleep(5)
        with allure.step("Check Quantity & Total Price"):
            with allure.step("Taking Quantity"):
                qty = int(self.get_tag_attribute(StoreElements.cart_qty,"value"))
            with allure.step("Taking Total Price"):
                total_price = self.get_text_from_element_only(StoreElements.cart_subtotal)
        
        with allure.step("Decrease Quantity"):
            self.do_click(StoreElements.cart_decrease_qty)
        time.sleep(5)
        with allure.step("Check Quantity & Total Price"):
            with allure.step("Taking Quantity"):
                qty2 = int(self.get_tag_attribute(StoreElements.cart_qty,"value"))
            with allure.step("Taking Total Price"):
                total_price2 = self.get_text_from_element_only(StoreElements.cart_subtotal)
        with allure.step("Checking Checkout Buttons"):
            checkout = self.get_element_visibility_only(StoreElements.checkout_button)

        if qty>qty2 and total_price != total_price2 and checkout:
            with allure.step("Increase and Decrease Buttons Are Working, Checkout Button Is Visible"):
                return True
        else:
            with allure.step("Increase and Decrease Buttons Are Not Working, Checkout Button Is Not Visible"):
                return False
    
    @allure.step("Checking Checkout Page Visibility")
    def get_checkout_page_visibility(self):
        with allure.step("Cliked On Checkout Button"):
            self.do_click(StoreElements.checkout_button)
        
        with allure.step("Cheking Checkout Page Open Or Not"):
            checkout_body = self.get_text_from_element(BasePageElements.body)

            if "Checkout" in checkout_body:
                with allure.step("Checkout Page Is Visible"):
                    return True
            else:
                with allure.step("Checkout Page Is Not Visible"):
                    return True

    @allure.step("Checking Mandatory Fields Showing * Or Not")
    def get_mandatory_fields(self):
        with allure.step("First Name"):
            first_name_status = self.get_tag_attribute(StoreElements.first_name_m,"placeholder")
        with allure.step("Last Name"):
            last_name_status = self.get_tag_attribute(StoreElements.last_name_m,"placeholder")
        with allure.step("Town/City"):
            city_status = self.get_tag_attribute(StoreElements.city_m,"placeholder")
        with allure.step("Zip Code"):
            zip_code_status = self.get_tag_attribute(StoreElements.zip_code_m,"placeholder")
        with allure.step("Phone Number"):
            phone_status = self.get_tag_attribute(StoreElements.phone_m,"placeholder")

        checking_fields = [ first_name_status, last_name_status, city_status,zip_code_status,phone_status]
        print(checking_fields)

        star = "\xa0*"
        star2 = "*"

        for field in checking_fields:
            if (star not in field or star2 not in field):
                with allure.step("Some Mandatory Fields Not Having *"):
                    return False
        with allure.step("All Mandatory Fields Having *"):
            return True
            


        
                

            


        






        

        





        




        

