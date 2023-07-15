from selenium.webdriver.common.by import By

class BiomagnetismElements:
    biomagnetism = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='What is Biomagnetism'])[1]")
    biomagnetism_dropdown = (By.XPATH,"(//ul[@class='sub-menu'])[2]/li/a")

    research = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Research']")
    biomagnetism_therapy_session = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Biomagnetism Therapy session'])[1]")
    biomagnetism_vs_magnet_therapy = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Biomagnetism vs Magnet Therapy'])[1]")
    faq = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='FAQs'][1]")
    faq2 = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='FAQ']")
    blogs = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Blogs']")
    podcast = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Podcasts']")

    background_image = (By.XPATH,"(//section[@class='elementor-section elementor-top-section elementor-element elementor-element-ddb2fe1 elementor-section-height-min-height elementor-section-boxed elementor-section-height-default elementor-section-items-middle'])[1]")
    background_heading = (By.XPATH,"//h1[normalize-space()='FAQs']")


    biomagnetism_faq = (By.XPATH,"(//a[@role='button'])[1]")
    biomagnetism_faq_session = (By.XPATH,"(//a[@role='button'])[2]")
    biomagnetism_faq_learner = (By.XPATH,"(//a[@role='button'])[3]")
    
    question = (By.XPATH,"(//div[@class='elementor-widget-container'])/h2")
    answare = (By.XPATH,"(//div[@class='elementor-widget-container'])/p")
    