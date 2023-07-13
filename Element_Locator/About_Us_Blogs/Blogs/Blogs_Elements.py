from selenium.webdriver.common.by import By

class BlogsElements:
    
    blog = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Blogs'])[1]")
    faq = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='FAQ']")
    podcast = (By.XPATH,"(//span[@class='elementor-button-text'][normalize-space()='Podcasts'])[1]")
    reasearch = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Research']")

    all_blogs = (By.XPATH,"(//div[contains(@class,'health-and-wellness')])")

    def get_each_blog_xpath(index_number):

        blog_image_locator = (By.XPATH,f"(//div[@class='uael-post__thumbnail'])[{index_number}]/a/img")
        read_more_locator = (By.XPATH,f"(//a[@class='uael-post__read-more elementor-button'])[{index_number}]")
        heading_locator = (By.XPATH,f"(//h3[contains(@class,'uael-post__title')])[{index_number}]")
        return blog_image_locator,read_more_locator,heading_locator

    search = (By.XPATH,"(//form[@role='search'])[2]")
    search_input = (By.XPATH,"(//input[@type='search'])[2]")
    search_button = (By.XPATH,"//button[contains(text(),'Search')]")
    search_heading = (By.XPATH,"//h1[@class='page-title ast-archive-title']")

    recent_post = (By.XPATH,"(//aside[@id='block-22'])[1]")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    categories = (By.XPATH,"(//aside[@id='block-23'])[1]")
    comment_form = (By.XPATH,"//div[@id='comments']")

    comment_text_area = (By.XPATH,"//textarea[@id='comment']")
    name = (By.XPATH,"//input[@id='author']")
    email = (By.XPATH,"(//input[@id='email'])[1]")
    website = (By.XPATH,"(//input[@id='url'])[1]")
    save_details_for_next = (By.XPATH,"//input[@id='wp-comment-cookies-consent'])[1]")
    post_comment = (By.XPATH,"//input[@id='submit']")
    response = (By.XPATH,"//div[@id='wdpajax-info']/p")
