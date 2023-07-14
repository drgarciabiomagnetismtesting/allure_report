from selenium.webdriver.common.by import By


class HomePageElements:
    #<------------Test 1--------------->

    header_logo = (By.XPATH,"(//span[@class='site-logo-img'])[1]")
    footer_logo = (By.XPATH,"(//img[@class='wp-image-15537'])[1]")

    #<------------Test 2---------------->
    nav_links = (By.XPATH,"//ul[@id='ast-hf-menu-1']/li/a/span[@class='menu-text']")
    search_btn = (By.XPATH,"(//span[@class = 'ast-icon icon-search'])[2]")
    cart_icon = (By.XPATH,"(//span[@class = 'ast-icon icon-cart'])[1]")


    #<------------Test 3---------------->
    banner_image = (By.XPATH,"(//section[@class='elementor-section elementor-top-section elementor-element elementor-element-7ba4d6c elementor-section-height-min-height elementor-section-items-top elementor-section-boxed elementor-section-height-default'])[1]")
    banner_heading = (By.XPATH,"//h1[normalize-space()='Dr Garcia BIOMAGNETISM']")
    banner_contain = (By.XPATH,"//h1[contains(text(),'Enabling individuals to unleash')]")

    #<-------------Test 4----------------->
    slide_1 = (By.XPATH,"(//rs-bullet[contains(@class,'tp-bullet')])[1]")
    slide_1_heading = (By.XPATH,"(//a[normalize-space()='What Is Biomagnetism?'])[1]")
    slide_1_image = (By.XPATH,"(//img[@decoding='async'])[3]")

    slide_2 = (By.XPATH,"(//rs-bullet[contains(@class,'tp-bullet')])[2]")
    slide_2_heading = (By.XPATH,"(//a[contains(text(),'How Biomagnetism Is')])[1]")
    slide_2_image = (By.XPATH,"(//img[@decoding='async'])[4]")

    slide_3 = (By.XPATH,"(//rs-bullet[contains(@class,'tp-bullet')])[3]")
    slide_3_heading = (By.XPATH,"(//a[normalize-space()='Learning Biomagnetism'])[1]")
    slide_3_image = (By.XPATH,"(//img[@decoding='async'])[5]")

    slide_4 = (By.XPATH,"(//rs-bullet[contains(@class,'tp-bullet')])[4]")
    slide_4_heading = (By.XPATH,"(//a[normalize-space()='To Take Back Your Health'])[1]")
    slide_4_image = (By.XPATH,"(//img[@decoding='async'])[6]")

    slide_5 = (By.XPATH,"(//rs-bullet[contains(@class,'tp-bullet')])[5]")
    slide_5_heading = (By.XPATH,"(//a[normalize-space()='Getting to Know Dr. Garcia'])[1]")
    slide_5_image = (By.XPATH,"(//img[@decoding='async'])[7]")


    #<------------Test 5---------------->

    contact_us = (By.XPATH,"(//div[normalize-space()='Contact Us'])[1]")
    contact_us_heading = (By.XPATH,"//h1[normalize-space()='CONTACT US']")

    #<------------Test 6---------------->

    card_1 = (By.XPATH,"((//div[@class='elementor-container elementor-column-gap-default'])[9]/div/div)[1]")
    card_2 = (By.XPATH,"((//div[@class='elementor-container elementor-column-gap-default'])[9]/div/div)[2]")
    card_3 = (By.XPATH,"((//div[@class='elementor-container elementor-column-gap-default'])[9]/div/div)[3]")

    card_heading_1 = (By.XPATH,"//h1[normalize-space()='What is Biomagnetism?']")
    card_body = (By.XPATH,"//body")
    card_heading_2 = (By.XPATH,"//h1[normalize-space()='Training']")
    card_heading_3 = (By.XPATH,"//a[contains(text(),'Biomagnetism Supplies')]")


    #<---------------Test 7-------------------->

    current_testimonial = (By.XPATH,"//div[@class='swiper-slide swiper-slide-active']")
    next_testimonial_button = (By.XPATH,"//div[@aria-label='Next slide']")
    prev_testimonial_button = (By.XPATH,"//div[@aria-label='Previous slide']")




