from selenium.webdriver.common.by import By

class BlogsElements:
    blog = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Blogs'])[1]")
    faq = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='FAQ']")
    podcast = (By.XPATH,"(//span[@class='elementor-button-text'][normalize-space()='Podcasts'])[1]")
    reasearch = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Research']")