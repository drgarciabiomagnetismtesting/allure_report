from selenium.webdriver.common.by import By

class BiomagnetismElements:
    biomagnetism = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='What is Biomagnetism'])[1]")
    biomagnetism_dropdown = (By.XPATH,"(//ul[@class='sub-menu'])[2]")
    