from selenium.webdriver.common.by import By


class FooterElements:

    #<----------Test 13----------------->
    recent_posts = (By.XPATH,"(//div[@class='site-footer-primary-section-2 site-footer-section site-footer-section-2'])[1]")
    updates = (By.XPATH,"(//section[@id='block-20'])[1]")
    contacts = (By.XPATH,"(//div[@class='site-footer-primary-section-1 site-footer-section site-footer-section-1'])[1]")

    #<----------Test 14---------------->

    email_input = (By.XPATH,"(//input[@id='wpforms-10-field_2'])[1]")
    subscribe_button = (By.XPATH,"(//button[normalize-space()='Subscribe'])[1]")
    subscription_success = (By.XPATH,"""(//p[contains(text(),"Thanks for signing up for the newsletter! We'll be")])[1]""")

    #<----------Test 15---------------->

    recent_post_elements = (By.XPATH,"//nav[@aria-label='RECENT POSTS']/ul/li")

    #<----------Test 16---------------->

    location = (By.XPATH,"//a[normalize-space()='138 Riverbend Drive, North Brunswick, NJ 08902']")
    contact_no = (By.XPATH,"//a[normalize-space()='732-983-8616']")
    email_id = (By.XPATH,"//a[normalize-space()='info@drgarciabiomagnetism.com']")

    #Social_media_links
    facebook = (By.XPATH,"//a[@aria-label='facebook-f']")
    twitter = (By.XPATH,"//a[@aria-label='twitter']")
    pinterest = (By.XPATH,"//a[@aria-label='pinterest-p']")
    linkedin = (By.XPATH,"//a[@aria-label='linkedin-in']")
    instagram = (By.XPATH,"//a[@aria-label='instagram']")
    youtube = (By.XPATH,"//a[@aria-label='youtube']")

    #<------------Test 18---------------->
    copyright = (By.XPATH,"//div[@class='ast-footer-copyright']")

    #<------------Test 19---------------->
    privacy_policy = (By.XPATH,"//a[normalize-space()='Privacy Policy']")
    privacy_policy_heading = (By.XPATH,"//h4[normalize-space()='PRIVACY POLICY']")

    #<------------Test 20---------------->
    DB = (By.XPATH,"//a[normalize-space()='DB']")
    Forget_password = (By.XPATH,"//a[normalize-space()='Forgot your password?']")
