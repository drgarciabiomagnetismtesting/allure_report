from selenium.webdriver.common.by import By

class BiomagnetismServiceElements:
    biomagnetism_service = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Biomagnetism Services'])[1]")
    service_dropdown = (By.XPATH,"(//ul[@class='sub-menu'])[4]/li/a")
    filter_cities = (By.XPATH,"(//div[@class='vp-filter vp-filter__style-default'])[1]/div/a")

    def get_city_xpath(city_name):
        return (By.XPATH,f"(//a[normalize-space()='{city_name.title()}'])[1]")

    load_more = (By.XPATH,"(//span[normalize-space()='Load More'])[1]")
    load_more2 = (By.XPATH,"(//a[@class='vp-pagination__load-more'])[1]")
    sort_filter = (By.XPATH,"(//div[@class='vp-portfolio__sort-wrap'])[1]/div/select")
    sort_options = (By.XPATH,"(//div[@class='vp-portfolio__sort-wrap'])[1]/div/select/option")

    drs_title = (By.XPATH,"//h2[@class='vp-portfolio__item-meta-title']")
    doctors = (By.XPATH,"//article")

    find_a_therapy = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Find a Therapist'])[1]")
    therapy_with_dr_garcia = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Therapy with Dr. Garcia'])[1]")
    
