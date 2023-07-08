from selenium.webdriver.common.by import By

class ContactUsElements:

    contact_us_button = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Contact Us'])[1]")

    contact_form = (By.XPATH,"//form[@aria-label='Contact form']")
    contact_form_error = (By.XPATH,"(//span[@class='wpcf7-not-valid-tip'][normalize-space()='Please fill out this field.'])[3]")
    send_message_button = (By.XPATH,"//input[@value='Send Message']")

    name = (By.XPATH,"//input[@placeholder='Name*']")
    email = (By.XPATH,"//input[@placeholder='Email*']")
    phone = (By.XPATH,"//input[@placeholder='Mobile Number*']")
    subject = (By.XPATH,"//input[@placeholder='Subject*']")
    your_message = (By.XPATH,"//textarea[@placeholder='Your message']")


    thank_you_message = (By.XPATH,"(//div[@class='wpcf7-response-output'])[1]")




