from selenium.webdriver.common.by import By

class StoreElements:

    store = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Store'])[1]")
    store_dropdown = (By.XPATH,"(//ul[@class='sub-menu'])[6]")
    store_dropdown_list = (By.XPATH,"(//ul[@class='sub-menu'])[5]/li")

    nutritional_health = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Nutritional Health'])[1]")
    biomagnetism_supplies = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Biomagnetism Supplies'])[1]")
    mold_recovery = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Mold Recovery'])[1]")
    EMF_protection = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='EMF Protection'])[1]")
    home_business = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Home and Business'])[1]")

    product = (By.XPATH,"//ul[contains(@class,'products')]")
    all_products = (By.XPATH,"//ul[contains(@class,'products')]/li")

    def get_product_xpath(product_index):
        product_heading = (By.XPATH,f"((//div[@class='astra-shop-summary-wrap'])/a/h2)[{product_index}]")
        product_image = (By.XPATH,f"(//div[@class='astra-shop-thumbnail-wrap'])[{product_index}]")
        product_price = (By.XPATH,f"(//span[@class='price'])[{product_index}]")
        product_add_to_cart = (By.XPATH,f"((//div[@class='astra-shop-summary-wrap'])/a[2])[{product_index}]")

        return product_heading,product_image, product_price, product_add_to_cart
    
    sorting_Element = (By.XPATH,"//select[@name='orderby']")
    sorting_options = (By.XPATH,"//select[@name='orderby']/option")
    sorting_product_heading = (By.XPATH,"(//div[@class='astra-shop-summary-wrap'])/a[1]")


    add_to_cart_icon = (By.XPATH,"(//i[contains(@class,'astra-icon ast-icon-shopping-cart')])[1]") #data-cart-total
    thera_creme = (By.XPATH,"(//li[contains(.,'TheraCreme, 59gr')]//a[contains(@class,'ajax_add_to_cart')])[2]")
    thera_creme_name = (By.XPATH,"(//div[@class='elementor-menu-cart__product-name product-name'])[3]")
    thera_cart_image = (By.XPATH,"(//div[@class='elementor-menu-cart__product woocommerce-cart-form__cart-item cart_item'])[3]//img")
    thera_cart_price = (By.XPATH,"((//div[@class='elementor-menu-cart__product-price product-price'])//span)[5]")

    decrease_qty = (By.XPATH,"(//a[@id='minus_qty'])[3]")
    increase_qty = (By.XPATH,"(//a[@id='plus_qty'])[3]")
    cart_decrease_qty = (By.XPATH,"(//a[@id='minus_qty'])[1]")
    cart_increase_qty = (By.XPATH,"(//a[@id='plus_qty'])[1]")
    qty = (By.XPATH,"(//input[@class='input-text qty text'])[3]") #value
    cart_qty = (By.XPATH,"(//input[@class='input-text qty text'])[1]")

    view_cart = (By.XPATH,"(//a[@class='elementor-button elementor-button--view-cart elementor-size-md'])[3]")
    checkout = (By.XPATH,"(//a[@class='elementor-button elementor-button--checkout elementor-size-md'])[3]")
    cart_close = (By.XPATH,"(//button[@aria-label='Close Cart Drawer'])[1]")
    sub_total = (By.XPATH,"(//div[@class='elementor-menu-cart__subtotal'])[3]")
    cart_subtotal = (By.XPATH,"//td[@class='product-subtotal']")
    checkout_button = (By.XPATH,"(//a[normalize-space()='Proceed to checkout'])[1]")


    username = (By.XPATH,"(//input[@id='billing_email'])[1]")
    first_name_m  = (By.XPATH,"(//input[@id='billing_first_name'])[1]")
    last_name_m = (By.XPATH,"(//input[@id='billing_last_name'])[1]")
    company = (By.XPATH,"(//input[@id='billing_company'])[1]")
    house_street_name = (By.XPATH,"(//input[@id='billing_address_1'])[1]")
    appartment = (By.XPATH,"(//input[@id='billing_address_2'])[1]")
    city_m = (By.XPATH,"(//input[@id='billing_city'])[1]")
    zip_code_m = (By.XPATH,"(//input[@id='billing_postcode'])[1]")
    phone_m = (By.XPATH,"(//input[@id='billing_phone'])[1]")
    

    






