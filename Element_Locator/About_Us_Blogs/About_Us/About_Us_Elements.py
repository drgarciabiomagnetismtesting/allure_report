from selenium.webdriver.common.by import By


class AboutUsElements:
    about_us = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='About Us'])[1]")
    welcome_video_button = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Welcome Video'])[1]")
    article_workpapper = (By.XPATH,"//span[contains(text(),'Articles & Working Papers')]")
    interviews = (By.XPATH,"(//span[@class='elementor-button-text'][normalize-space()='Interviews'])")
    research = (By.XPATH,"//span[contains(text(),'Research Experiences')]")
    bio = (By.XPATH,"//span[@class='elementor-button-text'][normalize-space()='Bio']")

    custom_play_button = (By.XPATH,"//i[@class='fa fa-play-circle']")
    #<---------Youtube------------------->
    youtube_screen = (By.XPATH, '//iframe')
    youtube_screen2 = (By.ID,"player")
    yt_play_pause_btn = (By.CLASS_NAME, 'ytp-play-button')
    video_current_progress = (By.CLASS_NAME, 'ytp-time-current')

    #<----------Dropdown------------------->
    article_work_paper_dropdown = (By.XPATH,"//li[@id='menu-item-15650']//span[@class='menu-text'][normalize-space()='Articles and Working Papers']")
    interviews_dropdown = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Interviews & Conferences'])[1]")
    research_dropdown = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Research experiences'])[1]")
